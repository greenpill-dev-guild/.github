---
name: scorecard-pulse
description: Monthly outcome scorecard — refreshes indicator registers, posts per-initiative readouts, flags drift between cards, fields, registers, and strategy docs.
schedule: "0 10 1 * *"  # 1st of month 10:00 UTC, one hour after stipend-ledger
environment: guild-routines
model: claude-opus-4-8[1m]
connectors:
  - linear  # OAuth connector only — NO stored API key (guild rule)
env:
  - DISCORD_BOT_TOKEN
  - DISCORD_LEAD_COUNCIL_CHANNEL_ID
status: active
---

# Scorecard Pulse

## Why this exists

The outcome layer froze once before: in June 2026 the indicator registers were built and then sat untouched for four weeks while the initiatives drifted. This pulse is the mechanism that keeps outcomes, indicators, and strategy docs honest — it refreshes what can be read mechanically and flags what has drifted, once a month, in one pass. The operating model is defined in `docs/strategy/scorecard-and-branch-map.md` in this repo (mirrored by a Linear reference doc on the ops shelf); where that document and this spec disagree on indicator policy, the document wins.

## Scope contract

- **Reads:** Linear initiatives, their `Indicator Register` documents, projects, issues (label/state counts), status updates; public HTTP (Karma GAP API, public RPC/explorers) via curl for on-chain rows.
- **Writes:** `Indicator Register` documents (Current / As-of cells only), one initiative status update per active outcome initiative per month, one #lead-council Discord message.
- **Never:** creates/edits/deletes issues or projects; never edits outcome cards, strategy docs, or any other document; never invents a value; never writes to GitHub or any repo.

## Phase 0 — Preflight (fail closed)

1. Linear connector check: `list_initiatives`. If unauthorized or unreachable → post ONE Discord line to #lead-council ("scorecard-pulse: Linear connector needs re-authorization — skipped this month.") and exit. Never scout blind.
2. Discord env check (`DISCORD_BOT_TOKEN` + `DISCORD_LEAD_COUNCIL_CHANNEL_ID`). Discord down but Linear up → run the Linear half and record the Discord failure in the closing line. Both down → exit non-zero.
3. Idempotency: for each target initiative, look for an existing status update this calendar month carrying the signature line (Phase 4). Same-month re-run → refresh that update in place via its id; never duplicate.

## Phase 1 — Read

- All initiatives: status, health, targetDate, updatedAt, full description.
- Each Active or Planned **outcome** initiative's `Indicator Register` document. Skip status-only surfaces (any initiative whose card says status-only) and Completed/Canceled initiatives — their registers are closed pointers.
- The rules from `docs/strategy/scorecard-and-branch-map.md` in the .github clone.
- Whether a Linear document titled `Strategy — {current quarter}` (e.g. `Strategy — Q3 2026`) exists on the `Guild Operating System` shelf. Strategy is written as a new Linear edition each quarter; a missing edition means the quarterly review has not happened.

## Phase 2 — Compute (auto-derivable only)

Refresh a register row's Current/As-of ONLY where the source is mechanically readable this run:

- **Linear-derivable:** `funding:*` counts by stage (Growth team), open P0/P1 counts, COM cycle throughput, MAR briefs completed in window, release-project state and milestone progress, GIF v0.1 milestone progress.
- **Public HTTP:** Karma GAP project API (CIDS records, milestones); public RPC/explorer reads for badge/squad/TVL rows. Best effort with curl; on failure leave the row untouched.
- **PostHog rows** (activation funnel, MAU): this environment has NO PostHog key by design. Do not guess. If the latest growth-pulse status update on the green-goods side carries the numbers, relay them with source noted as `via growth-pulse {date}`; otherwise leave the row untouched.

Rules: never invent a value. A refreshed row gets today's As-of. An unreadable row keeps its old As-of — that staleness is signal, not failure.

## Phase 3 — Write registers

Apply refreshed rows to each `Indicator Register` document. Change cell values only; keep the table structure and any narrative-only notes intact.

## Phase 4 — Status updates (one per initiative)

For each **Active** outcome initiative (Planned ones only when they carry a drift flag), post or refresh ONE status update:

- 2–4 sentences, human tone, what actually moved.
- Indicator readout: the register's rows inline as `Indicator — Current (As-of) vs Target`.
- Drift flags, one line each, only when true:
  - Card `Target:` line ≠ initiative target-date field.
  - `Current roadmap projects` naming a completed, canceled, or nonexistent project.
  - Register rows with As-of older than 30 days.
  - Register document updatedAt older than the initiative description's updatedAt (register left behind).
  - No `Strategy — {current quarter}` document exists on the Guild Operating System shelf (the quarterly review has not happened), or `theory-of-change.md` in the .github clone is untouched for more than 380 days via `git log -1`. These flags go in the Discord digest's Needs-you block, not on any initiative.
- Health: carry the initiative's current health forward (default `onTrack` if unset); if flags warrant a change, SAY SO in the text — the steward changes health, not the pulse.
- End with the signature line: `— scorecard-pulse {YYYY-MM}` (the idempotency key).

## Phase 5 — Discord digest (house style)

ONE message to #lead-council:

```
POST https://discord.com/api/v10/channels/${DISCORD_LEAD_COUNCIL_CHANNEL_ID}/messages
Authorization: Bot ${DISCORD_BOT_TOKEN}
```

Channel guard: post ONLY to `DISCORD_LEAD_COUNCIL_CHANNEL_ID`. There is NO Discord MCP — use the REST recipe above; if the var is missing, skip Discord and record the skip in the closing line. Never silently degrade, never post to any other channel id.

Format (guild house style): lead with **🔴 Needs you** (drift requiring a steward decision), then **Watch**, then per-initiative bullets ONLY for outcomes that moved — fold metrics into the initiative line; omit empty sections; one message. Close with `Full readouts →` linking the Linear initiatives view.

## Phase 6 — Verification surface

The Discord digest's final line records: `initiatives updated N · register rows refreshed M`. The digest message id (or the skip reason recorded in the per-initiative updates' closing lines) is the run's verification surface; same-month re-runs refresh the per-initiative updates in place.

## Guardrails

- Fail closed everywhere. A quiet month posts a short "quiet month" digest — never fabricated movement.
- Every factual claim must trace to something read THIS run (a Linear id, URL, or explorer link). No remembered numbers from prior months.
- One Discord message max per run. One status update per initiative per month.
- This spec is canonical; the trigger is a thin wrapper that re-reads `origin/main:routines/claude/scorecard-pulse.md` each run.
