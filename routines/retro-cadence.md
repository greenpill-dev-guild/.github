# Retro Cadence

> Quarterly and annual retrospectives for the guild — what worked, what didn't, what changes.

**When to use this**: You're hosting or contributing to a guild retrospective.

## Why this exists

Retros that don't change behavior are theater. The guild does retros to honestly look at what worked and what didn't, and to commit to specific changes — not just to feel introspective.

## Cadence

| Type | Frequency | Length | Output |
| --- | --- | --- | --- |
| **Project retro** | End of each major funded scope, volunteer push, or milestone | 30–45 min | Project-specific changes |
| **Quarterly guild retro** | Every 3 months | 60–90 min | Forum post, action items |
| **Annual review** | Every 12 months | 2 hours | Quarterly overview, steward rotation |

## Quarterly guild retro

The standard format. Run by a steward; open to all guild members.

### Prep (one week ahead)

- **Pull data**:
  - Bounties opened, accepted, completed, declined this quarter
  - Grants applied for, won, declined
  - New contributors onboarded; contributors gone quiet
  - Major shipped work per project
  - Treasury inflows and outflows
- **Send pre-read** — share the data with attendees 48 hours before the retro
- **Solicit topics** — async via forum or Discord; don't surprise people in the call

### During the retro

Format (90 min):

1. **Frame** (5 min) — what we covered last retro, what we committed to, what actually happened
2. **What went well** (15 min) — facts, not vibes; reference data
3. **What didn't go well** (20 min) — same: facts, not vibes
4. **Patterns** (15 min) — recurring blockers, recurring strengths, recurring requests
5. **Decisions** (20 min) — what specifically will change next quarter? Each decision needs an owner.
6. **Wrap** (5 min) — confirm the action list and who owns the writeup

Discord voice; record for absent members; store `agenda.md`, `raw-notes.md`, `decisions.md`, `action-items.md`, and the recording link in the shared Drive folder `01-meetings/YYYY-MM-DD-quarterly-retro/`, following [meeting-notes.md](./meeting-notes.md).

### After the retro

Within 1 week:

- **Forum post** summarizing the retro publicly (omit anything sensitive)
- **GitHub issues** for each action item, on the relevant repo
- **Calendar** the next retro
- **Update the guild quarterly overview** (per [GOVERNANCE.md](../GOVERNANCE.md))

## Annual review

Heavier than quarterly. Same structure but:

- Look at the year's quarterly retro outcomes — did committed changes stick?
- Review steward roster; rotate if appropriate (per GOVERNANCE)
- Set themes for the next year (not specific deliverables; broader direction)
- Refresh the [profile README](../profile/README.md) and `routines/` for accuracy

## Project retros

Lighter, project-specific. Run after a major shipped milestone or at the end of a delivery cycle.

Format (45 min):

1. **What shipped** (10 min) — the actual delivered work
2. **What surprised us** (10 min) — both positive and negative
3. **What we'd do differently** (15 min) — concrete process changes
4. **What's next** (10 min) — handing off to the next phase

Output goes to the project's repo (e.g. `RETRO-YYYY-Q3.md` or in `docs/retros/`).

## Anti-patterns to avoid

- **Vague retros** — "we should communicate better" is not a decision; "we'll switch to weekly written check-ins for cross-project work" is.
- **Action items without owners** — they don't happen.
- **Retros that ignore data** — relying on memory rather than pulling actual numbers leads to recency bias.
- **Treating retros as therapy** — venting is fine; it's not the output.
- **Skipping the followup** — retros without followup lose all value; the second retro will rehash the same complaints.
- **Inviting only the people who succeeded** — retros need the contributors who struggled too.

## What to track over time

The retro outcomes themselves are signal. Maintain a simple log:

```
00-org/retro-log.md
```

Per quarter, two columns: **decided** and **what actually happened**. Reviewing this log at the next retro is one of the highest-leverage 5 minutes the guild does.

## Common pitfalls

- **Skipping the quarter when busy** — busy quarters are exactly when retros help
- **Inviting only contributors, not stewards** — both perspectives needed
- **Letting the loudest voice dominate** — facilitator's job to round-robin
- **Conflating retro with planning** — retro looks back; planning is a separate session

## See also

- [meeting-notes.md](./meeting-notes.md) — retro outputs flow through this routine
- [GOVERNANCE.md](../GOVERNANCE.md) — quarterly overview cadence is governance
