# Contributing to the Greenpill Dev Guild

Welcome! We're glad you're here. This guide covers how to get involved, take on scoped work, and ship contributions that meet guild standards across our projects.

## Table of contents

- [Getting started](#getting-started)
- [Funded scoped work](#funded-scoped-work)
- [Development guidelines](#development-guidelines)
- [Submitting your work](#submitting-your-work)
- [Review process](#review-process)
- [Funded work completion](#funded-work-completion)
- [Agentic development](#agentic-development)
- [Resources](#resources)
- [Code of Conduct](#code-of-conduct)

---

## Getting started

1. **Join our community.** Engage with us on [Telegram](https://t.me/+n7g-u8wYtwQ2YjVi) and [Discord](https://discord.gg/ZJjft2EKz7) to stay updated and ask questions.
2. **Familiarize yourself with our projects.** Browse the active repositories pinned on [our org page](https://github.com/greenpill-dev-guild) — `green-goods`, `coop`, `cookie-jar`, `network-website` are the flagship surfaces.
3. **Read the [Code of Conduct](./CODE_OF_CONDUCT.md).** Required for all contributors.
4. **Skim the [routines/](./routines/)** directory if you're new to the guild — short markdown playbooks for our recurring flows, weekly check-ins, onboarding, retros, and grants.
5. **Know the operating model.** Linear owns project management; GitHub owns public execution, issues, PRs, and RFCs. See [docs/linear-operating-model.md](./docs/linear-operating-model.md).

## Funded scoped work

Some guild work is volunteer open-source contribution. Paid work is grant-dependent or sponsor-dependent and must be clearly scoped before implementation starts.

For funded scoped work:

1. **Confirm the scope** with a maintainer or steward, including deliverables, acceptance criteria, review path, and expected timeline.
2. **Confirm the funding source** before starting. Funding may come from an active grant, sponsor commitment, or maintainer-approved budget.
3. **Track the scope in Linear** when asked, so ownership, status, funding context, and acceptance criteria are visible to maintainers.
4. **Open a GitHub execution issue** only when public implementation or review work needs a repo-local reference.
5. **Check in regularly** while work is active, especially if timing, risk, or scope changes.
6. **Submit your work** through the relevant project repo and include the agreed validation.

## Development guidelines

These apply across all guild projects. Project-specific `AGENTS.md` / `CLAUDE.md` / `CONTRIBUTING.md` files extend or override.

- **Open source only** — all code and dependencies must be open-source-licensed.
- **Test what you ship** — unit tests for new logic, integration tests for cross-package flows, and E2E for user-facing journeys where they exist.
- **Documented contributions** — at minimum, a clear PR description; substantive changes warrant updates to the project's docs.
- **Conventional Commits** — most projects use `type(scope): description` (e.g. `feat(green-goods): add garden filter`). Check the project's `CONTRIBUTING.md` for the exact convention.
- **Bun-forward** — newer guild projects standardize on [Bun](https://bun.sh) as the JavaScript runtime and package manager. If you're scaffolding something new, default to Bun unless there's a specific reason not to.
- **Security best practices** — never commit secrets, validate inputs at system boundaries, follow the [Security Policy](./SECURITY.md).

## Submitting your work

1. **Branch naming** — `type/short-description` (e.g. `feature/hats-v2`, `bug/admin-fix`). Match the project's existing convention.
2. **Pull requests** — use the project's PR template; link to the relevant issue, plan, or funded-work scope; describe what changed and why; include a test plan.
3. **CI must pass** — formatting, linting, tests, and build checks must be green before requesting review.
4. **One approved scope, one PR** where reasonable — long-running work can be split, but coordinate with the maintainer first.
5. **For design work** — submit via Figma or the project's design tool, link from the PR description, and notify the project's design lead.

## Review process

- **Maintainer review** — project maintainers review for correctness, scope adherence, test coverage, and security.
- **Feedback** — if revisions are needed, you'll get a clear list. Address them and request re-review.
- **Approval** — once approved and CI is green, the maintainer merges. For high-risk paths (deploy scripts, contracts, security-sensitive code), an additional steward review may be required.

## Funded work completion

- **Approval** — completion is based on the scoped acceptance criteria and maintainer review.
- **Payment terms** — funded work terms vary by grant, sponsor, or budget. Confirm payment amount, timing, and method in writing before starting.
- **No standing paid-work promise** — open issues, roadmap items, and community requests are not automatically funded work.

## Agentic development

Many guild contributors work with AI coding assistants (Claude Code, Codex, Copilot). The guild publishes shared baselines so this works smoothly:

- **Templates** at [templates/](./templates/) — copy-into-repo starters for `CLAUDE.md`, `AGENTS.md`, and `copilot-instructions.md` if your project doesn't have them yet.
- **Org defaults** — community-health files and issue/PR templates in this repo propagate to guild repos unless overridden locally.
- **Copilot instructions** — use the template here to create a project-local `.github/copilot-instructions.md`, or configure organization-level Copilot instructions in GitHub settings.
- **Reusable workflows** — opt-in building blocks such as labels sync and non-blocking Claude PR review that any guild repo can call explicitly.

If you're using an AI assistant on guild code, treat it like any other contributor: it's bound by these guidelines, the project's `CLAUDE.md` / `AGENTS.md`, and the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Resources

- [Greenpill Dev Guild on GitHub](https://github.com/greenpill-dev-guild)
- [Greenpill Network](https://greenpill.network) — the parent network
- [Routines](./routines/) — markdown playbooks for guild-wide flows
- [Linear Operating Model](./docs/linear-operating-model.md)
- [Partner Interface](./PARTNERS.md)
- [Governance](./GOVERNANCE.md)
- [Security Policy](./SECURITY.md)

## Code of Conduct

Please read and adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md) to keep our community welcoming, inclusive, and productive.

---

Thank you for contributing to the Greenpill Dev Guild — we're excited to build with you.
