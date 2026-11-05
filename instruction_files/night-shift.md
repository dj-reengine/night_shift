# Night Shift

The dashboard shows what is waiting on you, what failed, and today's calendar, and the log records what changed overnight and what was suggested.

Night Shift uses idle time on David's MacBook Pro (M5 Pro, 18 CPU cores, 64 GB) to run easier AI work locally, overnight and whenever the machine is otherwise idle. Frontier models stay reserved for the hard problems. A local mid-size instruct model is enough for structured, repeatable work.

Proxmox is the always-on triage device. It decides what deserves a job, holds the queue, writes Gmail drafts, and hosts the Night Shift dashboard. The Mac polls Proxmox. Proxmox does not push, and the Mac opens no inbound ports.

Status as of 2026-11-04: decided design, nothing built yet. Build defaults below are the spec to plan against.

Out of scope: file sync, Seafile, the public-speaking bot, proposal-folder cleanup, billing, and anything else in the source notes that is not a Night Shift job.

## Transcripts

Night Shift reads transcripts only from `stored_transcripts` on ReEngine My Drive. Every transcript it should see will be in that folder. A file in that folder is already assigned. Night Shift does not read a holding area, does not sign off files, and does not move or file them.

The assignment already on the file is the first word of its name: GSL-MSD, BHCC, ReEngine admin, Summit (admin or Summit plus a client name), or TDHCA. Night Shift uses that word to choose the project. It does not run a second assignment step.

## Skill files

David writes the five specialist skill files as the work proceeds. The active-project synopsis does not run until all five exist. Other Night Shift jobs do not wait on them.

The five files, one persona each:

- Six Sigma: flag steps with too much variation; suggest a control chart where that fits.
- Lean. The specific check is not set yet. David sets it in the skill file.
- Theory of Constraints: point out where work piles up before a bottleneck.
- Change management, leaning on ProSci: notice client-team resistance and suggest different framing.
- Project management, leaning on PMI.

## RAG vault

The proposal extractor cross-references the ReEngine RAG vault. David is fixing two-way RAG sync on 2026-11-04, before the first overnight run. Night Shift does not build that sync. The extractor assumes the vault is available on the Mac when it runs.

The project synopsis reads the new transcript or email. It does not query the RAG vault unless a skill file says so.

## Proxmox triage

Proxmox triages ReEngine, Summit, and TDHCA. It writes the queue. If Proxmox is down, the Mac retries later and queued jobs stay queued.

### What gets a job

- Proposal solicitations. The trigger is the Decision column on Primary Tracking. When David sets Decision to Pursue, any capitalization, Night Shift sets `Extracted` to `queued` and enqueues the row. `none` and a blank cell both mean it has not been queued. A row David has set to `done` by hand is skipped, even if Decision is Pursue. There is no folder watcher.
- Active ReEngine projects. A worker checks `stored_transcripts` and project email for anything new since the last run. With nothing new, it does nothing. With something new, it adds the project to the queue. The synopsis half of this job stays off until the five skill files exist.
- ReEngine mail and Summit mail that need a response. Rules are under Mail.
- Summit QuickBooks. Proxmox pulls and diffs overnight. The Mac analyzes the diff. Details are under QuickBooks.
- Summit HubSpot digest. Weekly. Runs Sunday night and is on Monday's dashboard.
- TDHCA calendar gap. Fixed nightly schedule, every night, with no other conditions and no dependence on the Mac being idle. It needs no model.

### Job identity and lifecycle

- Every job has a unique ID keyed to its trigger, so the same transcript, email message, solicitation, QuickBooks night, HubSpot week, or calendar date cannot spawn a second job.
- The Mac marks a job claimed on the first grab. A later poll cannot take it again.
- Claimed means the Mac has taken it. Complete means the work finished. A claimed job with no progress past the stall timeout shows on the dashboard as stalled.
- The first failure returns the job to the queue. The second failure alerts David on the dashboard.
- Jobs enter at standard priority. David can move any job to high or low from the queue view. Within a priority level, jobs run first-in, first-out.
- One model job runs at a time.

### TDHCA calendar gap

David's TDHCA email account is state-owned and locked down by IT. No sync tools are approved. Only busy/free status crosses from TDHCA to Google Calendar, with no event details or titles.

The nightly job reads the TDHCA-flagged calendar and the ReEngine calendar through the Google Calendar API, compares them by time slot only, and emails David a mismatch report each morning. The same result feeds the dashboard calendar strip, together with the Summit and ReEngine calendars.

Calendar reads for ReEngine, Summit, and David Tasks use the existing Capacities service account, `capacities-io@capacities-io.iam.gserviceaccount.com`. Those three calendars are shared with that account. TDHCA cannot be shared, and its Google embed link does not return events to a server. TDHCA is read from the Outlook source URL in `TDHCA_CALENDAR_ICS_URL`. That feed is what Google is subscribed to. A fetch returns the calendar with no browser login.

- A TDHCA busy block with no ReEngine event opposite it is a gap to fill by hand.
- A ReEngine event during TDHCA free time may need to be added on the TDHCA side.
- The job only reads. It does not write either calendar and it does not sync them.

Ignore these ReEngine events when looking for a TDHCA counterpart:

- The David Tasks calendar. Those are soft blocks for completing tasks.
- Events that are not out-of-office and have no other person invited. Those are personal time blocks for a separate time-entry scraper. Night Shift does not build that scraper.

A ReEngine event counts as a real commitment when it is out-of-office or has at least one other attendee. Out-of-office means either the calendar flags it as out-of-office, or the title contains "out of office" (case-insensitive). Either condition is enough.

## Mail

Same rules for Summit and ReEngine.

The ReEngine email bot already categorizes that mailbox. Night Shift drafts only the ReEngine messages that bot marked as needing a response. Summit has no categorizer. The local model sorts Summit mail in the same pass as the draft, and it drafts only what it marks as needing a response. Newsletters, receipts, and FYI mail get no draft on either account.

The bot's handoff is section 6 of `Documents/ReEngine/Email Triage/reengine-email-triage.md` on the Mac. Night Shift drafts only rows flagged REPLY. ACTION, DECIDE, and WATCH stay in the file and get no draft.

- **Evening run, after the workday and before 9:30pm CT.** The bot reads INBOX and the RFPs label for mail since the last evening run, writes or updates REPLY rows with the Gmail thread id and the inbound message id, and closes rows David already answered. It does not save the Gmail draft. Night Shift drafts those open REPLY rows overnight.
- **Morning run, close-out only.** The bot reads Sent mail against the open rows and closes anything David already answered. It does not add new REPLY rows. Those wait for the evening run.

Nothing sends, ever. The end of the line is a message sitting in Gmail Drafts. The Mac has no mail credentials. The Proxmox writer has no send capability: it creates the draft by IMAP `APPEND` into Drafts and sets the `AI` label over IMAP. The Gmail API is not linked into that writer. A model cannot call send, because no send function and no send credential exist on either machine.

Path:

1. Proxmox packages the message, the thread, a short sample of David's sent mail for voice, and whether a draft already exists.
2. The Mac writes the draft text and a sensitivity flag. The text is clean: no generated-by footer, and no AI wording in the subject or body. The voice sample is the prompt's guide.
3. The Mac hands that text back to Proxmox in the result file.
4. Proxmox appends it to Drafts.

Sensitivity, until David logs the full rules: scheduling, confirmations, and admin are drafted for morning review with no extra flag. Mail that carries client names, dollar figures, or strategy is still only a draft, and it is flagged on the dashboard for review before David sends it himself. Routine mail does not send itself.

Leave a thread alone once a draft has been suggested. If Night Shift has already suggested a draft for that inbound message and David has not sent a reply on the thread, the next night does not reprocess it, even if he deleted the draft. After David sends a reply, a newer inbound message that needs a response gets one new draft. The trigger key is the account, the thread, and that inbound message id.

## QuickBooks

Overnight Summit job. Proxmox does the extract. The Mac does the reading.

- Proxmox pulls a full extract through the QuickBooks API, saves it as CSV, and diffs it against the prior night's snapshot. Keep 13 months. The oldest month rolls off monthly. The API needs care around auth and pagination. Analysts read the snapshot rather than calling the live API.
- Proxmox also computes the unbilled set: clients who emailed overnight and have no invoice on file. That match is a join, not a model judgment.
- The Mac, when idle, reads the diff and the unbilled set. It writes a short note on what changed, and it phrases each unbilled flag in this shape: "This client reached out about work, and there's no invoice on file for them yet, so you might want to bill before the work piles up."

## Mac, when it is idle

Ollama on this Mac is the runtime. LM Studio is not. One instruct model stays loaded. Thinking mode is off for every Night Shift call, so drafts stay clean and jobs finish.

Serve routine summaries, drafts, classification, extraction, and the QuickBooks note from that model. Context for a call is 32,768 tokens. A solicitation or transcript longer than that is chunked. Asking for the model's full advertised window will push this 64 GB machine into swap and make it look busy.

Local models own extraction, matching, classification, summarization, and first-draft writing. Frontier models own the prose that has to win: narrative, differentiators, and the compliance-matrix write-up on proposals. The local model can flag confidence in the extractor JSON. The pursue-or-pass decision stays with David in the tracking sheet.

### When a job may start

User input outranks CPU. Background sync spikes CPU and is not "David is working."

- On battery, start nothing. If power is lost mid-job, finish the current model call, then stop.
- On AC power, start work when there has been no keyboard, mouse, or trackpad input for 10 minutes and the 3-minute CPU average is under 25 percent.
- From 9:30pm to 6:30am CT, on AC power, the wait is 3 minutes without input and the same CPU average. Evening use still wins.
- Do not start a new job while input is happening, or while the 3-minute CPU average is at or above 25 percent.
- If input resumes, or CPU stays at or above 60 percent for 45 seconds, finish the current model call only if it is already underway and under a minute old. Otherwise stop, put the job back in the queue, and wait until the machine is idle again.
- While the overnight window is open, or a job is running, on AC power, hold idle sleep off (`caffeinate -ims`), including with the lid closed. Release that hold when the queue is empty and the window is closed, or when the machine is on battery.
- The TDHCA calendar job and the QuickBooks extract run on Proxmox. They do not wait on this watcher. Model jobs do.
- The Mac polls every 2 minutes while it is allowed to work, and every 10 minutes while it is not, so a Run now is still picked up.
- No token progress and no file progress for 20 minutes is a stall. That counts as a failure.

David can jump the queue with Run now from the dashboard when a deadline is tight. Run now still waits if he is actively using the machine, unless he confirms he wants it anyway. The offline-Mac notice uses the same control.

## Models

Installed on this Mac on 2026-11-04. None of them is the Night Shift workhorse.

| Model | Size | Night Shift |
| --- | --- | --- |
| `qwen2.5-coder:32b` | 19 GB | Leave. Coding work uses it. Wrong model for drafts and extraction. |
| `qwen-wide` | 19 GB | Leave. Same coder weights, wider context. |
| `qwen2.5-coder:1.5b` | 1 GB | Leave. Too small for these jobs. |
| `bhmud-r1-32b-ctx32k` | 19 GB | Leave. Named project model. Thinking model, poor fit for clean drafts. |
| `deepseek-r1:32b` | 19 GB | Leave if you use it by hand. Night Shift does not load it. |
| `deepseek-r1:latest` (8.2B) | 5.2 GB | Safe to delete if you do not use the small R1 by hand. Night Shift does not load it. |
| `deepseek-r1:70b` | 42 GB | Delete if you do not use it by hand. On 64 GB it cannot hold a long solicitation or transcript beside the system. A thinking model also dirties draft text. |
| `nomic-embed-text` | 274 MB | Leave. Embeddings for the RAG vault. |

Add one model and use it for every Night Shift call:

`qwen3.8:27b` (about 18 GB, Q4_K_M, long context). Thinking is on by default in that model. Night Shift turns it off per request. Pull it when the build starts. Do not add a second Night Shift model. Specialists are five prompts on this model, then one synthesizer pass on the same loaded model.

## Workloads the Mac runs

### Proposal solicitation extractor

- Pull every mandatory requirement, deadline, and evaluation criterion from the solicitation.
- Record the website where the proposal is submitted, and whether submittal is electronic or hard-copy.
- Cross-reference each item against the RAG vault and past performance. Confidence is not a pursue-or-pass call.
- Write one markdown file, `night_shift_results_[solicitation_name].md`, into that solicitation's local deal folder (`deals/NNN_Slug/`). The name is the solicitation filename without its extension. The file stays on local disk. It is not written into the Drive folder. The submission website and the electronic or hard-copy method are in that file.
- On later runs, recheck the submission website recorded in that file. When the page changes, append a dated note to the same file. A hard-copy solicitation with no website has nothing to recheck. This check runs only when the results file already exists.
- If the local deal folder does not exist yet, the job waits until the scanner has created it, then writes the file there.
- When that file has been created, Night Shift sets `Extracted` to `done`. The sheet receives only that status.
- A row already set to `done`, including one David set by hand, is not queued and does not get a file.

### ReEngine active-project synopsis

Runs only after the five skill files exist. Volume stays low: at most two meetings a day, and many emails are administrative.

Each specialist reads only the new material and posts one short finding. A synthesizer merges those findings into one narrative, so the result reads as one advisor.

Append a dated section to one running markdown file per project, in that project's local folder. Never overwrite the file. The section is a timeline of what changed and what was suggested, and a skim sheet before a client call. The Mac also sends that new section back to Proxmox so the dashboard can link to it.

Charter check in every run: say whether the last meeting moved the project closer to its stated objectives or drifted.

Every suggestion cites the specific artifact it came from.

### ReEngine and Summit email drafts

Described under Mail. The Mac returns text and a sensitivity flag. Proxmox creates the draft.

### QuickBooks note and unbilled flags

Described under QuickBooks. The Mac returns the note and the phrased flags. Proxmox already holds the CSV, the diff, and the unbilled set.

### Weekly HubSpot digest

Sunday night, Summit only. The local model reads the week's HubSpot activity and writes a one-pager: stalled deals, promised follow-ups, and anything about to slip. ReEngine uses HubSpot to track government-contracting deals, so this digest stays off the ReEngine side. Proxmox stores the one-pager for the Monday dashboard.

## Night Shift dashboard

Internal website on Proxmox. David opens it in the morning to see what ran and what is still waiting.

Top of the page, in order:

- One-line daily digest. Pick the first line that applies, and stop: a second failure or a stalled job; else a sensitivity-flagged draft; else an unbilled client; else a TDHCA gap that affects today; else a charter check that says a project drifted; else "Queue clear." This is a fixed order, not another model call.
- Quiet failure alert for a job that failed once and was requeued, and for a job that failed twice.
- Calendar strip: what is coming up today across verticals, from the TDHCA calendar-gap result plus the Summit and ReEngine calendars.
- Offline-Mac notice with Run now, when the Mac did not pick up work.

The board:

- Filters for TDHCA, Summit, ReEngine, or everything.
- Color coding by those verticals.
- Dark mode toggle.
- Cards with a timestamp and a link to the output file. For a solicitation, that link opens `night_shift_results_[solicitation_name].md`. That file is the hyperlink.
- Search across projects.
- One living markdown file per project. Nightly jobs append to it.
- A pinned section for flagged items: sensitivity flags, unbilled clients, stalls, and second failures.

Queue and usage:

- Queue view of everything currently queued on Proxmox, not only what already ran. From that view David sets high, standard, or low priority.
- Utilization state: working, paused because the Mac is in use, or paused because it is on battery.
- Per-job stats: tokens in, tokens out, runtime, success or fail. Cumulative counters climb and are not reset. No cost line.
- Stalled jobs and second-failure alerts show here.

## Where files live

The Mac opens no listener. It pulls job files from Proxmox and pushes results back over SSH, using a key that can only see this tree.

Proxmox:

- `/var/lib/night-shift/queue/` jobs waiting
- `/var/lib/night-shift/claimed/` taken by the Mac
- `/var/lib/night-shift/results/` one JSON per finished attempt
- `/var/lib/night-shift/artifacts/` extractor JSON, synopsis sections, draft bodies, QuickBooks CSV and diff, HubSpot one-pager
- `/var/lib/night-shift/failed/` second failures

Mac spool, so a Proxmox blip does not drop a job already in progress:

- `~/Library/Application Support/Night Shift/incoming/`
- `~/Library/Application Support/Night Shift/work/`
- `~/Library/Application Support/Night Shift/outbox/`

A job file is JSON: `id`, `trigger_key`, `type`, `priority`, `attempt`, `created_at`, and `payload_path`. Claiming is an atomic move from `queue/` to `claimed/` with `claimed_at` set. The Mac writes `results/{id}.json` with status, token counts, runtime, sensitivity, and artifact paths. Proxmox then moves the job from `claimed/` to done state by deleting it from `claimed/` after the result is stored. A second poll finds nothing left to claim.

## Still open

- David will log the full email sensitivity rules later. Until then, client names, dollar figures, and strategy are the flag.
- David writes the five skill files. The synopsis stays off until they exist.
- Lean's check is whatever David puts in that skill file.
