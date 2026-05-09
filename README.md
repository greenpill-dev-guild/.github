# greenpill-dev-guild/.github

> Org defaults, public profile content, and shared contributor guidance for the Greenpill Dev Guild.

This is the org-level `.github` repository for `greenpill-dev-guild`. It has three jobs:

1. Provide the community-health defaults that GitHub can inherit into guild repositories.
2. Host opt-in reusable workflow building blocks for repositories that call them explicitly.
3. Hold shared guild docs that contributors can read or copy, but that do not propagate automatically.

## What propagates automatically

Files at the repo root and in `.github/` can become org defaults for repositories that do not override them locally.

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)
- [`FUNDING.yml`](./FUNDING.yml)
- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`SECURITY.md`](./SECURITY.md)
- [`SUPPORT.md`](./SUPPORT.md)
- [`.github/ISSUE_TEMPLATE/`](./.github/ISSUE_TEMPLATE/)
- [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md)

The org profile is separate:

- [`profile/README.md`](./profile/README.md) renders on the public org page at `github.com/greenpill-dev-guild`

## What is opt-in

These files are reusable from this repo, but each consuming repository must adopt them explicitly:

- [`.github/workflows/labels-sync.yml`](./.github/workflows/labels-sync.yml) — syncs the guild label manifest into a repo that calls it
- [`.github/workflows/claude-pr-review.yml`](./.github/workflows/claude-pr-review.yml) — runs non-blocking Claude PR review for a repo that calls it

## What does not propagate automatically

These directories are shared references for guild contributors, but they must be adopted intentionally:

- [`templates/`](./templates/) — copy-into-repo starters for `README.md`, `AGENTS.md`, `CLAUDE.md`, and Copilot instructions
- [`routines/`](./routines/) — guild-wide playbooks for recurring flows
- [`adr/`](./adr/) — guild-level architectural decision records and template
- [`PARTNERS.md`](./PARTNERS.md) — partner, funder, and chapter interface
- [`docs/linear-operating-model.md`](./docs/linear-operating-model.md) — source-of-truth split for Linear, GitHub, Drive, and discussion channels

## Working rules for this repo

- **Default scope is documentation-first.** Markdown docs, issue-form YAML, templates, and the existing Phase 2 reusable workflows are in scope. New workflows, composite actions, executable scripts, or automation config still need explicit approval.
- **Bun-forward, stack-neutral.** New JavaScript repos can default to Bun; inherited guidance should stay welcoming to pnpm, yarn, npm, and non-JS repos.
- **Use GitHub issue types for work classification.** `Bug`, `Story`, `Epic`, and `Task` carry issue kind; labels are for cross-cutting dimensions, sources, routines, and automation state.
- **Linear is the project-management source of truth.** GitHub owns public execution and RFCs; Drive owns memos and evidence; Discord, Telegram, and calls own discussion.
- **No guild-wide Season framing.** Use `quarter`, `cycle`, `milestone`, or the specific historical program name instead.
- **The dev guild is one guild under Greenpill Network.** Do not describe it as the whole network.

## Directory map

| Path | Purpose |
| --- | --- |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Guild-wide contributor flow and funded scoped work guidance |
| [`GOVERNANCE.md`](./GOVERNANCE.md) | How the dev guild makes cross-project decisions |
| [`PARTNERS.md`](./PARTNERS.md) | Partner, funder, and chapter interface |
| [`SECURITY.md`](./SECURITY.md) | Public vulnerability-reporting policy |
| [`SUPPORT.md`](./SUPPORT.md) | Support routing and expectations |
| [`docs/`](./docs/) | Operating-model docs that support guild-wide coordination |
| [`profile/`](./profile/) | Public org-profile README |
| [`templates/`](./templates/) | Starters for project-level docs |
| [`routines/`](./routines/) | Playbooks for guild operations |
| [`adr/`](./adr/) | Guild ADRs and ADR template |

## Contributing here

For guild-wide changes, open an [RFC](https://github.com/greenpill-dev-guild/.github/issues/new?template=rfc.yml) when the change affects more than one project, shared standards, governance, vocabulary, or partner commitments.

Small clarifications and corrections can go through a normal PR, but keep cross-references aligned in the same change:

- `routines/README.md` should match the actual contents of `routines/`
- `adr/README.md` should match the actual contents of `adr/`
- `profile/README.md`, `CONTRIBUTING.md`, `PARTNERS.md`, and the routines should not drift on funded scoped work, payment language, partner routing, or the Linear operating model
