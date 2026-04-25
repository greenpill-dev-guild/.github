# Bounty Intake

> The end-to-end bounty flow, from "I see an opportunity" to "I got paid."

**When to use this**: You are a contributor (new or returning) interested in claiming guild bounty work. Or you are a steward / project maintainer reviewing applications.

## Operational split

The guild deliberately separates **operations** and **execution**:

- **Operations** — bounty listing, application, stipend release, final approval, payout — happen in the **guild workspace** at `greenpill.app/dev-guild` *(coming soon — currently on Charmverse during migration)*.
- **Execution** — the actual work — happens on **GitHub** in the relevant project repo (issues, PRs, code review).

Don't mix the two. The guild workspace is the source of truth for "is this person engaged on this bounty"; GitHub is the source of truth for "what is the state of the work."

## Contributor flow

### 1. Find a bounty

Browse the bounty list in the guild workspace. Bounties include:

- A description and acceptance criteria
- A target project
- Estimated effort and stipend amount
- Any prerequisites

If a bounty looks promising but you have questions, ask in Discord (`#bounties` or the project's channel) or in the weekly call before applying.

### 2. Apply

Submit a formal application in the workspace including:

- Your background (link to GitHub, prior work, anything relevant)
- Your **timeline** — when you can start, key milestones, expected completion
- Your **technical approach** — what you understand about the problem, your proposed approach, open questions
- Any conflicts of interest or other commitments

Keep it tight. Stewards prefer 1–2 paragraphs of substance over 5 paragraphs of preamble.

### 3. Review and acceptance

A steward (often the project maintainer) reviews and either:

- **Accepts** — you receive a development stipend to begin work
- **Requests revision** — usually because scope or approach needs alignment
- **Declines** — with a short reason; nothing personal

Acceptance turnaround is generally one weekly call cycle. If urgent, flag it in Discord.

### 4. Open the GitHub tracking issue

Once accepted, open a `Bounty application` issue on the project repo using its inherited issue form, with:

- A link back to the workspace bounty
- Your scope and timeline
- Technical context for reviewers

This issue is the single open place where reviewers can track progress without needing workspace access.

### 5. Do the work

- Branch from the project's default branch (note: it varies — `main`, `develop`, or `dev` depending on the repo)
- Follow the project's `CONTRIBUTING.md` and `AGENTS.md` / `CLAUDE.md`
- Open a PR early as a draft so reviewers can follow along
- Keep CI green

### 6. Weekly check-ins

Show up to the weekly call (or post async if you can't make it). 15 minutes max. Cover:

- What you've done since last week
- What you're doing this week
- Blockers or open questions

See [weekly-checkin.md](./weekly-checkin.md) for the full format.

### 7. Submit for final approval

When work is merged:

1. Mark the workspace bounty as ready for final approval
2. Link to the merged PR(s)
3. Note any deviations from the original scope and why

### 8. Payout

A steward reviews and approves. Final payment is sent via [Optimism](https://www.optimism.io/) within 2 business days.

## Steward / maintainer flow

Reviewing an application:

1. **Scope check** — Is the proposed scope aligned with the bounty? Realistic?
2. **Capacity check** — Does this contributor have bandwidth? Other open bounties?
3. **Fit check** — Does their background match the technical needs?
4. **Decision** — accept, request revision, or decline. Short explicit reason either way.

Reviewing final submission:

1. **Acceptance criteria met?** — every item in the original bounty
2. **Tests and CI green?** — required
3. **Docs updated?** — for behavior changes
4. **Any follow-up issues?** — open them and link from the bounty before closing

## Common pitfalls

- **Scoping too big** — break large bounties into multiple smaller ones rather than one mega-PR.
- **Skipping check-ins** — silence for 2+ weeks is the strongest predictor of bounty failure. Stewards may rescind unaccepted bounties after extended silence.
- **Mixing workspace and GitHub state** — keep both updated; don't assume one mirrors the other.
- **Letting CI rot** — bounties with red CI for more than a week get flagged; fix it or ask for help.
- **Surprise scope creep** — if you discover the bounty needs more than the stipend covers, raise it in a check-in immediately, not at submission.

## See also

- [CONTRIBUTING.md](../CONTRIBUTING.md) · the public-facing summary of this flow
- [weekly-checkin.md](./weekly-checkin.md)
- [newcomer-onboarding.md](./newcomer-onboarding.md)
