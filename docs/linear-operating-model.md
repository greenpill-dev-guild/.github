# Linear Operating Model

> How the Greenpill Dev Guild separates project management, execution, evidence, and discussion.

Linear is the guild's project-management source of truth. GitHub remains the public execution surface for code, issues, pull requests, and RFCs. Drive holds memos, evidence, grant drafts, meeting notes, and partner materials. Discord, Telegram, and calls are discussion and pulse channels.

## Source-of-truth split

| Surface | Owns | Does not own |
| --- | --- | --- |
| **Linear** | Roadmap, accepted work, customer and partner needs, funding lifecycle, research tasks, ownership, status | Code review, public bug reports, raw discussion |
| **GitHub** | Public issues, PRs, RFCs, implementation references, repository defaults | Durable project-management backlog |
| **Drive** | Memos, evidence bundles, grant drafts, partner docs, meeting notes | Work status or ownership |
| **Discord / Telegram / calls** | Discussion, triage, community pulse, lightweight coordination | Canonical commitments |

If a discussion creates real work, move the commitment into Linear or GitHub depending on the type of work.

## Linear teams

- **Product** — accepted product, protocol, funding, delivery, QA, and maintenance work.
- **Research** — accepted research tasks and partner/data investigations before implementation is committed.

Raw signal should start as Customer Needs or discussion. Linear Issues are for accepted work with a clear next step.

## Linear labels

Use these label families for Linear Issues:

- `protocol:*` — project or protocol surface, such as `protocol:green-goods`, `protocol:coop`, `protocol:network`, `protocol:cookie-jar`, `protocol:pgsp`, `protocol:greenwill`, or `protocol:tas-hub`.
- `package:*` — code package surface when useful, such as `package:client`, `package:admin`, `package:contracts`, `package:indexer`, or `package:agent`.
- `activity:*` — work mode, such as `activity:build`, `activity:research`, `activity:design`, `activity:qa`, or `activity:maintenance`.
- `task:*` — user-task semantics, such as `task:funding-pathway`, `task:evidence`, `task:access-participation`, `task:data-input`, or `task:local-onboarding`.
- `funding:*` — grant/funding lifecycle: `funding:prospect`, `funding:drafting`, `funding:submitted`, `funding:active-award`.
- `source:*` — originating signal, such as `source:github`, `source:discord`, `source:telegram`, `source:drive`, or `source:plans`.
- `agent:*` — authored or maintained by a routine or agent, such as `agent:claude`, `agent:codex`, or `agent:copilot`.

Do not recreate retired GitHub-era label families in Linear. In particular, avoid `area:*`, `work:*`, `migration:*`, `automation:*`, `health:*`, `grant:*`, and `source:linear`.

## Funding lifecycle

Funding lifecycle is represented by Linear labels and saved views, not by GitHub Issues or a standing roadmap project.

- Prospects, drafts, and submissions live as Linear Product Issues labeled with the current `funding:*` state.
- Saved views over `funding:*` labels are the pipeline view.
- Awarded grants receive `funding:active-award` and graduate into a bounded award or delivery project when there is delivery, reporting, compliance, or funder follow-through to manage.
- Public GitHub issues are used only when there is open execution work in a repo, and they should link back to the relevant Linear context when appropriate.

## Research acceptance bar

Research traffic starts as raw signal in Discord, Drive, or partner notes. It becomes a Linear Research Issue only when it is accepted enough to spend research time on it.

Create a Research Issue when all of these are true:

- The surface or question is specific.
- The next action is more concrete than "investigate this."
- There is medium or higher confidence from repeated signal, partner need, or contributor convergence.
- The work is small or medium enough to track without becoming open-ended R&D.

Keep speculative ideas in Discord or Drive memos until they cross this bar.

## GitHub boundaries

Use GitHub for:

- Bugs, stories, design proposals, and implementation references in the relevant project repo.
- RFCs that affect more than one guild project, shared standards, governance, vocabulary, or partner commitments.
- Pull requests, review, release notes, and code history.

Do not use GitHub as the durable funding pipeline, research backlog, or partner-needs tracker.
