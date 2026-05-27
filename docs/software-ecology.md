# Software Ecology Operating Model

Software ecology is the guild's cross-repo view of how people, agents, validation, local dev surfaces, release posture, and repo truth surfaces fit together.

This is not a backlog. It is an operating map for seeing whether AI-assisted development is amplifying good engineering practice or adding unmanaged activity.

## Source-of-truth split

| Surface | Owns | Does not own |
| --- | --- | --- |
| `dev-surfaces` | Local executable snapshot: `dev ecology --json`, Drive-ready handoff bundle via `dev ecology --json --handoff`, live dev-surface status, git state, plan counts, validation scripts, and ignored local snapshots | Durable guild policy, hosted routine setup, Linear status |
| `.github` | Guild-level policy, routine source prompts, source-of-truth split, and shared language | Local process ownership or repo runtime launch details |
| Project `.plans` | Execution truth for active feature work and lane state | Cross-repo status, social priority, or release authority |
| Linear | Roadmap/status tracking, initiatives, accepted work, and status updates | Repo implementation truth or code review |
| Drive | Weekly memos and evidence archive | Work ownership or implementation state |
| Discord | Human-readable pulse and coordination | Canonical commitments |

## V1 repo set

The first ecology index covers:

| Repo | Tier | Role |
| --- | --- | --- |
| Green Goods | Tier 1 heavy agentic product | Reference implementation for heavy `.plans`, shared contracts, design/docs drift checks, browser proof, and release complexity |
| Coop | Tier 1 heavy agentic product | Reference implementation for human attention, agent policy, local-first review, and validation selection |
| Greenpill Network | Tier 1 heavy agentic product | Reference implementation for public/private route contracts and workspace/auth decision discipline |
| WEFA | Tier 1 heavy agentic product | Reference implementation for child-safety, route-local validation, and child-facing browser proof |
| Portfolio | Tier 2 lightweight public site | Lightweight route, contact validation, Storybook, and browser-proof surface |
| TAS-Hub | Tier 2 lightweight public site | Lightweight public Next.js site with token, smoke, and motion/accessibility guardrails |

Impact Reef and other dormant repos stay out of V1 until they become active work again.

## Signal definitions

`dev ecology --json` is the machine-readable inspection snapshot. `dev ecology --json --handoff` is the hosted routine input. Both should be treated as point-in-time local snapshots, not as replacements for project repo truth.

The snapshot records:

- Git branch, upstream, ahead/behind, dirty count, and change-type counts.
- Plan-hub `status.json` count and canonical lane status totals, when `.plans` exists. Raw lane vocabularies remain in JSON for audit.
- Validation, browser-proof, release, deploy, and agentic scripts from `package.json`.
- Workbench dev-surface status for repos registered in `dev-surfaces`.
- Curated risk tier, source-truth surfaces, API/privacy boundaries, release/rollback notes, and likely bottleneck.

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

The `software-ecology-pulse` routine is status-only.

Before enabling or running the hosted routine, produce the weekly handoff locally:

```sh
dev ecology --json --handoff
```

Upload or attach the generated JSON as `Software Ecology Snapshot YYYY-WW`. The Markdown sibling is for human review. This makes the routine deterministic: Claude reads the handoff snapshot and allow-listed guidance surfaces; it does not run local commands, start browsers, or infer local repo state from memory.

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

If the local ecology handoff is missing, incomplete, or stale, the routine must mark health `atRisk`, explain which proof is missing, and avoid creating work.

## Reading the dashboard

Use `dev ecology --markdown` for human review, `dev ecology --json` for machine inspection, and `dev ecology --json --handoff` for the weekly routine input.

Read the output in this order:

1. Workbench check errors or warnings.
2. Tier 1 repos with dirty trees, ahead/behind drift, or blocked lanes.
3. Repos with no plan state but active implementation risk.
4. API/privacy boundary notes before recommending any agent expansion.
5. Release/rollback notes before increasing automation or deploy cadence.

The correct response to a weak signal is usually a bounded clarification or proof task, not automatic issue creation.
