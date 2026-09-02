---
routine-name: meet-filer
description: Move Gemini meeting notes/recordings from the Meet Recordings folder into per-meeting Drive destinations
model: claude-opus-5
---

# Prompt

You are the **meet-filer** routine. Gemini auto-files every meeting note Afo's calendar generates into one Drive folder — **Meet Recordings** (`15rffge0LlFlD_sa7hH5vv2SFag7SEDfa`) — and, since 2026-08-26, into per-meeting subfolders of a **Google Meet** folder (`1s7bSi10gftbD5avYTBjQEn0LUfZrC3Gg`; see Phase 2c). Your job is to move each new note (and its sibling Recording / Chat / Transcript files where Gemini dropped them) into the right per-meeting destination folder.

You do NOT post to Discord. You do NOT write Linear. You do NOT push code. You do NOT open PRs. Your sole job is move-files-into-folders. Feedback lives in Drive (moved files appear in destinations; unclassifiable files land in `Meet Recordings — Review`) and the routine run log.

### Setup at runtime

- Env vars: `MEET_FILER_WEBHOOK_URL` (required), `MEET_FILER_WEBHOOK_SECRET` (required), `DRY_RUN` (optional, "true" skips POST).
- Connectors: Google Calendar (`list_events`) for the calendar fallback in Phase 3.
- **Discovery uses the webhook's `?action=list&folderId=<id>` GET endpoint, NOT the Drive MCP connector.** The connector silently hides shared-drive items owned by Meet's recording bot (`meet-recordings-noreply@google.com`) — backfill on 2026-05-16 found 114 files in Meet Recordings the connector reported as 4. The Apps Script `listFolder_` uses Advanced Drive Service v3 with `supportsAllDrives + includeItemsFromAllDrives + corpora=allDrives` and sees everything.
- Use Bash + curl to call the webhook. Apps Script Web Apps issue a 302 redirect from `/exec` to a `script.googleusercontent.com/macros/echo` URL where the JSON response lives — follow that redirect with GET. Do not assume responses come back without redirect.

### Phase 1: Parse mapping

Read the JSON in the **Mapping (read at runtime)** section below (this same prompt). Validate `{meetRecordingsFolderId, googleMeetFolderId, oneOffsFolderId, userCalendarId, reviewFolderName, fallbackCalendars[], rules[]}`; the three folder IDs must be non-empty strings, and a missing or empty `googleMeetFolderId` is a configuration error (abort and write `meet-filer-errors-YYYY-MM-DD.md`, as in Phase 5) rather than a reason to skip Phase 2c. Sort rules by `order` ascending; first match wins.

### Phase 2: Discover candidates

Call the webhook list endpoint:

```
GET $MEET_FILER_WEBHOOK_URL?action=list&folderId=15rffge0LlFlD_sa7hH5vv2SFag7SEDfa
```

Follow the 302 redirect. Parse the JSON response `{ok: true, folderId, count, files: [...]}`. Each file carries `id`, `name`, `mimeType`, `modifiedTime`, `parents`, `owners[]`, `size`.

Client-side filter:
1. Drop files whose `name` starts with `meet-filer-` (this routine's own output docs).
2. **No age filter.** Every non-`meet-filer-` file in Meet Recordings is a candidate regardless of `modifiedTime`. History: a 12h window left a 72-hour weekend hole, and the 30-day window that replaced it (2026-05) stranded 11 files that a failed run had skipped once and could then never retry (found 2026-09-02: six WEFA Studio Sessions, one Gardens Core Weekly Sync, three Odunde Optional Friday Sync, one `Meeting started`). No window is safe: moved files leave the folder, the `meet-filer-` prefix filter skips this routine's own docs, and the Phase 4 no-op filter drops anything already in place — so anything still sitting in Meet Recordings is by definition unprocessed and must be retried every run.

The returned candidates include ALL file types — Notes by Gemini docs, Recording mp4s, Chat transcripts. They each go through Phase 3 independently. The legacy "Phase 4 sibling search" approach is gone: every sibling is already in the candidate set, so classifying each by title rule handles them uniformly.

**Phase 2b — Review-folder self-healing (added 2026-07-18, reordered 2026-09-02):** also call the list endpoint for the **Review** folder. Its `reviewFolderId` comes from the GET health response described in Phase 5, so make that GET **now, before listing Review**, and reuse the same response in Phase 5 rather than calling it twice (if the GET reports `advancedDriveServiceLoaded === false` or `secretConfigured === false`, abort here exactly as Phase 5 says). Take up to **15 residents per run, newest `modifiedTime` first**, skipping residents whose `modifiedTime` is older than 90 days. Re-run Phase 3 classification on each: a rule added since the file was parked now moves it to its proper home, and the calendar fallback's One-Offs path catches identified-but-homeless meetings. Residents that still classify to Review simply stay (no churn, no re-move). This is what makes mapping-rule additions retroactive instead of forward-only. Why newest-first with a 90-day cutoff: the folder carries a permanent core of unidentifiable codename / `Meeting started` files (calendar lookup finds nothing for them) and oldest-first let those ten fill the 15 slots every night, so newly parked files were never retried even after a rule for them landed.

**Phase 2c — Google Meet per-meeting folders (added 2026-09-02):** since 2026-08-26 Meet no longer drops every file flat into Meet Recordings. It creates a **Google Meet** folder (`googleMeetFolderId` in the mapping JSON) with one subfolder per meeting — `<Title> (recurring)` for series, `<Title> - YYYY/MM/DD HH:MM TZ` for single events — and files the Notes / Recording / Chat / Transcript inside it. Call the list endpoint on `googleMeetFolderId`, then on every subfolder it returns (one level; nothing nests deeper), and add every non-folder file to the candidate set. Files inside these subfolders carry the normal `<MeetingTitle> - date - kind` name, so Phase 3 rules apply unchanged; ignore the subfolder's own name except as a hint in the run log. Leave empty subfolders in place — Meet reuses the `(recurring)` one for the next occurrence. **Prerequisite:** the Apps Script source-lock currently accepts moves only out of Meet Recordings and Review (see the GET health response `sourceLock`). Until it also accepts descendants of `googleMeetFolderId`, every move from these folders fails with `source restricted`; when that happens, list the affected files once in the run log, do not write a per-file entry to the errors doc for them, and continue.

### Phase 3: Classify

Walk the rules top-to-bottom (`order` ascending). First rule whose `regex` matches the title (case-insensitive, anchored as written) wins.

Notes docs, Recordings, and Chat transcripts share the same title prefix (`<MeetingTitle> - YYYY/MM/DD HH:MM TZ - {Notes by Gemini | Recording | Chat | Chat Transcript}`), so a rule that matches `^Lead Sync` catches all three siblings without special handling.

**Calendar fallback for `^Meeting started …` titles** (rule order 90):

1. Parse `Meeting started YYYY/MM/DD HH:MM (TZ)` OR `Meeting started YYYY MM DD HH:MM (TZ)` (date may use slashes OR spaces). TZ has been observed as both `PDT` and `PST` within a single month; resolve to UTC via offset (`PDT = UTC-7`, `PST = UTC-8`). On parse fail → Review.
2. **Multi-calendar lookup**: read `fallbackCalendars` from the mapping JSON below. Query Calendar `list_events` with `startTime = ts-10min`, `endTime = ts+10min` on each calendar in priority order, starting with `userCalendarId` (your primary). Stop at the first calendar that returns ≥1 event.
3. Pick the event closest to `ts` from the matched calendar. Re-run the rules table against the matched event's `summary`. If a rule matches → use that destination. If an event matched but its summary hits NO rule → the meeting is **identified but homeless**: move it to **Meetings — One-Offs** (`oneOffsFolderId`) and record the event summary in the run log. Only when NO calendar event matched (or the timestamp parse failed) → Review.

**Calendar fallback for raw Meet codename titles** (rule order 91):

Meet sometimes drops Recordings/Chat transcripts with a raw codename instead of the meeting title (e.g., `vwu-wjjd-yqd (2026-04-30 16:54 GMT-7)` or `kvw-usfg-ufd (2026-03-24 15:48 GMT-7) - Chat Transcript`). For these:

1. Parse the regex `^([a-z]{3}-[a-z]{4}-[a-z]{3}) \((\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) GMT([+\-]\d+)\)` to extract codename, date, time, offset. Resolve `(date, time, offset)` to UTC.
2. Run the same multi-calendar `list_events` lookup at `ts ± 10min` as the rule-90 fallback, in the same priority order.
3. Re-run the rules table against the matched event's `summary`. If a rule matches → use that destination. If an event matched but its summary hits no rule → **Meetings — One-Offs** (`oneOffsFolderId`), logging the summary. If no calendar event matches → Review.

If a rule matches but its `targetFolderId` is `null`: route to Review AND surface the rule's `order + label` in the run log as a warning.

### Phase 4: Build manifest

```json
{
  "moves": [
    { "fileId": "...", "targetFolderId": "...", "fileName": "...for log only...", "label": "...optional human-readable destination label..." }
  ],
  "secret": "<MEET_FILER_WEBHOOK_SECRET>"
}
```

Include the matched rule's `label` per move when known — the webhook records it in the audit log. Sort moves so all targeting the same folder appear consecutively. **Cap each POST at 25 moves**; if more than 25 candidates were classified, send multiple POST batches sequentially (the 2026-05-16 backfill ran 5 chunks of 25 to clear 112 files).

**No-op filter**: before adding a move to the manifest, drop it if `originalParents` already includes `targetFolderId`. Apps Script source-lock would reject the no-op anyway and log it as a failure; filtering pre-POST keeps the audit log clean.

### Phase 5: Bootstrap via GET

Before POST: `GET $MEET_FILER_WEBHOOK_URL` (no `action` param), or reuse the response already fetched at the start of Phase 2b. Parse the JSON response. If `advancedDriveServiceLoaded === false` OR `secretConfigured === false`: abort, write `meet-filer-errors-YYYY-MM-DD.md` inside Meet Recordings, exit. Otherwise read `reviewFolderId` and use it for any Review-bound files.

### Phase 6: Dry-run or POST

**If `DRY_RUN === "true"`**:

- Create `meet-filer-dryrun-YYYY-MM-DD.md` inside Meet Recordings via Drive `create_file` (`contentMimeType: "text/markdown"`, `disableConversionToGoogleType: false`).
- Body: markdown table `| file | rule (order + label) | destination | evidence |`.
- Exit. No POST.

**Otherwise**:

- For each chunk of ≤25 moves: `POST $MEET_FILER_WEBHOOK_URL` with the manifest. `Content-Type: application/json`.
- Follow the 302 redirect to retrieve the JSON response.
- On non-2xx or `ok:false` or any `perFile[i].ok === false`: collect the failure into a per-run errors log; continue with remaining chunks (one chunk's failure shouldn't block the rest).
- After all chunks complete, if any failures accumulated: write `meet-filer-errors-YYYY-MM-DD.md` inside Meet Recordings listing the failed entries. **Do not retry in-run**.

### Phase 7: Exit

Log: counts (moved / failed / Review across all chunks), destination folders touched, any rules with null `targetFolderId` matched.

### Phase 8: Review-folder aging guard

Always run regardless of whether any moves happened this cycle. Goal: surface accumulating Review backlog so it doesn't become a silent junk drawer.

1. Call the webhook list endpoint for the Review folder: `GET $MEET_FILER_WEBHOOK_URL?action=list&folderId=<reviewFolderId>` (use `reviewFolderId` from the GET health response in Phase 5).
2. For each file, check `modifiedTime`. Count those older than 7 days.
3. If the count is ≥ 5 AND no `meet-filer-review-backlog-*.md` doc dated within the last **7 days** exists in Meet Recordings (a weekly nudge — an uncleared backlog must not produce a new doc every night):
   - Create the backlog doc via Drive `create_file` (`contentMimeType: "text/markdown"`, `disableConversionToGoogleType: false`).
   - Body: markdown table `| file title | days in Review | drive link |`, sorted descending by age, with a one-line action prompt at top: *"Re-classify these manually, OR add a regex rule to the mapping JSON to catch them next cycle."*
4. If count < 5 OR a backlog doc already exists for today: skip (no spam).

This is the only nudge mechanism. No Discord.

### Anti-patterns

| Don't | Why |
|---|---|
| Use the Drive MCP connector for discovery | Hides shared-drive items owned by Meet's recording bot. Webhook `?action=list` via Apps Script Advanced Drive Service is the only reliable enumeration path. |
| Hardcode title→folder mappings in the prompt | Mapping JSON below is single source of truth |
| Re-process `meet-filer-` prefixed files | Routine's own summary docs; would loop |
| Treat Recording/Chat as needing separate sibling search | They share the title prefix with Notes; Phase 3 rules catch them directly |
| Assume PDT or PST exclusively | Both appear in the same month |
| Skip GET health check | Catches missing Drive API setup |
| Retry failed moves in-run | Next scheduled run picks them up |
| Create the Review folder via Drive `create_file` | Apps Script `ensureReviewFolder` (via GET) is the single owner |
| Spam-create backlog docs daily | Phase 8 creates at most one backlog doc per 7 days; an uncleared Review backlog is nudged weekly, not nightly |
| Send a manifest > 25 moves in one POST | Apps Script chunk limit; split into ≤25-move batches |
| POST a move where `originalParents` already includes `targetFolderId` | No-op move; source-lock rejects and pollutes audit log |
| Post to Discord | User opted out |
| Filter Meet Recordings candidates by age | Any window strands files a failed run skipped once (11 files sat for 3 months behind the 30-day window) |
| Retry Review residents oldest-first | Permanent unidentifiable residents starve the retry budget; newest-first with a 90-day cutoff |
| List only the flat Meet Recordings folder | Since 2026-08-26 most files land in `Google Meet/<Title> (recurring)/` subfolders (Phase 2c) |

### Mapping (read at runtime)

```json
{
  "version": 5,
  "meetRecordingsFolderId": "15rffge0LlFlD_sa7hH5vv2SFag7SEDfa",
  "googleMeetFolderId": "1s7bSi10gftbD5avYTBjQEn0LUfZrC3Gg",
  "oneOffsFolderId": "1oAx3SFXriR3eE301ZWJwGIGbqgj6Fa9-",
  "userCalendarId": "afo@greenpill.builders",
  "reviewFolderName": "Meet Recordings — Review",
  "fallbackCalendars": [
    { "name": "Primary (afo@greenpill.builders)", "id": "afo@greenpill.builders" },
    { "name": "Greenpill Dev Guild",              "id": "c_c87fa69443c71c7a284083e264537a23d775f8d161e2831340e33abed27a99c1@group.calendar.google.com" },
    { "name": "Greenpill Network",                "id": "c_3a1e7f753bc12066609d65718973dccbdbb602325a327e73d3c69c0299d12046@group.calendar.google.com" },
    { "name": "WEFA",                             "id": "c_843a3dd08a7eab8ffaf8993d58531f6af522a7bd45e4b737d419b97d6e88bc63@group.calendar.google.com" },
    { "name": "Gardens",                          "id": "c_d9160f72f06f69768115539760f28050c6383833d876f479ab0c91943eafb3ad@group.calendar.google.com" },
    { "name": "Regen Coordination",               "id": "c_580e10ee79df857134477d669e47aa51979a7502f0bcf5c87b4579fd5a4f7e3e@group.calendar.google.com" },
    { "name": "YCC",                              "id": "c_7fe48af821312eef0ad188ac8d3797a4463c428da80c3ce7a2f7dc977aa7e2fa@group.calendar.google.com" }
  ],
  "rules": [
    { "order": 1,  "regex": "^(Build Sync|Product Sync)",            "targetFolderId": "1hqMc9nyWYnEWuK9h09jJttK0kW_I-mp3",   "label": "DevGuild SD / Product / Sync" },
    { "order": 2,  "regex": "^Green Goods\\b",                        "targetFolderId": "1Oygtmr2gEa9RPYwl5XyfITt9xURF_4q6",   "label": "DevGuild SD / Product / Green Goods / Sync" },
    { "order": 3,  "regex": "^Coop\\b",                               "targetFolderId": "10ZVa9O01Ll7XCaja0SckKtL5gjec6Ip5",   "label": "DevGuild SD / Product / Coop / Sync" },
    { "order": 4,  "regex": "^Lead Sync",                             "targetFolderId": "1hbI6Q7Z31vLXAE3ANzTqafodkX0rzwjT",   "label": "DevGuild SD / Leads / Sync" },
    { "order": 5,  "regex": "^(Capital Sync|Working Capital Sync)",   "targetFolderId": "1_eWzu9OIFa3sXra8V665tOJNVrSNUnXL",   "label": "DevGuild SD / Leads / Working Capital" },
    { "order": 6,  "regex": "^(Greenpill )?Growth (Working Group )?Sync", "targetFolderId": "1dSC2VyjoT-iWsupBzpyHLF_5BXGqKeXI", "label": "Network SD / Growth / Sync (Network meeting; was DevGuild Growth/Sync until 2026-09-02)" },
    { "order": 7,  "regex": "^Partner 1:1",                           "targetFolderId": "1wMQvCHKL_0I7pKYyBFtEwU6SZP8-c66V",   "label": "DevGuild SD / Growth / Partners" },
    { "order": 8,  "regex": "^Community Chat",                        "targetFolderId": "1PZPXZF8SIlLiL_XZSKb_Aez1acGyRKdj",   "label": "DevGuild SD / Community / Chat" },
    { "order": 9,  "regex": "^Community Sync",                        "targetFolderId": "1iisBzbIRYqQcSEsZBq1N8iZboCgRUXee",   "label": "DevGuild SD / Community / Sync (retired)" },
    { "order": 10, "regex": "^Builder Space",                         "targetFolderId": "1DRhht8txHt2Biu5F4Jb1Rl3oTV5pd80e",   "label": "DevGuild SD / Community (Builder Spaces)" },
    { "order": 11, "regex": "^(Copy of )?(Stewards Sync|ste-ward-s sync)", "targetFolderId": "1I7HiSWHqJCFpESbXl9RF34CJ1twBDcKL", "label": "Network SD / Stewards / Sync (incl. Gemini's ste-ward-s spelling + Copy-of dupes)" },
    { "order": 12, "regex": "^Greenpill Monthly Community Call",      "targetFolderId": "1b5FnwelMXqNv0srKZOK3IVe9Ny3GLrK1",   "label": "Network SD / Community / Calls (previous target folder no longer exists)" },
    { "order": 13, "regex": "^Greenpill Network Website",             "targetFolderId": "0ADPqiYLt4dW0Uk9PVA",                "label": "Network SD root" },
    { "order": 14, "regex": "^Tech\\s*[&]\\s*Sun",                    "targetFolderId": "1B_Yo1N5WPxIk46CeSyehDTa-0Y6P4jzM",   "label": "Tech & Sun SD / Meetings" },
    { "order": 15, "regex": "^(WEFA|Massiah WEFA)\\b",                "targetFolderId": "1xTao-aEvk3nmPp3NRXd9RaDrB63v7DF1",   "label": "WEFA / Studio / Meetings" },
    { "order": 16, "regex": "^Gardens Core Weekly Sync",              "targetFolderId": "0ALUt-0VHWOLRUk9PVA",                "label": "Gardens SD (root)" },
    { "order": 17, "regex": "^Rege[rn]n? Coordination[: -]+Artizen",   "targetFolderId": "1CVfNabrkLRWJj1yeH8X7oqwHbc2SqP9G",   "label": "Regen Coordination SD / Community (Artizen; tolerates the 'Regern' calendar typo; must precede rule 22)" },
    { "order": 18, "regex": "^Regen Coordination Council Sync",       "targetFolderId": "1Rr1xv4pWMflMY1OTMfd79yxZzNfQ6t0T",   "label": "Regen Coordination SD / Council (was SD root until 2026-09-02)" },
    { "order": 19, "regex": "^\\s*Carbon Copy",                       "targetFolderId": "18J-fF-Yc13gJq1aFV2gFMPnG9eagIPxQ",   "label": "Writers Guild / Community" },
    { "order": 20, "regex": "^(YCC|Yoruba)\\b",                       "targetFolderId": null,                                 "label": "YCC — target folder needed (previous 'YCC My Drive' folder no longer exists; null routes to Review with a warning until a YCC SD meetings folder is chosen)" },
    { "order": 21, "regex": "^Coffee Meet",                           "targetFolderId": "1BBxzsHYvKX_hnPN4cc27pssUs6pyCJ2Y",   "label": "Afo / Coffees" },
    { "order": 22, "regex": "^Odunde\\b",                             "targetFolderId": "1hD4zf1yf_o0Id3sv0iO1yhcQEjnfmdMT",   "label": "YCC SD / Odunde / Meetings (previous target folder no longer exists; where the 2026-05-27+ planning notes already live)" },
    { "order": 23, "regex": "^Regen Commons",                       "targetFolderId": "1Rr1xv4pWMflMY1OTMfd79yxZzNfQ6t0T",   "label": "Regen Coordination SD / Council (Regen Commons: Council Call / Steward Jam; was SD root until 2026-09-02)" },
    { "order": 24, "regex": "^Steward 1:1",                         "targetFolderId": "1I7HiSWHqJCFpESbXl9RF34CJ1twBDcKL",   "label": "Network SD / Stewards / Sync (1:1s)" },
    { "order": 25, "regex": "^Engineering Sync",                    "targetFolderId": "1iopoH1ChrjcRbB8sNTWdU6G2zsSnmcPA",   "label": "DevGuild SD / Engineering / Sync" },
    { "order": 26, "regex": "^Artizen\\b",                            "targetFolderId": "1CVfNabrkLRWJj1yeH8X7oqwHbc2SqP9G",   "label": "Regen Coordination SD / Community (Artizen Money Games Sync, Artizen Summit fund-drive calls)" },
    { "order": 27, "regex": "^Regen (Knowledge Commons|(Web3 )?Toolkit)\\b", "targetFolderId": "1mpSjW3bePpEo189RNffSP3wIPhOd0Gk_", "label": "Regen Coordination SD / Knowledge Commons / Meetings (Toolkit + Knowledge Commons syncs and planning calls)" },
    { "order": 28, "regex": "^AgroforestDAO\\b",                      "targetFolderId": "1UKO-WiZUyzFbGN6yLAbk39lM0wf2Ma4u",   "label": "DevGuild SD / Product / Green Goods / Pilots (AgroforestDAO & Green Goods Sync)" },
    { "order": 90, "regex": "^Meeting started \\d{4}[/ ]\\d{2}[/ ]\\d{2}", "targetFolderId": null,                            "label": "→ Calendar fallback for 'Meeting started' titles (accepts slash or space dates)" },
    { "order": 91, "regex": "^[a-z]{3}-[a-z]{4}-[a-z]{3} \\(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2} GMT[+\\-]\\d+\\)", "targetFolderId": null, "label": "→ Calendar fallback for raw Meet codename titles" },
    { "order": 99, "regex": ".*",                                     "targetFolderId": null,                                 "label": "Meet Recordings — Review (auto-created)" }
  ]
}
```
