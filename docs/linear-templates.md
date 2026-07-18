# Linear Templates

> Canonical body templates for Greenpill Dev Guild Linear records. Written to read like a teammate wrote them, not a form.

Linear is the single home for accepted work. GitHub holds code, PRs, review, and RFC/ADR markdown. Pick a template by **what you are making**, not by discipline. The `activity:*` label still rides along on the issue (it is how panels and the stipend ledger read the discipline), but it does not pick the template.

Linear UI templates may exist, but connector-based agents cannot reliably list or apply them. Treat this document as the durable source for template names and body shapes. If a matching Linear UI template exists, use it; otherwise copy the relevant body below.

## Two shapes, and when to use each

- **Most work is one issue.** A single deliverable, a bug, a grant: one issue, done.
- **Use a parent plus children only when the work fans into two or more separate outputs that share context** (a media set, a feature with several lanes, a Deep research piece that bundles a few artifacts). The parent is the Brief; the children are the pieces. Never force this on single-output work.

## Headers are friendly, the fields underneath are not

The friendly headers map to the payable-brief fields so the compensation flow can still find them:

- **"What are we making?"** is the Output.
- **"Out of scope"** is the Boundary.
- **"Done when"** is the Acceptance criteria plus the Decision/exit.

Acceptance is agreed up front and is what makes work claimable. On anything payable, set an **estimate** (exponential scale; 1/2/4/8 in live use, 16+ for a major integration), a `protocol:*`, an `activity:*`, a due date, and an assignee. A Brief with no estimate is accepted work still being scoped; add the estimate when it becomes payable. Pick the **team** by who owns acceptance: delivery on Product, investigation on Research, community work on Community, funding on Growth, campaigns and creative on Marketing (see the [team charters](./teams/README.md)).

## Routing, in one line

Raw signal becomes a **Customer Need**. Accepted work becomes an **issue**. A visible-but-unscoped project gets a **Scope** issue. A cluster of issues becomes a **Project**. An outcome arc over projects is an **Initiative**. Ongoing coverage (support, maintenance) lives as a **Document**, not an issue. Do not route new work into completed, canceled, or retired projects.

---

## Brief

The default for a scoped piece of work. Stands alone, or becomes the parent when the work splits into pieces.

Title: the deliverable in a few words. Team: whichever team owns acceptance. Labels: one `activity:*`, one `protocol:*`, estimate (when payable), due, assignee.

```markdown
## What are we making?
One or two plain sentences: the thing this produces and why it matters now.

## Why this matters
Audience:
Purpose:

## Scope
In scope:
-
Out of scope:
-

## Shared context
Links that apply to the whole piece: docs, product surface, protocol source, prior work.

## Done when
- 3 to 6 checkable signs it is finished and accepted (agreed up front).
- Reviewed by {steward or evaluator}.
- Feeds: {the decision or work this unblocks}.

## Child issues (only if it fans out)
One child per separate output. Leave this out for single-output work.
-

## Payment classification (payable briefs, when the terms need to be explicit)
Classification: stipend-claimable | volunteer | grant-deliverable
Allocation: optional reference amount or points note
Envelope: the funding source this draws from
Guardrails: caps, splits across contributors, exclusions
```

The payment-classification section is optional: an accepted, assigned, estimated brief is stipend-claimable by default (see the [compensation playbook](../routines/scoped-work-compensation.md)). Add the block when the split, envelope, or expectation should be explicit up front — the shape standardizes what briefs like COM-10, MAR-1, and MAR-15 already do.

## Artifact

One concrete output under a Brief: a graphic, a short video, a page, a component, a research sub-memo. Use only as a child of a Brief.

Title: the single output. Labels: inherit the parent's `protocol:*`; an `activity:*` for the work mode.

```markdown
## What are we making?
One artifact, in a sentence.

## Purpose
Audience:
Core message:

## Where it will be used
Docs / community / social / deck / other:

## Key references
Only what this artifact needs.
Parent brief:
Docs / source:
Product surface:
Design tool / Figma:
Screenshots / recordings:

## Direction
What it should show.
- For a visual: main sections, key labels, things to avoid.
- For a video: start state, key steps, end state, things to avoid.

## Deliverables
Editable source:
Final export:
Alt text / captions:
Storage link:

## Done when
- It clearly lands the core message.
- It matches the parent scope and the source material.
- The placement is clear and any product, docs, or technical notes are handled.
- Final files are attached or linked, and linked back on the parent.
```

## Feature / Polish

Product feature development or a polish push. Small ones stand alone; larger ones are a parent with task or lane children. Replaces the old `.plans` hub stub.

Title: the feature or polish in a few words. Team: Product. Labels: `activity:build` (or `activity:maintenance` for polish), `package:*`, `protocol:*`, estimate.

```markdown
## What are we building?
One or two sentences: the change and the user or system value.

## Why now
Short reason this is worth active attention.

## Scope
In scope:
-
Out of scope:
-

## Source
Plan or context: .plans/<path>/ (if any), the doc, the customer need, or the bug it came from.

## Done when
- The checkable signs it is shipped and accepted.
- Reviewed by {steward or evaluator}.

## Tasks / lanes (only if it fans out)
Add these when implementation starts; keep this issue as the hub until then.
-
```

## Bug

A defect from QA, telemetry, or a report.

Title: the symptom in a few words. Team: Product. Labels: `activity:qa`, `package:*`, `protocol:*`.

```markdown
## What happened
Plain terms: who saw it, where, and when. Steps to reproduce if known.

## Where
The surface and package it touches.

## Likely cause or first check
Best current guess at the fix, or what to look at first.

## Severity
P0 to P3 (blocker / major / minor / cosmetic), and a one-line why.

## Source and evidence
Where it came from (sync, Sentry, a report) and any telemetry. Say if it is unverified.

## Done when
- The fix is shipped and the original report is confirmed resolved, or it is reclassified with a reason.
```

## Grant

A funding opportunity, tracked through `funding:*` labels and saved views.

Title: `Grant: {Program}`. Team: Growth (every `funding:*` state lives there). Labels: one `funding:*`, `protocol:*`, and `agent:routine` when routine-authored. When awarded, the issue stays on Growth for reporting and follow-through; file the funded delivery on Product and link it.

```markdown
## Opportunity
Program:
URL:
Deadline:
Amount:
Source:

## Fit
Primary project(s):
Secondary:
Why it is a match:

## Evidence
Proof points we have:
Gaps a human must confirm:

## Status
Lifecycle: prospect / drafting / submitted / active-award (mirror it with the funding:* label).
Drive draft: URL or not started.

## Decision needed
Submit / draft / monitor / dismiss, and what to confirm before we put real time in.
```

## Customer Need

Raw signal from a customer, partner, funder, garden, cohort, or internal ops, before it is accepted as work.

```markdown
Source: {Discord, Telegram, Drive, call, garden check-in, GitHub, PostHog, or .plans}
Who: {garden | cohort | funder | partner | squad | internal ops}
Need: one sentence from their point of view.
Context: brief, with safe links only.
Routing: keep as a need, or which issue or project it becomes when accepted.
Privacy: anything that must not appear in public issue text.
Disposition: active signal | superseded duplicate | parked for more evidence.
```

## Scope (project-scoping issue)

Keep a project visible before it has scoped issues.

Title: `scope: {Project}`. Labels: primary `protocol:*` and `activity:*`.

```markdown
## Why this project exists
The customer, partner, funding, product, or research reason it should stay visible.

## Decision needed
What the team must decide before this becomes executable work.

## Candidate issues
-

## Signal source
Customer Need, Drive doc, GitHub, partner note, grant scope, or .plans.

## Next action
One concrete step, an owner, and the expected output.

## Scope guard
If no accepted issues or signals come out of this pass, close or archive the project rather than leave a placeholder.
```

## Project (container card)

A bounded project that owns a cluster of issues.

```markdown
Owner:
Initiative:
Target: {YYYY-MM-DD or none}

## Outcome
One sentence: the bounded outcome.

## Why now
Short reason it is worth active roadmap attention.

## Scope
In scope:
-
Out of scope:
-

## Done means
- Acceptance and validation or handoff signals.
```

## Initiative (outcome arc)

A durable outcome that groups several projects.

```markdown
Steward:
Cadence: {weekly | biweekly | monthly} review
Target: {YYYY-MM-DD or none}

## Outcome
One sentence: the real-world or product outcome.

## Success signals
-

## Project routing
- {project}: why it belongs here.

## Scope guard
What should not be attached unless explicitly accepted.
```

## Continuous role (a Document, not an issue)

Ongoing coverage that is not a single deliverable: community support, ongoing maintenance, funding tracking. The Document defines the arrangement; the claimable record is **one coverage issue per month** (what was covered, moved to Done and accepted), claimed within the monthly stipend cap per the [compensation playbook](../routines/scoped-work-compensation.md). Do not open per-task issues beyond the monthly coverage issue.

```markdown
Role:
Owner:
Cadence / coverage: what is covered each month.
Coverage issue: link each month's accepted coverage issue here.
Review: how the role is reviewed and renewed.
```
