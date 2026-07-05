# Software Ecology Operating Model

Software ecology is the guild's cross-repo view of how people, agents, validation, local dev surfaces, release posture, and repo truth surfaces fit together.

This is not a backlog. It is an operating map for seeing whether AI-assisted development is amplifying good engineering practice or adding unmanaged activity.

## Source-of-truth split

| Surface | Owns | Does not own |
| --- | --- | --- |
| `dev-surfaces` | Local executable snapshot: `dev ecology --json`, local handoff bundle via `dev ecology --json --handoff`, live dev-surface status, git state, plan counts, validation scripts, and ignored local snapshots | Durable guild policy, hosted routine setup, hosted routine input, Linear status |
| `.github` | Guild-level policy, routine source prompts, the pulse registry metadata below, source-of-truth split, and shared language | Local process ownership or repo runtime launch details |
| Project `.plans` | Execution truth for active feature work and lane state | Cross-repo status, social priority, or release authority |
| Linear | Roadmap/status tracking, initiatives, accepted work, and status updates | Repo implementation truth or code review |
| Drive | Weekly memos and evidence archive | Work ownership or implementation state |
| Discord | Human-readable pulse and coordination | Canonical commitments |

## V1 repo set

The ecology index covers the two guild-org repos:

| Repo | Tier | Role | Source-truth globs |
| --- | --- | --- | --- |
| Green Goods | Tier 1 heavy agentic product | Reference implementation for heavy `.plans`, shared contracts, design/docs drift checks, browser proof, and release complexity | `.plans/active/*/status.json`, `.plans/backlog/*/status.json`, `AGENTS.md`, `CLAUDE.md`, `package.json` |
| Greenpill Network | Tier 1 heavy agentic product | Reference implementation for public/private route contracts and workspace/auth decision discipline | `.plans/active/*/status.json`, `.plans/backlog/*/status.json`, `AGENTS.md`, `CLAUDE.md`, `package.json` |

Portfolio, WEFA, and TAS-Hub left the guild V1 set in 2026-W24 (personal or guild-adjacent repos owned outside the guild org); they remain in the local dev-surfaces registry for local workflows only. Impact Reef and other dormant repos stay out of V1 until they become active work again.

### Pulse registry metadata

Curated judgment fields consumed by the weekly pulse. A local twin lives in the dev-surfaces registry for local workflows; the pulse reads only this section.

**Green Goods**

- API/privacy boundaries: Shared hooks, domain types, and public contracts live in `packages/shared`. Agent and webhook behavior lives in `packages/agent`. Contract deployment artifacts remain the address source of truth.
- Release/rollback: Use repo-specific build, docs, design, package, browser-proof, and deploy scripts. Onchain or deploy rollback must be treated as a human-reviewed operation.
- Likely bottleneck: Source-structure debt, dirty-tree coordination, and choosing the right validation depth before adding more concurrent agent work.

**Greenpill Network**

- API/privacy boundaries: Public website remains static and public-safe. Private runtime, database, and intake concerns stay behind `packages/agent`. Public agent routes need exported constants, shared contracts, public-safe normalization, and tests.
- Release/rollback: Public site currently builds from `packages/website`; agent deploys use `packages/agent/fly.toml`. Workspace/auth runtime remains decision-packed before implementation.
- Likely bottleneck: Workspace/auth boundary decisions and integration proof across website snapshot, agent route, shared contract, Directus, and Postgres.

## Signal definitions

`dev ecology --json` is the local machine-readable inspection snapshot; `dev ecology --json --handoff` bundles it with a Markdown sibling for human review. Both are local conveniences: the hosted routine computes its own snapshot from cloud clones and does not consume these files. Treat them as point-in-time local snapshots, not as replacements for project repo truth.

The local snapshot records:

- Git branch, upstream, ahead/behind, dirty count, and change-type counts.
- Plan-hub `status.json` count and canonical lane status totals, when `.plans` exists. Raw lane vocabularies remain in JSON for audit.
- Validation, browser-proof, release, deploy, and agentic scripts from `package.json`.
- Workbench dev-surface status for repos registered in `dev-surfaces`.
- Curated risk tier, source-truth surfaces, API/privacy boundaries, release/rollback notes, and likely bottleneck.

The hosted pulse computes a narrower, clone-derivable subset: plan-lane counts, guidance presence, root script inventory, last-commit recency, and main-develop drift. Working-tree state and dev-surface runtime are local-only signals and never appear in the pulse.

Healthy ecology signals:

- Plan state, local scripts, and repo guidance agree.
- Dirty trees are understood and bounded.
- Public/internal API changes have explicit contracts and focused tests.
- Browser-proof and integration-proof lanes exist for user-facing changes.
- Human judgment points are visible before high-risk changes.

At-risk ecology signals:

- Many blocked or stale lanes without a clear next decision.
- Large dirty trees in high-risk repos.
- Runtime changes without matching proof scripts.
- Internal APIs exposed to agents without contract tests.
- Release or rollback paths documented only in memory or chat.

## Weekly pulse

The `software-ecology-pulse` routine is status-only and self-sufficient: each run computes its ecology snapshot from the fresh cloud clones of the three V1 repos (plan-lane counts, guidance presence, root script inventory, git recency, and main-develop drift where refs allow) plus the pulse registry metadata in this document. No local snapshot generation, upload, or attachment is required, and the routine must not search Drive for one.

Allowed outputs:

- One Linear initiative status update on `Software Ecology & Agentic Workflow Health`.
- One Dev Guild shared Drive memo.
- One private/dev-guild Discord summary.

Forbidden outputs:

- No Linear Issues or Customer Needs.
- No GitHub Issues, pull requests, branches, or repo edits.
- No production deploys.
- No browser sessions.
- No secret reads.
- No heavy validation runs.

If a V1 clone is missing or unreadable, the routine marks health `atRisk`, names the missing repo, and creates no work.

## Reading the dashboard

Use `dev ecology --markdown` for human review and `dev ecology --json` for local machine inspection.

Read the output in this order:

1. Workbench check errors or warnings.
2. Tier 1 repos with dirty trees, ahead/behind drift, or blocked lanes.
3. Repos with no plan state but active implementation risk.
4. API/privacy boundary notes before recommending any agent expansion.
5. Release/rollback notes before increasing automation or deploy cadence.

The correct response to a weak signal is usually a bounded clarification or proof task, not automatic issue creation.
