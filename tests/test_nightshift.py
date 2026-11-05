import json
import os
import tempfile
import unittest
from datetime import datetime

from nightshift.calendar_gap import compare, is_real_commitment
from nightshift.digest import digest_line
from nightshift.queue import claim_next, complete, enqueue, fail, release


def at(hour):
    return datetime(2026, 11, 5, hour, 0)


class DigestTest(unittest.TestCase):
    def test_order(self):
        self.assertEqual(digest_line({}), "Queue clear.")
        self.assertEqual(
            digest_line({"drift": "GSL drifted.", "unbilled": "Bill Acme."}),
            "Bill Acme.",
        )
        self.assertEqual(
            digest_line({"second_failure": "Mail failed a second time.", "unbilled": "Bill Acme."}),
            "Mail failed a second time.",
        )


class CalendarTest(unittest.TestCase):
    def test_ignores_personal_and_tasks(self):
        self.assertFalse(is_real_commitment({"calendar": "David Tasks", "title": "Write", "attendees": []}))
        self.assertFalse(is_real_commitment({"title": "Focus", "attendees": []}))
        self.assertTrue(is_real_commitment({"title": "Out of office Friday", "attendees": []}))
        self.assertTrue(is_real_commitment({"title": "Client", "attendees": [{"self": False}]}))

    def test_slots(self):
        busy = [{"start": at(9), "end": at(10)}]
        events = [
            {"title": "Focus", "start": at(9), "end": at(10), "attendees": []},
            {"title": "Client", "start": at(13), "end": at(14), "attendees": [{"self": False}]},
        ]
        result = compare(busy, events)
        self.assertEqual(result["fill"], [])
        self.assertEqual(result["add"][0]["title"], "Client")

    def test_uncovered_tdhca_is_a_gap(self):
        result = compare([{"start": at(9), "end": at(10)}], [])
        self.assertEqual(len(result["fill"]), 1)
        self.assertEqual(result["add"], [])

    def test_span_is_central_clock(self):
        from zoneinfo import ZoneInfo
        from nightshift.calendar_job import format_span
        chicago = ZoneInfo("America/Chicago")
        start = datetime(2026, 11, 4, 9, 0, 0, tzinfo=chicago)
        end = datetime(2026, 11, 4, 10, 30, 15, tzinfo=chicago)
        self.assertEqual(format_span(start, end), "2026-11-04 09:00:00–10:30:15 CT")

    def test_log_groups_a_central_day(self):
        from nightshift.dashboard import build_log
        log = build_log(
            [{
                "id": "a", "type": "extract", "title": "Bid", "vertical": "reengine",
                "finished_at": "2026-11-05T04:00:00+00:00", "tokens_in": 10, "tokens_out": 4,
            }],
            [{
                "feed": "Email - Summit", "title": "Note", "reason": "blast",
                "removed_at": "2026-11-05T03:00:00+00:00", "removed_at_ct": "2026-11-04 21:00:00",
            }],
        )
        self.assertEqual(log[0]["day"], "2026-11-04")
        self.assertEqual(log[0]["tokens_in"], 10)
        self.assertEqual(log[0]["tokens_out"], 4)
        self.assertEqual(log[0]["removed"][0]["reason"], "blast")


class QueueTest(unittest.TestCase):
    def test_claim_once_and_retry(self):
        with tempfile.TemporaryDirectory() as root:
            enqueue(root, {"id": "b", "trigger_key": "mail-2", "type": "mail", "title": "Later", "created_at": "2026-11-05T02:00:00+00:00", "priority": "standard"})
            enqueue(root, {"id": "a", "trigger_key": "mail-1", "type": "mail", "title": "First", "created_at": "2026-11-05T01:00:00+00:00", "priority": "high"})
            again = enqueue(root, {"id": "c", "trigger_key": "mail-1", "type": "mail", "title": "Dup"})
            self.assertIsNone(again)
            first = claim_next(root)
            self.assertEqual(first["id"], "a")
            second = claim_next(root)
            self.assertEqual(second["id"], "b")
            self.assertIsNone(claim_next(root))
            self.assertEqual(fail(root, "b")["outcome"], "requeued")
            self.assertEqual(fail(root, "b")["outcome"], "failed")
            self.assertTrue(os.path.exists(os.path.join(root, "failed", "b.json")))
            complete(root, "a", {"status": "ok", "tokens_in": 3, "tokens_out": 4, "summary": "done"})
            self.assertFalse(os.path.exists(os.path.join(root, "claimed", "a.json")))
            self.assertIsNone(enqueue(root, {"id": "d", "trigger_key": "mail-1", "type": "mail", "title": "Again"}))

    def test_a_held_job_lets_the_next_one_run(self):
        with tempfile.TemporaryDirectory() as root:
            enqueue(root, {"id": "a", "trigger_key": "file-1", "type": "extract", "title": "Missing", "created_at": "2026-11-05T01:00:00+00:00", "priority": "high"})
            enqueue(root, {"id": "b", "trigger_key": "note-1", "type": "synopsis", "title": "Note", "created_at": "2026-11-05T02:00:00+00:00", "priority": "standard"})
            claimed = claim_next(root)
            release(root, claimed["id"], retry_after="2099-01-01T00:00:00+00:00")
            self.assertEqual(claim_next(root)["id"], "b")

    def test_dismiss_keeps_the_trigger(self):
        from nightshift.queue import dismiss
        with tempfile.TemporaryDirectory() as root:
            enqueue(root, {"id": "a", "trigger_key": "mail-1", "type": "mail", "title": "Hold"})
            with self.assertRaises(ValueError):
                dismiss(root, "a", "  ")
            gone = dismiss(root, "a", "Already handled")
            self.assertEqual(gone["removed_reason"], "Already handled")
            self.assertFalse(os.path.exists(os.path.join(root, "queue", "a.json")))
            self.assertIsNone(enqueue(root, {"id": "b", "trigger_key": "mail-1", "type": "mail", "title": "Again"}))
            with open(os.path.join(root, "removals.json"), encoding="utf-8") as handle:
                log = json.load(handle)
            self.assertEqual(log["items"][0]["reason"], "Already handled")
            self.assertEqual(log["items"][0]["title"], "Hold")
            self.assertNotIn("body", log["items"][0])


class TranscriptTest(unittest.TestCase):
    def test_hannah_is_not_an_assigned_project(self):
        from nightshift.google_data import project_of
        self.assertEqual(project_of("Hannah"), "")
        self.assertEqual(project_of("BHCC_transcripts"), "BHCC")
        self.assertEqual(project_of("Summit Admin 2026-07-14 Meeting.txt"), "Summit")
        self.assertEqual(project_of("GSL-MSD kickoff"), "GSL-MSD")
        self.assertEqual(project_of("tdhca board"), "TDHCA")

    def test_specialist_prompt_is_the_short_instruction(self):
        from nightshift.model_jobs import _specialist_prompt
        prompt = _specialist_prompt("lean.md")
        self.assertLess(len(prompt), 600)
        self.assertIn("new material", prompt.lower())

    def test_summary_is_created_then_appended(self):
        from nightshift.model_jobs import _append_project_summary
        with tempfile.TemporaryDirectory() as root:
            os.makedirs(os.path.join(root, "BHCC"))
            path, created = _append_project_summary("BHCC", "\n\n## 2026-11-05\n\nFirst.\n", root)
            self.assertTrue(created)
            self.assertTrue(path.endswith(os.path.join("BHCC", "night_shift.md")))
            again, created_again = _append_project_summary("BHCC", "\n\n## 2026-11-06\n\nSecond.\n", root)
            self.assertFalse(created_again)
            self.assertEqual(path, again)
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            self.assertIn("First.", text)
            self.assertIn("Second.", text)
            self.assertEqual(text.count("# BHCC"), 1)


class MailFilterTest(unittest.TestCase):
    def test_noise_is_noreply_bulk_or_unaddressed(self):
        from nightshift.dispatcher import mail_is_noise

        me = "david@summitfinancial.solutions"
        self.assertTrue(mail_is_noise("HubSpot <noreply@notifications.transactional.hubspot.com>", "041907 is your HubSpot Log In Code"))
        self.assertTrue(mail_is_noise("Intuit <do_not_reply@intuit.com>", "Someone created a new app"))
        self.assertTrue(mail_is_noise("OfficeDepotOrders@officedepot.com", "Order Confirmation #1", {"To": me}, me))
        self.assertTrue(mail_is_noise("QuickBooks Payments <BusinessServices@intuit.com>", "Money on the way!", {"List-Unsubscribe": "yes", "To": me}, me))
        self.assertTrue(mail_is_noise("Julie Zhu <julie.zhu@tryadorabl.com>", "Sorry we missed you", {"To": "guests@example.com"}, me))
        self.assertFalse(mail_is_noise("Ford Meadows <fordameadows@gmail.com>", "Fwd: New Statement Available", {"To": me}, me))
        self.assertFalse(mail_is_noise("Ford Meadows <fordameadows@gmail.com>", "Fwd: New Statement Available"))

    def test_thread_is_settled_after_a_reply(self):
        from nightshift.dispatcher import _parse_thrid, reply_settled_reason

        me = "david@summitfinancial.solutions"
        self.assertEqual(reply_settled_reason(f"David <{me}>", "Ford <ford@example.com>", "", me), "Already answered this thread")
        self.assertEqual(reply_settled_reason("Alex <alex@example.com>", "Sam <sam@example.com>", "", me), "The latest reply is not to me")
        self.assertEqual(reply_settled_reason("Ford <ford@example.com>", f"David <{me}>", "", me), "")
        self.assertEqual(reply_settled_reason("Alex <alex@example.com>", "Sam <sam@example.com>", f"David <{me}>", me), "")
        sample = [(b"1 (X-GM-THRID 1278455344230334865 BODY[HEADER.FIELDS] {8}", b"From: a\r\n"), b")"]
        self.assertEqual(_parse_thrid(sample), "1278455344230334865")


class IdleTest(unittest.TestCase):
    def test_night_and_day_and_battery(self):
        from datetime import timezone
        from zoneinfo import ZoneInfo
        from nightshift.idle import gate, should_pause

        chicago = ZoneInfo("America/Chicago")
        night = datetime(2026, 11, 4, 22, 0, tzinfo=chicago)
        day = datetime(2026, 11, 4, 15, 0, tzinfo=chicago)
        self.assertEqual(gate(True, 200, 10, night), "start")
        self.assertEqual(gate(True, 100, 10, night), "in use")
        self.assertEqual(gate(True, 700, 10, day), "start")
        self.assertEqual(gate(True, 500, 10, day), "in use")
        self.assertEqual(gate(False, 9999, 0, night), "battery")
        self.assertEqual(gate(True, 9999, 30, night), "busy")
        self.assertFalse(should_pause(10, None))
        self.assertFalse(should_pause(50, 10))
        self.assertTrue(should_pause(50, 120))
        self.assertIsNotNone(timezone.utc)


class TextAndFeedTest(unittest.TestCase):
    def test_chunk_and_clean_draft(self):
        from nightshift.textutil import chunk_text, draft_is_clean
        parts = chunk_text("x" * 20000, max_tokens=3000, reserve_tokens=1000)
        self.assertGreater(len(parts), 1)
        self.assertTrue(draft_is_clean("Thanks, I will send the form."))
        self.assertFalse(draft_is_clean("Generated by a language model"))

    def test_mail_module_has_no_send(self):
        import inspect
        import nightshift.mail_writer as mail_writer
        source = inspect.getsource(mail_writer)
        self.assertFalse(hasattr(mail_writer, "send"))
        self.assertNotIn(".send(", source)
        self.assertNotIn("smtplib", source)

    def test_ics_free_is_not_busy(self):
        from nightshift.ics_feed import busy_blocks, parse_events
        text = """BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20261105T090000
DTEND:20261105T100000
SUMMARY:Busy
END:VEVENT
BEGIN:VEVENT
DTSTART:20261105T110000
DTEND:20261105T120000
SUMMARY:Free
END:VEVENT
END:VCALENDAR
"""
        blocks = busy_blocks(parse_events(text))
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["summary"], "Busy")

    def test_reply_rows_need_ids(self):
        from nightshift.triage import reply_rows
        text = """## 6. Needs response
| Flag | Who | What's needed | Deadline | First seen | Thread id | Inbound msg id | Status |
|---|---|---|---|---|---|---|---|
| REPLY | Brooke | Kickoff | ASAP | Nov 3 | thr1 | msg1 | open |
| REPLY | Mandy | Invoice | ASAP | Nov 3 | | | open |
| ACTION | Payroll | Run it | Nov 5 | Oct 30 | thr2 | msg2 | open |
| REPLY | Augusta | License | Nov 4 | Nov 3 | thr3 | msg3 | draft-exists |
"""
        rows = reply_rows(text)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["who"], "Brooke")


class ReleaseTest(unittest.TestCase):
    def test_release_does_not_count_a_failure(self):
        from nightshift.queue import release
        with tempfile.TemporaryDirectory() as root:
            enqueue(root, {"id": "a", "trigger_key": "mail-1", "type": "mail", "title": "Hold"})
            self.assertEqual(claim_next(root)["id"], "a")
            self.assertEqual(release(root, "a")["id"], "a")
            self.assertEqual(claim_next(root)["id"], "a")
            self.assertFalse(os.path.exists(os.path.join(root, "failed", "a.json")))


if __name__ == "__main__":
    unittest.main()
