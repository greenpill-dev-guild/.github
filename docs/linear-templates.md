# Linear Templates

> Canonical body templates for Greenpill Dev Guild Linear records.

Linear UI templates may exist, but Codex and other connector-based agents cannot reliably list or apply them. Treat this document as the durable source for template names, routing rules, and body shapes. If a matching Linear UI template exists, use it; otherwise copy the relevant body below.

## Routing Rules

- Customer Needs are raw customer, partner, funder, garden, cohort, or internal-ops signal. They are not commitments to build.
- Linear Issues are accepted units of work with a clear next action. Product issues track accepted delivery, QA, maintenance, funding, and protocol work. Research issues track accepted research tasks.
- Grouped child labels are exclusive in Linear. Choose the primary child label for each family, such as one `activity:*`, one `protocol:*`, and one `package:*` where applicable. Set an **estimate** on payable scoped briefs (replaces `band:*`).
- Projects are bounded containers made from multiple related stories, issues, or research tasks. Do not create a project for a single loose idea unless it is a deliberate scoping project.
- Initiatives are outcome arcs. They group projects around a durable strategic outcome, not around a repo, inbox, or imported board.
- Do not route new work into completed, canceled, staging, or retired projects such as `Green Goods`, `Coop`, `Network Website`, `Cookie Jar`, or `Story Board`.

## Linear Initiative - Outcome Arc

Use for durable outcome-level arcs that may contain multiple projects.

```markdown
## Lean Outcome Card

Steward: {owner name or open}
Cadence: {weekly light review | biweekly review | monthly review}
Target: {YYYY-MM-DD or none}

Outcome: {one sentence describing the desired real-world or product outcome}

Success signals:

* {signal 1}
* {signal 2}
* {signal 3}

Current project routing:

* {project name}: {why it belongs here}

Customer / partner signal:

* {customer or cohort}: {need summary}

Scope guard:

{what should not be attached to this initiative unless it is explicitly accepted}
```

## Linear Project - Lean Outcome

Use for a bounded project that owns a cluster of related issues or stories.

```markdown
## Lean Project Card

Owner: {owner name or open}
Initiative: {initiative name}
Target: {YYYY-MM-DD or none}

Outcome: {one sentence describing the bounded project outcome}

Why now:

{short reason this project is worth active roadmap attention}

Scope:

* {in-scope item 1}
* {in-scope item 2}
* {in-scope item 3}

Out of scope:

* {out-of-scope item 1}
* {out-of-scope item 2}

Issue model:

Multiple accepted stories, research tasks, QA tasks, or delivery tasks make up this project. Raw signal should stay in Customer Needs until accepted as work.

Done means:

* {acceptance signal 1}
* {acceptance signal 2}
* {validation or handoff signal}
```

## Linear Project Scoping Issue

Use when a project is real enough to keep visible but does not yet have scoped issues.

Title: `scope: {Project Name}`

Labels: primary relevant `protocol:*` and `activity:*`. Add `funding:*` only for funding lifecycle work.

```markdown
## Project Scoping Issue

Project: {project name}
Initiative: {initiative name or none yet}

## Why this project exists

{one paragraph explaining the customer, partner, funding, product, or research reason this project should stay visible}

## Decision needed

{what the team needs to decide before this becomes executable work}

## Candidate stories / issues

* {candidate story or issue 1}
* {candidate story or issue 2}
* {candidate story or issue 3}

## Customer / signal source

{Customer Need, Drive doc, GitHub issue, partner note, grant scope, or `.plans` source}

## Next action

{one concrete next step, owner, and expected output}

## Scope guard

If no accepted stories, issues, or customer signals are identified after this scoping pass, close or archive the project instead of leaving it as a placeholder.
```

## Linear Customer Need - Signal Intake

Use for customer, partner, funder, garden, cohort, squad, or internal-ops signal before it becomes accepted work.

```markdown
Source: {Discord, Telegram, Drive, partner call, funder conversation, garden check-in, GitHub, PostHog, or .plans}
Customer type: {garden | cohort | funder | protocol partner | data partner | squad | internal ops}
User-task categories: {Evidence, Evaluator/review, Funding pathway, Local onboarding/education, Access/participation, Data input, Reputation/identity}
Need statement: {one sentence from the customer's perspective}
Evidence/context: {brief context, with links only when safe}
Routing recommendation: {Customer Need -> project/issue, or keep unprojected until accepted}
Privacy note: {what must not be exposed in public issue text}
Disposition: {canonical active signal | superseded duplicate retained for history | parked until more evidence}
```

## Linear Research Issue - Accepted Task

Use only after the research acceptance bar is met.

Title: `Research: {short action title}`

Labels: `activity:research` and primary relevant `protocol:*`. Add `agent:routine` for routine-authored issues.

```markdown
## Accepted Research Task

Research source: {#research week of YYYY-MM-DD, partner conversation, Drive memo, or steward request}

## Theme

{theme name}

## Original sources

* {source link or safe source description}
* {source link or safe source description}

## Accepted action

{specific research action with a knowable output}

## Project / scope

{protocol, project, or guild-wide scope}

## Owner

{name, role, or open}

## Confidence

{high | medium | low} - {brief rationale}

## Status

Accepted - research time is committed to investigating this. Graduates into a bounded delivery project only if the investigation produces work the team commits to ship.
```

## Linear Scoped Brief - Payable Deliverable

Use when a piece of work is scoped for **payment** (any discipline). This is the deliverable shape behind the [compensation playbook](../routines/scoped-work-compensation.md). The *Accepted Research Task* above is the lighter acceptance-bar intake; a paid **Stage-0 scoping** pass turns an accepted task into this payable brief.

Title: `{short deliverable title}`

Labels: one `activity:*` (discipline) and primary relevant `protocol:*`. Set an **estimate** (Scout ~ 1 / Brief ~ 2 / Deep ~ 3), a due date, and an assignee.

```markdown
## Output

{the one concrete artifact this brief produces}

## Acceptance criteria

* {3–6 checkable bullets — what "done + accepted" means}

## Boundary

{what is explicitly out of scope}

## Decision / exit

Done when {condition}, reviewed by {steward / designated evaluator}. Feeds: {the decision this unblocks}.
```

## Linear Funding Issue - Grant Lifecycle

Use for funding opportunities tracked through saved views over `funding:*` labels.

Title: `Grant: {Program Name}`

Project: leave unprojected unless a bounded award or delivery project already exists and the issue is `funding:active-award`.

Labels: one current `funding:*` label, `activity:research`, primary relevant `protocol:*`, and `agent:routine` when routine-authored.

```markdown
## Opportunity

* **Program**: {name}
* **URL**: {url}
* **Deadline**: {date or rolling}
* **Amount**: {range}
* **Source**: {Discord message, Drive doc, Calendar event, Miro board, or web research query}

## Fit

* **Primary project(s)**: {project list}
* **Secondary project(s)**: {project list or none}
* **Alignment summary**: {short rationale}
* **Distinct angle**: {the pitch}

## Evidence

* **Existing proof points**: {links or bullets}
* **Evidence gaps**: {items a human needs to confirm}

## Draft status

* **Drive draft**: {URL or "not started"}
* **Current lifecycle**: {prospect | drafting | submitted | active-award}

## Human decision needed

{submit / draft / monitor / dismiss recommendation}
```
