# Linear Operating Model

> How the Greenpill Dev Guild separates project management, execution, evidence, and discussion.

Linear is the guild's project-management source of truth. GitHub remains the public execution surface for code, issues, pull requests, and RFCs. Drive holds memos, evidence, grant drafts, meeting notes, and partner materials. Discord, Telegram, and calls are discussion and pulse channels.

For local development startup, use the [Linear-aware dev day launcher](./linear-aware-dev-day-launcher.md): the active agent or script reads Linear through approved access, `dev-surfaces` resolves the local launch plan, and the human confirms before anything starts.

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

Use [Linear templates](./linear-templates.md) as the canonical body reference for connector-created Linear records. Linear UI templates can still be used manually when available, but connector-based agents should follow the documented template names and body shapes.

## Routing model

- Customer Needs are raw signal. They preserve customer, partner, funder, garden, cohort, squad, or internal-ops needs before the guild commits to delivery or research.
- Stories and issues are accepted units of work with a clear next action.
- Projects are bounded containers made from multiple related stories, issues, or research tasks.
- Initiatives are outcome arcs that group projects around a durable strategic outcome.

## Linear labels

Use these label families for Linear Issues:

- `protocol:*` — project or protocol surface, such as `protocol:green-goods`, `protocol:coop`, `protocol:network`, `protocol:cookie-jar`, `protocol:pgsp`, `protocol:greenwill`, or `protocol:tas-hub`.
- `package:*` — code surface, keyed to the **repo** the code lives in and orthogonal to `protocol:*` (the product — one package can serve several products, e.g. GreenWill contracts live in green-goods). green-goods: `package:client`, `package:admin`, `package:agent`, `package:indexer`; coop: `package:app`, `package:api`, `package:extension`; shared by both repos: `package:contracts`, `package:shared`, `package:docs`. Code-touching work only — omit on research / funding / ops; single-surface repos (e.g. `network`) omit it entirely.
- `activity:*` — work mode, such as `activity:build`, `activity:research`, `activity:design`, `activity:qa`, `activity:maintenance`, `activity:marketing`, `activity:community`, or `activity:growth`.
- `funding:*` — grant/funding lifecycle: `funding:prospect`, `funding:drafting`, `funding:submitted`, `funding:active-award`.
- `source:*` — originating signal, such as `source:github`, `source:discord`, `source:telegram`, `source:drive`, or `source:plans`.
- `agent:*` — authored or maintained by a routine or agent, such as `agent:claude`, `agent:codex`, or `agent:copilot`.
- **Estimate (Linear field)** — sizing for a paid scoped brief on the exponential scale (Scout ~ 1, Brief ~ 4, Deep ~ 16); replaces the retired `band:*` labels. See the [scoped-work compensation playbook](../routines/scoped-work-compensation.md).

Linear enforces exclusive child labels within grouped families. Pick the primary child label for each family rather than applying several `activity:*`, `protocol:*`, or `package:*` labels to the same issue.

Do not recreate retired GitHub-era label families in Linear. In particular, avoid `area:*`, `work:*`, `task:*`, `band:*`, `migration:*`, `automation:*`, `health:*`, `grant:*`, and `source:linear`.

## Scoped work, sizing & accountability

Paid work is scoped, sized, and paid per the [How the Dev Guild Pays for Scoped Work](../routines/scoped-work-compensation.md) playbook: a **scoped brief** (Output · Acceptance criteria · Boundary · Decision/exit) carries an **estimate** and an `activity:*` discipline label, and "Done" (accepted) is the payment event. Use the [Scope brief issue template](https://github.com/greenpill-dev-guild/.github/issues/new?template=scope.yml) or the [scoped-brief body](./linear-templates.md#linear-scoped-brief---payable-deliverable). Dated, owned briefs are chased by the `research-accountability-pulse` routine under the **Research Accountability** rule (scope → due date → pulse → escalation), kept as a Linear Document in the Research Operations project. Continuous roles (e.g. community support) are a monthly arrangement rather than per-brief.

**Scope before assign, sign off before start:**

- **Async scoping.** Briefs are prepared in Linear *before* the call that commits them, not invented live. Raw ideas stay in Discord / Drive until they cross the brief bar.
- **Estimate means scoped.** Setting a Linear **estimate** is the signal that an issue is a scoped brief (and, on Product, a paid one). No estimate means it is not yet scoped.
- **Panel sign-off is the gate.** Anyone may scope a brief; the matching **discipline evaluator panel** (see [GOVERNANCE.md](../GOVERNANCE.md#decision-making)) signs it off to move it **Backlog → Todo** (and, if funded, payable). Async SLA: **3 days**; afo's ack counts on any panel.
- **Mandatory peer review.** Every scoped brief gets at least one peer review before it is accepted as done. The `scope-review-pulse` routine routes waiting briefs to their panel daily; the `research-accountability-pulse` chases dated / owned work for slippage.

## Cycle cadence and rollover

- **Product** runs short (roughly weekly) cycles for polish, bugs, QA, and delivery. **Research** runs long, multi-week cycles and focuses on **one theme per cycle** rather than many parallel threads — research is not judged on Product's weekly rhythm.
- **Cycle rollover.** At a cycle boundary, every unfinished issue is **explicitly** either rolled to the next cycle (with its dependents, as one unit) or moved to Backlog. Issues are never left to silently drop out of a closing cycle. Closing a cycle strong means each issue in it is closed-with-proof, rolled, or backlogged on purpose.

## Cross-team placement

Place an issue on the team that owns its acceptance, and keep dependent work together:

- **Funding lifecycle** — awarded grants (`funding:active-award`) live on **Product** once there is delivery; all earlier states (prospect, drafting, submitted) live on **Research** in Grant Scouting.
- **Research-led architecture briefs** (e.g. the Impact Framework v0.1 set) live on the team that signs them off. Moving a scoped brief across teams renumbers it but preserves its labels, project, estimate, and history, so move deliberately rather than reflexively.
- **Keep a gate and its dependents in one cycle.** A QA gate and the issues it blocks, or a foundation brief and the briefs that depend on it, move together so a dependency chain is never split across cycles.

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
