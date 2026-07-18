# Linear Operating Model

> How the Greenpill Dev Guild separates project management, execution, evidence, and discussion.

Linear is the guild's project-management source of truth. GitHub remains the public execution surface for code, issues, pull requests, and RFCs. Drive holds memos, evidence, grant drafts, meeting notes, and partner materials. Discord, Telegram, and calls are discussion and pulse channels.

For local development startup, use the [Linear-aware dev day launcher](./linear-aware-dev-day-launcher.md): the active agent or script reads Linear through approved access, `dev-surfaces` resolves the local launch plan, and the human confirms before anything starts.

## Source-of-truth split

| Surface | Owns | Does not own |
| --- | --- | --- |
| **Linear** | Roadmap, all accepted work (delivery, QA and bugs, features, research), customer and partner needs, funding lifecycle, ownership, status | Code review, raw external reports before they are triaged |
| **GitHub** | PRs, code review, releases, RFC and ADR markdown, implementation references, repository defaults | The issue tracker or durable project-management backlog |
| **Drive** | Memos, evidence bundles, grant drafts, partner docs, meeting notes | Work status or ownership |
| **Discord / Telegram / calls** | Discussion, triage, community pulse, lightweight coordination | Canonical commitments |

If a discussion creates real work, move the commitment into Linear or GitHub depending on the type of work.

## Linear teams

Five teams, one charter each in [docs/teams/](./teams/README.md). The charter carries the team's purpose, states, cycle stance, panel, and templates; this document owns the rules that cut across teams.

| Team | Key | Owns | Cycles |
| --- | --- | --- | --- |
| [Product](./teams/product.md) | `PRD` | Shippable delivery: features, bugs, QA, maintenance, product/UX design on live products | 2-week |
| [Research](./teams/research.md) | `RESR` | Accepted investigations that produce decision-ready artifacts before build commitment | Long, **one theme per cycle** |
| [Community](./teams/community.md) | `COM` | Cohorts, onboarding, support coverage, gatherings, member coordination | 2-week |
| [Growth](./teams/growth.md) | `GROW` | The entire `funding:*` pipeline, partnerships, BD, funder reporting | None (deadline-driven) |
| [Marketing](./teams/marketing.md) | `MAR` | Campaigns, content, announcements, brand/creative assets | None (brief-driven) |

Raw signal should start as Customer Needs or discussion. Linear Issues are for accepted work with a clear next step.

Use [Linear templates](./linear-templates.md) as the canonical body reference for connector-created Linear records. Linear UI templates can still be used manually when available, but connector-based agents should follow the documented template names and body shapes.

## Team map

| Team | Discord | Routine coverage | Evaluator panel | Signature labels |
| --- | --- | --- | --- | --- |
| Product | `#product`, `#engineering`, `#bug-report`, `#growth` | bug-intake, qa-triage-pulse, health-watch, growth-pulse, pr-review, delivery-hygiene-pulse, weekly synthesis | afo · gferreira525 · coi | `protocol:*`, `package:*`, `activity:build/qa/maintenance/design` |
| Research | `#research` (discussion) | delivery-hygiene-pulse, weekly synthesis (research block) | afo · coi · matt | `activity:research`, `activity:architecture` |
| Community | `#community` | delivery-hygiene-pulse, weekly synthesis | afo · nansel · matt | `activity:community` |
| Growth | `#funding` | guild-grant-scout, delivery-hygiene-pulse (non-funding issues), weekly synthesis | afo · matt | `funding:*`, `activity:capital` |
| Marketing | `#design` (creative review) | delivery-hygiene-pulse, weekly synthesis | afo · nansel · kit | `activity:marketing`, `activity:design` |

Panel rosters are confirmed in the Evaluator Panels Linear Document; the table above is the reference copy.

## Routing model

- Customer Needs are raw signal. They preserve customer, partner, funder, garden, cohort, squad, or internal-ops needs before the guild commits to delivery or research.
- Stories and issues are accepted units of work with a clear next action.
- Projects are bounded containers made from multiple related stories, issues, or research tasks.
- Initiatives are outcome arcs that group projects around a durable strategic outcome.

Routing between teams:

- Funding lifecycle, in every state → **Growth**.
- Campaigns, content, brand/creative → **Marketing**.
- Cohorts, onboarding, support → **Community**.
- Shippable delivery → **Product**.
- Investigation and methodology → **Research**.
- **Tiebreak: the team that owns acceptance owns the issue.** Design splits by kind: product/UX design → Product, brand/creative design → Marketing. Award-funded delivery is filed on Product and linked to the award issue on Growth.

## Linear labels

Use these label families for Linear Issues:

- `protocol:*` — project or protocol surface: `protocol:green-goods`, `protocol:network`, `protocol:coop`, `protocol:pgsp`, or `protocol:greenwill`.
- `package:*` — code surface, keyed to the **repo** the code lives in and orthogonal to `protocol:*` (the product — one package can serve several products, e.g. GreenWill contracts live in green-goods). green-goods: `package:client`, `package:admin`, `package:agent`, `package:indexer`, `package:community`; coop: `package:app`, `package:api`, `package:extension`; shared by both repos: `package:contracts`, `package:shared`, `package:docs`. Code-touching work only — omit on research / funding / ops; single-surface repos (e.g. `network`) omit it entirely.
- `activity:*` — work mode: `activity:build`, `activity:research`, `activity:design`, `activity:architecture`, `activity:qa`, `activity:maintenance`, `activity:marketing`, `activity:community`, `activity:ops`, or `activity:capital`. **`activity:growth` is retired**: Growth is a team (`GROW`), not a work mode; do not recreate the label.
- `funding:*` — grant/funding lifecycle: `funding:prospect`, `funding:drafting`, `funding:submitted`, `funding:active-award`. Lives on the Growth team.
- `source:*` — originating signal, such as `source:github`, `source:discord`, `source:telegram`, `source:drive`, or `source:plans`.
- `agent:*` — authored or maintained by a routine or agent, such as `agent:claude`, `agent:codex`, or `agent:copilot`.
- **Estimate (Linear field)** — sizing signal for a scoped brief on the exponential scale (1/2/4/8 in live use; 16+ for a major integration); replaces the retired `band:*` labels. An estimate is a size, not a price; see the [compensation playbook](../routines/scoped-work-compensation.md).

Linear enforces exclusive child labels within grouped families. Pick the primary child label for each family rather than applying several `activity:*`, `protocol:*`, or `package:*` labels to the same issue.

Do not recreate retired GitHub-era label families in Linear. In particular, avoid `area:*`, `work:*`, `task:*`, `band:*`, `migration:*`, `automation:*`, `health:*`, `grant:*`, and `source:linear`.

## Scoped work, sizing & accountability

Paid work is scoped, sized, and paid per the [compensation playbook](../routines/scoped-work-compensation.md): a **scoped brief** (Output · Acceptance criteria · Boundary · Decision/exit) carries an **estimate** and an `activity:*` discipline label, and "Done" (accepted) is what makes work claimable. Use the [Brief template](./linear-templates.md#brief). Dated, owned briefs on every team are chased for slippage by the `delivery-hygiene-pulse` routine under the **Delivery Accountability** rule (scope → due date → pulse → escalation), kept as a Linear Document. Continuous roles (e.g. community support) are a monthly arrangement rather than per-brief.

**Scope before assign, sign off before start:**

- **Async scoping.** Briefs are prepared in Linear *before* the call that commits them, not invented live. Raw ideas stay in Discord / Drive until they cross the brief bar.
- **Estimate means scoped.** Setting a Linear **estimate** is the signal that an issue is a scoped brief. No estimate means it is not yet scoped.
- **Panel sign-off is the gate.** Anyone may scope a brief; the matching **team evaluator panel** (see the [team charters](./teams/README.md) and [GOVERNANCE.md](../GOVERNANCE.md#decision-making)) signs it off to move it **Backlog → Todo** (and, if funded, claimable). Async SLA: **3 days**; afo's ack counts on any panel.
- **Mandatory peer review.** Every scoped brief gets at least one peer review before it is accepted as done. The `delivery-hygiene-pulse` routine routes waiting briefs to their panel on Mondays and Thursdays and chases dated / owned work for slippage.

## Cycle cadence and rollover

- **Product** and **Community** run 2-week cycles. **Research** runs long, multi-week cycles and focuses on **one theme per cycle** rather than many parallel threads — research is not judged on the two-week rhythm. **Growth** and **Marketing** run no cycles: their work is deadline- and brief-driven, paced by program windows and due dates.
- **Cycle rollover** (cycled teams). At a cycle boundary, every unfinished issue is **explicitly** either rolled to the next cycle (with its dependents, as one unit) or moved to Backlog. Issues are never left to silently drop out of a closing cycle. Closing a cycle strong means each issue in it is closed-with-proof, rolled, or backlogged on purpose.

## Cross-team placement

Place an issue on the team that owns its acceptance, and keep dependent work together:

- **Funding lifecycle** — every `funding:*` state, including `funding:active-award`, lives on **Growth**. The delivery work an award unlocks is filed on **Product** and linked back to the award issue.
- **Projects span teams.** A project is the shared container; its issues still live on their acceptance teams (House of Alignment spans Community, Growth, Research, and Product). Moving an issue across teams renumbers it but preserves labels, project, estimate, and history, so move deliberately rather than reflexively.
- **Research-led architecture briefs** (e.g. the Impact Framework v0.1 set) live on the team that signs them off.
- **Keep a gate and its dependents in one cycle.** A QA gate and the issues it blocks, or a foundation brief and the briefs that depend on it, move together so a dependency chain is never split across cycles.

Scope-review happens before Todo. Backlog and Triage issues that need a scoped brief or evaluator-panel sign-off are surfaced by `delivery-hygiene-pulse`; the routine can nudge the right panel, but it never accepts work or moves issues to Todo. Acceptance remains a human panel decision.

## Agent delegation

A Linear issue delegated to Codex or another coding agent must be self-contained enough that the issue is the prompt and the repo's `AGENTS.md` is the operating manual. Delegate only when the issue names the target repo/branch, behavior change, bounded surface, validation command, and acceptance criteria. If a task points to a `.plans` handoff or status file, link it explicitly and keep orchestration state in the plan/status file, not in the agent's private thread.

`agent:codex` marks an issue as suitable for Codex-style execution; it is not a priority label and does not replace a human reviewer. Agent PRs should target the integration branch named in the issue, stay one concern per PR, include the relevant Linear close/reference, and never self-merge.

## Acceptance and closure

GitHub merge evidence is useful but not sufficient by itself to mark Linear work Done. Close only when the acceptance criteria have been verified on the intended surface. If a PR is merged but the result needs staging proof, human QA, deploy verification, or residual-scope review, keep the issue in In Review and record the missing proof instead of moving it to Done.

## Funding lifecycle

Funding lifecycle is represented by Linear labels and saved views on the **Growth** team, not by GitHub Issues or a standing roadmap project.

- Prospects, drafts, submissions, and active awards live as Growth Issues labeled with the current `funding:*` state.
- Saved views over `funding:*` labels are the pipeline view.
- Awarded grants receive `funding:active-award` and stay on Growth for reporting, compliance, and funder follow-through; the funded delivery is filed on Product and linked.
- Public GitHub issues are used only when there is open execution work in a repo, and they should link back to the relevant Linear context when appropriate.

## Research acceptance bar

Research traffic starts as raw signal in Discord, Drive, or partner notes. It becomes a Linear Research Issue only when it is accepted enough to spend research time on it.

Create a Research Issue when all of these are true:

- The surface or question is specific.
- The next action is more concrete than "investigate this."
- There is medium or higher confidence from repeated signal, partner need, or contributor convergence.
- The work is small or medium enough to track without becoming open-ended R&D.

Research runs one theme per cycle, so accepted research also either fits the active theme or waits for the next cycle. Keep speculative ideas in Discord or Drive memos until they cross this bar.

## GitHub boundaries

Use GitHub for:

- Pull requests, review, release notes, and code history.
- RFCs and ADRs that affect more than one guild project, shared standards, governance, vocabulary, or partner commitments, kept as in-repo markdown proposed via PR.
- Implementation references in the relevant project repo.

Accepted work (bugs, stories, features, research, funding) is tracked as Linear issues, not GitHub issues. External reports may still arrive as blank GitHub issues and are triaged into Linear. Do not use GitHub as the issue tracker, durable funding pipeline, research backlog, or partner-needs tracker.
