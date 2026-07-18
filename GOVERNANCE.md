# Governance

> How the Greenpill Dev Guild makes decisions, distributes responsibility, and evolves over time.

The guild is one of several skill-specific Guilds under the [Greenpill Network](https://greenpill.network). This document covers the dev guild's internal governance only. Network-level coordination lives at the network layer.

## Stewardship team

A small, accountable group responsible for:

- **Code of Conduct enforcement** — investigating reports, deciding consequences (see [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md))
- **Treasury and funded-work approval** — sign-off on scoped budgets, stipend claim review, and completion
- **Org access** — granting and revoking GitHub org membership, repo access, and elevated roles
- **Strategic direction** — quarterly overview decisions, partnership commitments, grant applications
- **Conflict resolution** — mediating disputes between contributors or maintainers

Reach the stewardship team at `steward@greenpill.builders`.

## Roles

The guild operates with the following recognized roles (sourced from our Guild.xyz roster):

- **Stewards** · core governance, treasury, partnerships
- **Admins** · org-level GitHub administration, security, infrastructure
- **Engineering / Product / Research / Community / Marketing / Growth Leads** · domain leadership for active workstreams; each discipline lead anchors a scope-acceptance panel (see Decision-making)
- **Contributors** · funded scoped workers, volunteer contributors, and ongoing project contributors (Brand, Social, Community, Engineering)
- **Treasury Manager** and **Work Capital Manager** · financial operations
- **Partners** · external organizations and individuals with formal collaboration agreements

Roles are not permanent. Active contribution determines standing.

## Decision-making

Decisions are made at the lowest reasonable scope:

| Scope | Who decides | How |
| --- | --- | --- |
| **Project-level technical** (e.g. green-goods architecture) | Project maintainers | PR review, repo CODEOWNERS |
| **Cross-project standards** (e.g. shared CI, this `.github` repo) | Engineering Lead + Stewards | RFC + lazy consensus on the forum |
| **Stipend claims & treasury** | Stewards | Cookie Jar claims reviewed against the monthly stipend ledger (see the [compensation playbook](./routines/scoped-work-compensation.md)); multi-sig sign-off for payouts outside the jar |
| **Scope acceptance** (scoped-brief sign-off) | Team evaluator panel (2–3 reviewers per Linear team; afo standing on every panel; rosters in the [team charters](./docs/teams/README.md) and the Evaluator Panels Linear Document) | Estimate set + panel ack moves Backlog → Todo; 3-day async SLA |
| **Org membership and access** | Admins + Stewards | Steward sign-off required |
| **Code of Conduct cases** | Stewardship team | Confidential, see CoC |
| **Partnerships and external commitments** | Stewards | Public announcement after decision |

## RFC process

For changes that affect more than one project (shared CI, vocabulary conventions, treasury policy, partnership commitments), open an RFC:

1. Start a thread on the forum describing the proposed change and why it generalizes.
2. Open a PR to this `.github` repo with the concrete change (docs, config, or template).
3. Allow **7 days** for written feedback (longer for high-impact changes).
4. Stewards close the RFC with a decision and a short rationale; record lasting outcomes as an ADR in [adr/](./adr/).

ADRs (architectural decision records) capture the outcomes that durably shape how the guild builds. See [adr/](./adr/).

## Typical cadence

- **Weekly** — public guild call when active (open to all; agenda on the forum)
- **Monthly** — Twitter/X Spaces and/or written forum update
- **Quarterly** — comprehensive overview (progress, treasury, roadmap)
- **Annually** — strategic review and steward rotation

## Org technical conventions

These are enforced at the GitHub org level for all guild repos:

- **Two-factor authentication** required for all org members
- **Signed commits** required on protected branches
- **MIT license** unless otherwise documented
- **Default repository permission**: read
- New repo creation gated to stewards/admins

## Changing this document

Updates to GOVERNANCE.md follow the RFC process above. Substantive changes require steward approval and a 7-day comment window.
