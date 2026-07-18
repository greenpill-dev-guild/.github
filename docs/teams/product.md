# Product — Team Charter

> Ship and maintain the guild's live products.

**Key:** `PRD` · **Cycles:** 2-week · **Panel:** afo, gferreira525, coi

## Purpose

<<<<<<< HEAD
Linear team description (paste verbatim — the settings field caps at ~255 characters, and this version fits):

> Accepted, shippable work: features, delivery, QA, and maintenance on live products. Every issue has a clear next action and an owner, human or agent. Research starts on Research, funding on Growth, raw signal as a Customer Need.
=======
Use this text verbatim as the Linear team description:

> Accepted, shippable work: product and protocol features, delivery, QA, and maintenance on live products. Every issue has a clear next action and an owner, human or agent. Research starts on Research, funding lives on Growth, and raw signal starts as a Customer Need.
>>>>>>> origin/main

(The pre-2026-07 description also claimed "funding on live products"; that clause moved to Growth with the funding pipeline.)

## What belongs here

- Features, bugs, QA, polish, and maintenance on Green Goods and the Greenpill Network website (for example the "Q3 July — Commitment Pooling" cycle work).
- Product and UX design (`activity:design` on this team means interface and experience design).
- Delivery work unlocked by a grant award: filed here, linked back to the award issue on Growth.
- Customer Needs for product surfaces, triaged by the bug-intake and qa-triage routines.

## What doesn't

- Investigations and methodology work → Research.
- Grant lifecycle, partnerships, funder reporting → Growth.
- Campaigns, content, brand and visual assets → Marketing.
- Cohort building, onboarding, support coverage → Community.

## Workflow states

Triage · Backlog · Todo · In Progress · In Review · Done · Canceled · Duplicate

- **Triage** is the intake gate: routine-filed issues (bug-intake, qa-triage-pulse) and external reports land here before acceptance.
- The former QA and Ready states were retired in the 2026-07 simplification. QA proof now lives in **In Review** plus the acceptance rule: merge evidence alone is not Done, close only when acceptance criteria are verified on the intended surface.
- No state changes needed; this set matches the live Linear configuration.

## Cycles

2-week cycles, named for the cycle's focus. At every boundary each unfinished issue is explicitly rolled (with its dependents, as one unit) or moved to Backlog; nothing silently drops out.

## Evaluator panel

afo, gferreira525, coi. Panel sign-off moves a scoped brief Backlog → Todo (3-day async SLA; afo's ack counts). Roster is confirmed in the Evaluator Panels Linear Document.

## Templates

Templates live **globally at the workspace level** (steward decision 2026-07-18), not per team — create and apply them from [linear-templates.md](../linear-templates.md). This team's everyday shapes:

- **Feature / Polish** — default for build work (`activity:build` or `activity:maintenance`, `package:*`, `protocol:*`, estimate).
- **Bug** — defects from QA, telemetry, or reports (`activity:qa`, `package:*`, `protocol:*`).
- **Brief** — anything scoped that is neither a feature nor a bug.

## Surfaces

- **Discord:** `#product` (routine acks and summaries), `#engineering` (health-watch red alerts), `#bug-report` (raw reports), `#growth` (Green Goods growth pulse).
- **Routines:** bug-intake, qa-triage-pulse, health-watch, growth-pulse, pr-review (green-goods scoped); delivery-hygiene and weekly synthesis (guild level).
- **Common labels:** `protocol:*`, `package:*`, `activity:build` / `qa` / `maintenance` / `design`.
