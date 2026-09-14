# Greenpill Dev Guild

> A community of regen builders shipping public goods for impact measurement, capital allocation, capital formation and community coordination.

We are one of several skill-specific Guilds under the [Greenpill Network](https://greenpill.network) — a decentralized community of regional Chapters and skill-specific Guilds working to turn degens into regens. Since October 2023 we've been building tools, running grant rounds, and supporting Greenpill Chapters across the world.

We are both **grantees** and **grantmakers**: funded by Octant, Giveth, and Gitcoin — and operating Grant Ships and Gitcoin community rounds that fund other regen projects.

---

## What we ship

Active guild-owned projects we build and maintain:

| Project | What it does | Stack |
| --- | --- | --- |
| [**green-goods**](https://github.com/greenpill-dev-guild/green-goods) | Offline-first PWA documenting regenerative work on-chain (attestations, hypercerts, impact). Flagship. | TypeScript · Solidity · Bun |
| [**network-website**](https://github.com/greenpill-dev-guild/network-website) | Frontend for greenpill.network. | TypeScript |

This profile focuses on guild-owned GitHub projects and earlier guild artifacts. Upstream forks we use for ecosystem contribution or integration are not treated as active project inventory here.

## Now building

<!-- now-building:start -->
- **Green Goods**: the flagship regen-documentation PWA is cutting its v1.3.0 release, with this month's work going into offline reliability — a gardener can complete a whole work submission with no connection and have it sync on reconnect — and into recovery for the installed app.
- **Commitment Pooling**: per-garden pools where a community names a need, members promise help, and the person helped confirms it — the contracts, shared API, and client interface are built, and the first garden pool is being configured after the first community workshop.
- **Garden distributions**: a funded pilot is making its first direct distribution to selected gardens, with the allocation model in review and the first report being packaged.
<!-- now-building:end -->

## Recently shipped

<!-- recently-shipped:start -->
- **Green Goods**: shipped [v1.2.2](https://github.com/greenpill-dev-guild/green-goods/releases/tag/v1.2.2), a patch that gets passkey signing working again in production — passkey users could sign in but every approval failed, and the fix lands without moving anyone's account or asking anyone to re-register.
- **Guild org repo**: the [meeting filer](https://github.com/greenpill-dev-guild/.github/pull/63) routine now fails loudly when its source lock does not match, instead of quietly filing to the wrong place, and clears out its own stale documents.
<!-- recently-shipped:end -->

## Across the guild

How work is organized: five teams — Product, Research, Community, Growth, and Marketing — tracked in Linear ([how we run them](https://github.com/greenpill-dev-guild/.github/blob/main/docs/teams/README.md)). What each is on right now:

<!-- team-shipping:start -->
- **Product** — cutting the v1.3.0 release and working through QA findings across the client and admin surfaces, after shipping the v1.2.2 passkey signing patch and making work submission survive going offline mid-flow.
- **Research** — reading an existing community-credit deployment before committing to voucher interoperability for Commitment Pooling, and setting the entry criteria for reporting impact over WhatsApp and SMS.
- **Community** — onboarding the first pooling operators and configuring the first garden pool, after running the commitment-pooling workshop with a pilot hub and clearing the outstanding gardener work approvals.
- **Growth** — running the Artizen Season 7 raise and keeping reporting current on active grant awards, with the allocation model for a funded garden pilot's first distribution now in review.
<!-- team-shipping:end -->

## Past work

Notable earlier artifacts — public, open-source, and worth referencing:

- [**greenwill**](https://github.com/greenpill-dev-guild/greenwill) · Farcaster Frame for regen reputation scoring (the "GreenWill" reputation primitive)
- [**allo-yeeter**](https://github.com/greenpill-dev-guild/allo-yeeter) · Allo-protocol disbursement tool
- [**impact-reef**](https://github.com/greenpill-dev-guild/impact-reef) · Qualitative impact evaluation
- [**regen-rabbit-race**](https://github.com/greenpill-dev-guild/regen-rabbit-race) · Farcaster betting frame
- [**greenpill-commons**](https://github.com/greenpill-dev-guild/greenpill-commons) · Community proposals PWA
- [**cookie-jar**](https://github.com/greenpill-dev-guild/cookie-jar) · Smart-contract-governed funding pools (allowlist, NFT, POAP, Hypercert, and Hats gating)

---

## How we work

Contribution flows through scoped project work. Some work is volunteer open-source contribution; paid work depends on active grants, sponsors, or steward-approved budgets.

1. **Start** with a project issue, proposal, or maintainer-scoped work item.
2. **Confirm** deliverables, acceptance criteria, and review path before implementation.
3. **Know how it pays**: guild members claim a monthly stipend against work tracked and accepted on Linear — see the [compensation playbook](https://github.com/greenpill-dev-guild/.github/blob/main/routines/scoped-work-compensation.md).
4. **Submit** a PR or design artifact linked to the agreed scope.
5. **Review** for quality, scope, tests, and project fit.

Our working cadence is a **weekly** public call, **monthly** Twitter/X Spaces and/or forum updates, **quarterly** overviews, and regular workshops on Hypercerts, EAS, and other regen primitives.

Full contributor flow: [CONTRIBUTING.md](https://github.com/greenpill-dev-guild/.github/blob/main/CONTRIBUTING.md). Guild-wide playbooks: [routines/](https://github.com/greenpill-dev-guild/.github/tree/main/routines).

## How we're funded — and how we fund

**Funded by**: [GitHub Sponsors](https://github.com/sponsors/greenpill-dev-guild) · [Gitcoin](https://explorer.gitcoin.co/) · [Giveth](https://giveth.io/project/greenpill-dev-guild) · [Octant](https://octant.app/).

**We fund**: regenerative projects across gaming and public goods through Grant Ships rounds, Gitcoin community rounds (including the GreenPill x Octant round), and clearly scoped grant-dependent work. Contributor compensation runs through a monthly [Cookie Jar stipend](https://github.com/greenpill-dev-guild/.github/blob/main/routines/scoped-work-compensation.md) backed by Linear-tracked work.

---

## Get involved

| You are... | Start here |
| --- | --- |
| A **developer or designer** wanting to ship regen tools | Join [Telegram](https://t.me/+n7g-u8wYtwQ2YjVi) · [Discord](https://discord.gg/ZJjft2EKz7) · read [CONTRIBUTING.md](https://github.com/greenpill-dev-guild/.github/blob/main/CONTRIBUTING.md) |
| A **partner** building regen infrastructure | Read [PARTNERS.md](https://github.com/greenpill-dev-guild/.github/blob/main/PARTNERS.md) · email `contact@greenpill.builders` |
| A **funder or sponsor** | See our [funding profiles](https://github.com/greenpill-dev-guild/.github/blob/main/FUNDING.yml) |
| A **chapter or community** wanting tools | Open an issue on the relevant project repo |

## Governance and contact

Guild operations are stewarded by a **stewardship team** that handles Code of Conduct enforcement, governance, and treasury. See [GOVERNANCE.md](https://github.com/greenpill-dev-guild/.github/blob/main/GOVERNANCE.md).

Project management and all accepted work run through Linear; GitHub is the public surface for code, pull requests, review, releases, and RFC/ADR markdown. See the [Linear operating model](https://github.com/greenpill-dev-guild/.github/blob/main/docs/linear-operating-model.md).

| Channel | Email |
| --- | --- |
| General | `contact@greenpill.builders` |
| Stewards / governance | `steward@greenpill.builders` |
| Security / responsible disclosure | `security@greenpill.builders` |

---

*All guild work is open-source. Code is MIT licensed unless otherwise noted. Read our [Code of Conduct](https://github.com/greenpill-dev-guild/.github/blob/main/CODE_OF_CONDUCT.md) and [Security Policy](https://github.com/greenpill-dev-guild/.github/blob/main/SECURITY.md) before contributing.*
