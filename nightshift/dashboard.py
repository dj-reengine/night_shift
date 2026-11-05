"""Night Shift dashboard. The page is what is going on. The log files are what went on."""

import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from nightshift.digest import digest_line
from nightshift.queue import dismiss, set_priority, snapshot

CHICAGO = ZoneInfo("America/Chicago")

FEEDS = {
    "mail_summit": ("Email - Summit", "summit"),
    "mail_reengine": ("Email - ReEngine", "reengine"),
    "extract": ("Proposal", "proposal"),
    "hubspot": ("HubSpot", "hubspot"),
    "qb_note": ("QuickBooks", "quickbooks"),
    "synopsis": ("Synopsis", "synopsis"),
    "tdhca": ("TDHCA", "tdhca"),
}


def _feed(kind):
    return FEEDS.get(kind or "", ("Night Shift", "reengine"))


PRIORITY_FACE = {
    "high": ("High", "high"),
    "standard": ("Medium", "medium"),
    "low": ("Low", "low"),
}


def _priority(value):
    return PRIORITY_FACE.get(value or "", ("", ""))


def _entity(item):
    payload = item.get("payload") if isinstance(item.get("payload"), dict) else {}
    return (item.get("entity") or payload.get("entity") or "").strip()

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Night Shift</title>
<style>
  :root {
    color-scheme: light;
    --bg: #eef1f6; --ink: #12141a; --card: #ffffff; --line: #e3e7ee;
    --muted: #5d6573; --pin: #fff6ea; --bad: #9f2d2d;
    --tdhca: #2f5d8c; --summit: #2f6b4f; --reengine: #8c5a2f;
    --shadow: 0 1px 2px rgba(18, 20, 26, .06);
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --bg: #0f1218; --ink: #f4f6f8; --card: #191e27; --line: #2c3340;
    --muted: #a7b0bd; --pin: #3a2c18; --bad: #ffb4b4;
    --shadow: none;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font: 15px/1.5 ui-sans-serif, system-ui, sans-serif; background: var(--bg); color: var(--ink); }
  header, main { max-width: 820px; margin: 0 auto; padding: 22px 20px; }
  header { padding-bottom: 0; }
  h1 { font-size: 1.35rem; font-weight: 650; letter-spacing: -0.03em; margin: 0; }
  h2 { font-size: 0.78rem; font-weight: 650; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin: 28px 0 8px; }
  .row { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
  .top { display: flex; justify-content: space-between; gap: 12px; align-items: center; }
  button, select, input { font: inherit; color: inherit; background: var(--card); border: 1px solid var(--line); border-radius: 999px; padding: 7px 12px; }
  button { cursor: pointer; }
  input[type="search"] { border-radius: 999px; min-width: 180px; }
  .digest { font-size: 1.35rem; font-weight: 600; letter-spacing: -0.03em; line-height: 1.3; margin: 18px 0 8px; }
  .alert { color: var(--bad); }
  .card, .pin, .job { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 16px 16px 46px; margin: 10px 0; box-shadow: var(--shadow); }
  .pin { background: var(--pin); padding-bottom: 16px; }
  .tag { font: 11px/1 sans-serif; letter-spacing: 0.06em; text-transform: uppercase; font-weight: 650; }
  .job, .card { position: relative; }
  .job h3, .card h3 { margin: 4px 0; font-size: 1.02rem; font-weight: 640; letter-spacing: -0.02em; }
  .copy { padding-right: 132px; }
  .feed { position: absolute; top: 14px; right: 14px; font: 11px/1.2 sans-serif; font-weight: 650; color: #fff; border-radius: 999px; padding: 4px 8px; }
  .feed.tdhca { background: var(--tdhca); color: #fff; }
  .feed.summit { background: var(--summit); color: #fff; }
  .feed.reengine { background: var(--reengine); color: #fff; }
  .feed.hubspot { background: #6b3fa0; color: #fff; }
  .feed.proposal { background: #245c6b; color: #fff; }
  .feed.quickbooks { background: #2f6b4f; color: #fff; }
  .feed.synopsis { background: #8c5a2f; color: #fff; }
  .pri { position: absolute; right: 14px; bottom: 14px; font: 11px/1.2 sans-serif; font-weight: 650; color: #fff; border-radius: 999px; padding: 4px 8px; }
  .pri.high { background: #d06a12; }
  .pri.medium { background: #2f6b4f; }
  .pri.low { background: #2f5d8c; }
  .actions { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 12px; }
  .days { display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; }
  .days button[aria-pressed="true"] { background: var(--ink); color: var(--bg); border-color: var(--ink); }
  .tokens { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 10px 0 4px; }
  .token { background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px; }
  .token b { display: block; font-size: 1.35rem; letter-spacing: -0.03em; }
  #modal { position: fixed; inset: 0; background: rgba(10, 12, 16, .48); display: flex; align-items: center; justify-content: center; }
  #modal[hidden] { display: none; }
  #modal form { background: var(--card); color: var(--ink); padding: 18px; border-radius: 16px; width: min(440px, 92vw); }
  #modal textarea { width: 100%; min-height: 96px; box-sizing: border-box; border-radius: 12px; }
  .tdhca { color: var(--tdhca); } .summit { color: var(--summit); } .reengine { color: var(--reengine); }
  a { color: inherit; }
  .muted { color: var(--muted); font-size: 13px; }
  .subject { margin: 0; }
</style>
</head>
<body>
<header>
  <div class="top">
    <h1>Night Shift</h1>
    <button id="theme" type="button">Dark mode</button>
  </div>
  <div class="row">
    <select id="filter">
      <option value="">Everything</option>
      <option>TDHCA</option>
      <option>Summit</option>
      <option>ReEngine</option>
    </select>
    <input id="search" type="search" placeholder="Search">
    <button id="run-queue" type="button">Run queue</button>
  </div>
</header>
<main id="app"></main>
<div id="modal" hidden>
  <form id="remove-form">
    <p>Why are you removing this from the queue?</p>
    <textarea id="why" required></textarea>
    <div class="row"><button type="submit">Remove</button><button id="cancel" type="button">Cancel</button></div>
  </form>
</div>
<script>
const app = document.querySelector("#app");
const filter = document.querySelector("#filter");
const search = document.querySelector("#search");
const theme = document.querySelector("#theme");
if (localStorage.getItem("nightshift-theme") === "dark") document.documentElement.dataset.theme = "dark";
theme.onclick = () => {
  const dark = document.documentElement.dataset.theme !== "dark";
  document.documentElement.dataset.theme = dark ? "dark" : "";
  localStorage.setItem("nightshift-theme", dark ? "dark" : "light");
};
function esc(value) {
  return String(value ?? "").replace(/[&<>"]/g, ch => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;" }[ch]));
}
function wanted(item) {
  const vertical = (item.vertical || "").toLowerCase();
  const pick = filter.value.toLowerCase();
  if (pick && vertical !== pick) return false;
  const q = search.value.trim().toLowerCase();
  if (!q) return true;
  return JSON.stringify(item).toLowerCase().includes(q);
}
async function setPriority(id, priority) {
  await fetch("/api/jobs/" + id + "/priority", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ priority }) });
  load();
}
async function runNow(id) {
  await fetch("/api/jobs/" + id + "/run-now", { method: "POST" });
  load();
}
function central(iso) {
  if (!iso) return "";
  const when = new Date(iso);
  if (Number.isNaN(when.getTime())) return iso;
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: "America/Chicago",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit",
    hourCycle: "h23"
  }).formatToParts(when);
  const get = (type) => (parts.find(part => part.type === type) || {}).value || "00";
  const hour = get("hour") === "24" ? "00" : get("hour");
  return get("year") + "-" + get("month") + "-" + get("day") + " " + hour + ":" + get("minute") + ":" + get("second");
}
function proposalName(item) {
  const title = item.title || "";
  if (item.feed !== "Proposal" || !item.entity) return title;
  if (title.toLowerCase().includes(String(item.entity).toLowerCase())) return title;
  return item.entity + " — " + title;
}
function priorityMark(item) {
  if (!item.priority_label) return "";
  return `<span class="pri ${esc(item.priority_class)}">${esc(item.priority_label)}</span>`;
}
function whenLine(job) {
  const queued = central(job.created_at);
  const sent = central(job.sent_at);
  if (sent) return `<div class="muted">Sent ${esc(sent)}</div><div class="muted">Queued ${esc(queued)}</div>`;
  return `<span class="muted">${esc(queued)}</span>`;
}
let removing = "";
let latest = null;
let logDay = "";
function count(value) {
  return Number(value || 0).toLocaleString("en-US");
}
function askRemove(id) {
  removing = id;
  document.querySelector("#why").value = "";
  document.querySelector("#modal").hidden = false;
  document.querySelector("#why").focus();
}
async function createMeeting(start, end, button) {
  button.disabled = true;
  const response = await fetch("/api/calendar/tdhca-meeting", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ start, end })
  });
  const text = await response.text();
  if (!response.ok) {
    button.disabled = false;
    alert(text);
    return;
  }
  load();
}
function logView(state) {
  const days = state.log || [];
  if (!days.length) return `<h2>Log</h2><p class="muted">Nothing logged yet.</p>`;
  if (!logDay || !days.some(day => day.day === logDay)) logDay = days[0].day;
  const day = days.find(item => item.day === logDay) || days[0];
  const runs = (day.runs || []).filter(wanted);
  const removed = (day.removed || []).filter(wanted);
  return `
    <h2>Log</h2>
    <div class="days">${days.map(item => `<button type="button" data-day="${esc(item.day)}" aria-pressed="${item.day === day.day}">${esc(item.day)}</button>`).join("")}</div>
    <div class="tokens">
      <div class="token"><b>${count(day.tokens_in)}</b><span class="muted">Tokens in</span></div>
      <div class="token"><b>${count(day.tokens_out)}</b><span class="muted">Tokens out</span></div>
    </div>
    <h2>Ran</h2>
    ${runs.map(card => `<div class="card"><span class="feed ${esc(card.feed_class)}">${esc(card.feed)}</span><div class="copy"><span class="tag ${esc(card.vertical)}">${esc(card.vertical)}</span><h3><a href="${esc(card.href)}">${esc(proposalName(card))}</a></h3><p>${esc(card.summary)}</p><p class="muted">${esc(central(card.finished_at))} · in ${count(card.tokens_in)} · out ${count(card.tokens_out)}</p></div></div>`).join("") || `<p class="muted">Nothing ran.</p>`}
    <h2>Removed</h2>
    ${removed.map(item => `<div class="card"><span class="feed ${esc(item.feed_class)}">${esc(item.feed)}</span><div class="copy"><h3>${esc(item.who || item.title)}</h3>${item.subject ? `<p class="subject">${esc(item.subject)}</p>` : ""}${item.entity ? `<p>${esc(item.entity)}</p>` : ""}<p>${esc(item.reason)}</p><p class="muted">${esc(central(item.removed_at))}</p></div></div>`).join("") || `<p class="muted">Nothing removed.</p>`}
  `;
}
function paint() {
  const state = latest;
  if (!state) return;
  const jobs = state.queue.filter(wanted);
  const pins = state.pinned.filter(wanted);
  app.innerHTML = `
    <p class="digest">${esc(state.digest)}</p>
    ${state.failures.map(item => `<p class="alert">${esc(item)}</p>`).join("")}
    ${state.offline ? `<p class="alert">The Mac did not pick up work.</p>` : ""}
    <p class="muted">Mac: ${esc(state.utilization)}. Times are Central.</p>
    <h2>Pinned</h2>
    ${pins.map(item => `<div class="pin"><span class="tag ${esc(item.vertical)}">${esc(item.vertical)}</span> ${esc(item.text)}</div>`).join("") || `<p class="muted">Nothing pinned.</p>`}
    <h2>Waiting</h2>
    ${jobs.map(job => `<div class="job"><span class="feed ${esc(job.feed_class)}">${esc(job.feed)}</span>${priorityMark(job)}<div class="copy"><span class="tag ${esc(job.vertical)}">${esc(job.vertical)}</span><h3>${esc(proposalName(job))}</h3>${job.subject ? `<p class="subject">${esc(job.subject)}</p>` : ""}${whenLine(job)}</div>
      <div class="actions"><button data-id="${esc(job.id)}" data-p="high">High</button><button data-id="${esc(job.id)}" data-p="standard">Medium</button><button data-id="${esc(job.id)}" data-p="low">Low</button><button data-id="${esc(job.id)}" data-remove="1">Remove</button></div></div>`).join("") || `<p class="muted">Nothing queued.</p>`}
    ${logView(state)}
    <p class="muted">All time · in ${count(state.stats.tokens_in)} · out ${count(state.stats.tokens_out)} · runs ${count(state.stats.runs)} · failures ${count(state.stats.failures)}</p>`;
  app.querySelectorAll("button[data-p]").forEach(button => {
    button.onclick = () => setPriority(button.dataset.id, button.dataset.p);
  });
  app.querySelectorAll("button[data-remove]").forEach(button => {
    button.onclick = () => askRemove(button.dataset.id);
  });
  app.querySelectorAll("button[data-day]").forEach(button => {
    button.onclick = () => { logDay = button.dataset.day; paint(); };
  });
}
function load() {
  fetch("/api/state").then(r => r.json()).then(state => { latest = state; paint(); });
}
filter.onchange = paint;
search.oninput = paint;
document.querySelector("#run-queue").onclick = async () => {
  await fetch("/api/run", { method: "POST" });
  load();
};
load();
setInterval(load, 30000);
document.querySelector("#cancel").onclick = () => { document.querySelector("#modal").hidden = true; };
document.querySelector("#remove-form").onsubmit = async (event) => {
  event.preventDefault();
  const reason = document.querySelector("#why").value.trim();
  if (!reason || !removing) return;
  const response = await fetch("/api/jobs/" + removing + "/remove", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ reason })
  });
  document.querySelector("#modal").hidden = true;
  if (!response.ok) alert(await response.text());
  load();
};
</script>
</body>
</html>
"""

GAP_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TDHCA calendar gap</title>
<style>
  body { margin: 0; font: 15px/1.5 ui-sans-serif, system-ui, sans-serif; background: #eef1f6; color: #12141a; }
  main { max-width: 820px; margin: 0 auto; padding: 22px 20px; }
  a { color: inherit; }
  .muted { color: #5d6573; font-size: 13px; }
  .slot { display: grid; grid-template-columns: 1fr auto; gap: 12px; align-items: center; padding: 12px 0; border-bottom: 1px solid #e3e7ee; }
  .when { white-space: nowrap; }
  button { font: inherit; background: #fff; border: 1px solid #e3e7ee; border-radius: 999px; padding: 7px 12px; }
</style>
</head>
<body>
<main>
  <p><a href="/">Night Shift</a></p>
  <h1>TDHCA calendar gap</h1>
  <div id="app"></div>
</main>
<script>
function esc(value) {
  return String(value ?? "").replace(/[&<>"]/g, ch => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;" }[ch]));
}
async function createMeeting(start, end, button) {
  button.disabled = true;
  const response = await fetch("/api/calendar/tdhca-meeting", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ start, end })
  });
  if (!response.ok) {
    button.disabled = false;
    alert(await response.text());
    return;
  }
  load();
}
function load() {
  fetch("/api/state").then(r => r.json()).then(state => {
    const gaps = state.gaps || { fill: [], add: [] };
    const fill = gaps.fill || [];
    const add = gaps.add || [];
    const app = document.querySelector("#app");
    if (!fill.length && !add.length) {
      app.innerHTML = `<p>ReEngine already has something opposite each TDHCA block.</p>`;
      return;
    }
    app.innerHTML = `
      ${fill.length ? `<h2>Add on ReEngine</h2>` : ""}
      ${fill.map(item => `<div class="slot"><span class="when">${esc(item.label)}. Private TDHCA Meeting.</span><button type="button" data-start="${esc(item.start)}" data-end="${esc(item.end)}">Create</button></div>`).join("")}
      ${add.length ? `<h2>Add on TDHCA</h2>` : ""}
      ${add.map(item => `<div class="slot"><span class="when">${esc(item.label)}${item.title ? " (" + esc(item.title) + ")" : ""}</span></div>`).join("")}
    `;
    app.querySelectorAll("button[data-start]").forEach(button => {
      button.onclick = () => createMeeting(button.dataset.start, button.dataset.end, button);
    });
  });
}
load();
</script>
</body>
</html>
"""

def _vertical(value):
    text = (value or "").lower()
    if text in ("tdhca", "summit", "reengine"):
        return text
    return ""


def _central_day(iso):
    if not iso:
        return ""
    try:
        when = datetime.fromisoformat(iso)
    except ValueError:
        return ""
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return when.astimezone(CHICAGO).strftime("%Y-%m-%d")


FEED_VERTICAL = {
    "Email - Summit": "summit",
    "Email - ReEngine": "reengine",
    "Proposal": "reengine",
    "HubSpot": "summit",
    "QuickBooks": "summit",
    "Synopsis": "reengine",
    "TDHCA": "tdhca",
}
FEED_CLASS = {
    "Email - Summit": "summit",
    "Email - ReEngine": "reengine",
    "Proposal": "proposal",
    "HubSpot": "hubspot",
    "QuickBooks": "quickbooks",
    "Synopsis": "synopsis",
    "TDHCA": "tdhca",
}


def build_log(results, removals):
    """Group finished work and removals by Central calendar day."""
    days = {}

    def bucket(day):
        return days.setdefault(day, {"day": day, "tokens_in": 0, "tokens_out": 0, "runs": [], "removed": []})

    for item in results:
        day = _central_day(item.get("finished_at"))
        if not day:
            continue
        entry = bucket(day)
        tokens_in = int(item.get("tokens_in") or 0)
        tokens_out = int(item.get("tokens_out") or 0)
        entry["tokens_in"] += tokens_in
        entry["tokens_out"] += tokens_out
        href = ""
        paths = item.get("artifact_paths") or []
        if paths:
            href = "/artifacts/" + os.path.basename(paths[0])
        if item.get("type") == "tdhca":
            href = "/tdhca"
        entry["runs"].append({
            "title": item.get("title") or item.get("id"),
            "entity": _entity(item),
            "vertical": _vertical(item.get("vertical")),
            "feed": _feed(item.get("type"))[0],
            "feed_class": _feed(item.get("type"))[1],
            "summary": item.get("summary") or "",
            "finished_at": item.get("finished_at") or "",
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "href": href or "#",
        })
    for item in removals:
        day = (item.get("removed_at_ct") or "")[:10] or _central_day(item.get("removed_at"))
        if not day:
            continue
        feed = item.get("feed") or "Night Shift"
        bucket(day)["removed"].append({
            "title": item.get("title") or "",
            "who": item.get("who") or "",
            "subject": item.get("subject") or "",
            "entity": item.get("entity") or "",
            "reason": item.get("reason") or "",
            "removed_at": item.get("removed_at") or "",
            "feed": feed,
            "feed_class": FEED_CLASS.get(feed, "reengine"),
            "vertical": FEED_VERTICAL.get(feed, ""),
        })
    ordered = [days[key] for key in sorted(days, reverse=True)]
    for day in ordered:
        day["runs"].sort(key=lambda item: item.get("finished_at") or "", reverse=True)
        day["removed"].sort(key=lambda item: item.get("removed_at") or "", reverse=True)
    return ordered


def build_state(root):
    data = snapshot(root)
    failed = data["failed"]
    claimed = data["claimed"]
    results = sorted(data["results"], key=lambda item: item.get("finished_at") or "", reverse=True)
    sensitive = next((item for item in results if item.get("sensitivity")), None)
    unbilled = next((item for item in results if item.get("unbilled")), None)
    gap = next((item for item in results if item.get("tdhca_gap_today")), None)
    drift = next((item for item in results if item.get("drift")), None)
    stalled = next((item for item in claimed if item.get("stalled")), None)
    second = failed[-1] if failed else None
    line = digest_line({
        "second_failure": f"{second['title']} failed a second time." if second else "",
        "stalled": f"{stalled['title']} is stalled." if stalled else "",
        "sensitive_draft": f"A draft needs review: {sensitive['title']}." if sensitive else "",
        "unbilled": unbilled.get("summary") if unbilled else "",
        "tdhca_gap_today": gap.get("summary") if gap else "",
        "drift": drift.get("summary") if drift else "",
    })
    mac = data["mac"] or {}
    seen = mac.get("seen_at") or ""
    offline = True
    if seen:
        try:
            when = datetime.fromisoformat(seen)
            age = (datetime.now(timezone.utc) - when).total_seconds()
            offline = age > 15 * 60
        except ValueError:
            offline = True
    cards = []
    for item in results:
        href = ""
        paths = item.get("artifact_paths") or []
        if paths:
            href = "/artifacts/" + os.path.basename(paths[0])
        if item.get("type") == "tdhca":
            href = "/tdhca"
        cards.append({
            "title": item.get("title") or item.get("id"),
            "entity": _entity(item),
            "vertical": _vertical(item.get("vertical")),
            "feed": _feed(item.get("type"))[0],
            "feed_class": _feed(item.get("type"))[1],
            "priority_label": _priority(item.get("priority"))[0],
            "priority_class": _priority(item.get("priority"))[1],
            "summary": item.get("summary") or "",
            "finished_at": item.get("finished_at") or "",
            "href": href or "#",
        })
    pinned = []
    for item in failed:
        pinned.append({"vertical": _vertical(item.get("vertical")), "text": f"{item.get('title')} failed a second time."})
    for item in claimed:
        if item.get("stalled"):
            pinned.append({"vertical": _vertical(item.get("vertical")), "text": f"{item.get('title')} is stalled."})
    for item in results:
        if item.get("sensitivity"):
            pinned.append({"vertical": _vertical(item.get("vertical")), "text": f"Review the draft for {item.get('title')}."})
        if item.get("unbilled"):
            pinned.append({"vertical": "summit", "text": item.get("summary") or "A client has no invoice."})
    queue = []
    for job in sorted(data["queue"], key=lambda item: item.get("created_at") or ""):
        payload = job.get("payload") if isinstance(job.get("payload"), dict) else {}
        queue.append({
            "id": job["id"],
            "title": job.get("title") or job["type"],
            "subject": (payload.get("subject") or "") if str(job.get("type") or "").startswith("mail") else "",
            "entity": _entity(job),
            "vertical": _vertical(job.get("vertical")),
            "feed": _feed(job.get("type"))[0],
            "feed_class": _feed(job.get("type"))[1],
            "priority": job.get("priority") or "standard",
            "priority_label": _priority(job.get("priority") or "standard")[0],
            "priority_class": _priority(job.get("priority") or "standard")[1],
            "created_at": job.get("created_at") or "",
            "sent_at": job.get("received_at") or payload.get("received_at") or "",
        })
    high = next((job for job in data["queue"] if job.get("priority") == "high"), None)
    target = high or (data["queue"][0] if data["queue"] else None)
    gaps = {"fill": [], "add": []}
    gaps_path = os.path.join(root, "gaps.json")
    if os.path.exists(gaps_path):
        with open(gaps_path, encoding="utf-8") as handle:
            gaps = json.load(handle)
    failures = []
    for item in failed:
        failures.append(f"{item.get('title')} failed a second time.")
    for job in data["queue"]:
        if job.get("attempt", 1) > 1:
            failures.append(f"{job.get('title')} failed once and is queued again.")
    removals = []
    removals_path = os.path.join(root, "removals.json")
    if os.path.isfile(removals_path):
        with open(removals_path, encoding="utf-8") as handle:
            removals = (json.load(handle).get("items") or [])
    return {
        "digest": line,
        "failures": failures,
        "offline": offline,
        "utilization": mac.get("utilization") or "offline",
        "cards": cards,
        "pinned": pinned,
        "queue": queue,
        "log": build_log(results, removals),
        "gaps": gaps,
        "stats": data["stats"],
        "run_now_id": target["id"] if target else "",
    }


class Handler(BaseHTTPRequestHandler):
    root = "/var/lib/night-shift"

    def log_message(self, fmt, *args):
        return

    def _send(self, code, body, content_type):
        payload = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self._send(200, PAGE, "text/html; charset=utf-8")
            return
        if path == "/tdhca":
            self._send(200, GAP_PAGE, "text/html; charset=utf-8")
            return
        if path == "/api/state":
            self._send(200, json.dumps(build_state(self.root)), "application/json")
            return
        if path.startswith("/artifacts/"):
            name = os.path.basename(path[len("/artifacts/"):])
            file_path = os.path.join(self.root, "artifacts", name)
            if os.path.isfile(file_path):
                with open(file_path, "rb") as handle:
                    self._send(200, handle.read(), "text/plain; charset=utf-8")
                return
        self._send(404, "Not found", "text/plain; charset=utf-8")

    def do_POST(self):
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            body = {}
        parts = [part for part in path.split("/") if part]
        if len(parts) == 4 and parts[0] == "api" and parts[1] == "jobs" and parts[3] == "priority":
            try:
                job = set_priority(self.root, parts[2], body.get("priority"))
            except ValueError:
                self._send(400, "Bad priority", "text/plain; charset=utf-8")
                return
            if job is None:
                self._send(404, "Not queued", "text/plain; charset=utf-8")
                return
            self._send(200, json.dumps(job), "application/json")
            return
        if len(parts) == 4 and parts[0] == "api" and parts[1] == "jobs" and parts[3] == "run-now":
            job = set_priority(self.root, parts[2], "high")
            if job is None:
                self._send(404, "Not queued", "text/plain; charset=utf-8")
                return
            job["run_now"] = True
            from nightshift.queue import _write
            _write(os.path.join(self.root, "queue", job["id"] + ".json"), job)
            self._send(200, json.dumps(job), "application/json")
            return
        if path == "/api/run":
            from nightshift.queue import _jobs, _write
            started = 0
            for job in _jobs(os.path.join(self.root, "queue")):
                job["run_now"] = True
                _write(os.path.join(self.root, "queue", job["id"] + ".json"), job)
                started += 1
            self._send(200, json.dumps({"started": started}), "application/json")
            return
        if len(parts) == 4 and parts[0] == "api" and parts[1] == "jobs" and parts[3] == "remove":
            try:
                job = dismiss(self.root, parts[2], body.get("reason"))
            except ValueError:
                self._send(400, "Say why you are removing it.", "text/plain; charset=utf-8")
                return
            if job is None:
                self._send(404, "Not queued", "text/plain; charset=utf-8")
                return
            self._send(200, json.dumps({"id": job["id"]}), "application/json")
            return
        if path == "/api/calendar/tdhca-meeting":
            start = body.get("start") or ""
            end = body.get("end") or ""
            if not start or not end:
                self._send(400, "Missing time.", "text/plain; charset=utf-8")
                return
            try:
                from nightshift.calendar_job import create_tdhca_meeting
                from nightshift.envfile import env_path, load
                env = load(env_path())
                env["_env_path"] = env_path()
                create_tdhca_meeting(env, start, end)
            except Exception as error:
                self._send(403, str(error), "text/plain; charset=utf-8")
                return
            gaps_path = os.path.join(self.root, "gaps.json")
            if os.path.isfile(gaps_path):
                with open(gaps_path, encoding="utf-8") as handle:
                    gaps = json.load(handle)
                gaps["fill"] = [item for item in gaps.get("fill") or [] if item.get("start") != start]
                with open(gaps_path, "w", encoding="utf-8") as handle:
                    json.dump(gaps, handle)
            self._send(200, json.dumps({"created": True}), "application/json")
            return
        self._send(404, "Not found", "text/plain; charset=utf-8")


def serve(root, port):
    os.makedirs(root, exist_ok=True)
    Handler.root = root
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()
