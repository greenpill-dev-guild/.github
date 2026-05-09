# Funded Work Intake

> How the guild scopes grant-dependent, sponsor-funded, or steward-approved paid work.

**When to use this**: You are a contributor, steward, or maintainer discussing paid scoped work. Volunteer open-source contributions can use the normal project issue and PR flow.

## Operating split

The guild deliberately separates project management and public execution:

- **Linear** — funding context, owner, status, acceptance criteria, deadlines, and payment/completion state.
- **GitHub** — public implementation issues, pull requests, code review, and repo-local execution references.
- **Drive** — private or semi-private grant scopes, sponsor notes, evidence bundles, and working docs.
- **Discord / Telegram / calls** — discussion and check-ins, not canonical commitments.

Do not treat a GitHub issue, roadmap idea, partner request, or community ask as paid work until scope and funding are confirmed.

## Contributor flow

### 1. Start with a scoped opportunity

Funded scoped work usually starts from:

- An active grant or funder commitment.
- A sponsor-approved scope.
- A maintainer or steward identifying budget for a bounded task.
- A partner need that has been accepted into Linear.

If the opportunity is unclear, ask a maintainer or steward before drafting a proposal.

### 2. Confirm scope and funding

Before implementation starts, confirm:

- Deliverables and acceptance criteria.
- Project, package, or design surface affected.
- Review path and required validation.
- Timeline, milestones, and check-in cadence.
- Funding source, payment amount, payment method, and payment timing.
- Any privacy, partner, or grant-reporting constraints.

Keep the agreement concrete. A short scope with crisp acceptance criteria is better than a broad promise.

### 3. Track in Linear

Accepted funded scoped work is tracked in Linear. The Linear item should carry enough context for stewards and maintainers to understand:

- What is being delivered.
- Who owns it.
- What funding or sponsor context applies.
- What "done" means.
- Which GitHub issue, PR, Drive doc, or partner context is linked.

Funding opportunities use the `funding:*` lifecycle labels in Linear and saved views. GitHub is not the funding pipeline.

### 4. Open a GitHub execution reference when useful

Open a GitHub issue only when public implementation needs a repo-local reference. Use the funded scoped work issue template when a maintainer asks for a GitHub execution-side issue.

The GitHub issue should link to the Linear item or funding reference when appropriate, but it should not duplicate private budget, partner, or grant details.

### 5. Do the work

- Branch from the project's default branch.
- Follow the project's `CONTRIBUTING.md`, `AGENTS.md`, and `CLAUDE.md`.
- Open a draft PR early for implementation work when helpful.
- Keep CI green and include the agreed validation.
- Raise timing, risk, or scope changes before they become blockers.

### 6. Check in

Use the same short update shape for synchronous or async check-ins:

| Item | What to say |
| --- | --- |
| **Done** | What shipped, merged, or was decided since last check-in |
| **Doing** | What is planned before the next check-in |
| **Blocked** | Decisions, access, review, or context needed |
| **Risks** | Scope, timeline, funding, partner, or validation risks |

See [weekly-checkin.md](./weekly-checkin.md) for the full format.

### 7. Complete and close out

Completion is based on the accepted scope:

1. Acceptance criteria are met.
2. Required tests, review, or design handoff are complete.
3. PRs, Drive docs, or deliverables are linked from Linear.
4. Deviations from scope are documented.
5. Stewards or maintainers confirm completion and payment handling.

Payment terms vary by grant, sponsor, or budget. Confirm them in writing before work starts.

## Steward / maintainer checks

Before accepting funded scoped work:

- Is the scope bounded and aligned with an active funding source?
- Is the contributor or team a good fit for the work?
- Is the review path clear?
- Are private partner, budget, or grant details kept out of public GitHub issues?
- Is Linear the canonical status surface?

Before marking complete:

- Did the work meet the acceptance criteria?
- Is validation recorded?
- Are public artifacts linked where appropriate?
- Are follow-up issues separated from completion?
- Are payment/completion notes captured in the right private surface?

## Common pitfalls

- **Treating open issues as paid by default** — they are not.
- **Duplicating private funding details into GitHub** — keep those in Linear or Drive.
- **Letting scope drift silently** — raise it immediately.
- **Tracking status in chat only** — discussions are not the source of truth.
- **Skipping validation** — funded work still needs the same quality bar as volunteer work.

## See also

- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [Linear operating model](../docs/linear-operating-model.md)
- [weekly-checkin.md](./weekly-checkin.md)
- [Partner interface](../PARTNERS.md)
