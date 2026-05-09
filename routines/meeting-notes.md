# Meeting Notes

> Capturing, processing, and acting on notes from guild meetings — weekly calls, workshops, partner conversations.

**When to use this**: You're taking notes for a guild meeting, or you're processing a backlog of notes into action.

## Why this exists

Notes that don't turn into action are noise. The guild generates real signal in calls — partner intros, scope decisions, blocker patterns, follow-ups owed — and most of it gets lost. This routine exists to make capture cheap and processing systematic.

## Two-stage flow

### Stage 1: Capture (during or immediately after the meeting)

Use whatever tool you prefer (Gemini live notes, Otter, manual). The format that matters is what you produce **after** capture, not during.

Minimum capture:

- Date and meeting type
- Attendees (or "open call")
- Decisions made (with who decided)
- Open questions raised
- Action items with owners

Don't try to make capture pretty in real time.

### Stage 2: Process (within 48 hours)

Convert raw notes into:

1. **Action items as GitHub issues** — anything with an owner and a deliverable. Use the right repo's issue template.
2. **Decisions logged** — append to the relevant ADR if architectural; otherwise a forum post.
3. **Open questions parked** — add to the relevant project's `next-up` doc or the guild forum if cross-project.
4. **Follow-ups scheduled** — calendar items for time-sensitive things.

Anything that doesn't fit one of these categories is probably noise. Drop it.

## File and folder convention

Where notes live right now:

```
01-meetings/
└── YYYY-MM-DD-<meeting-type>/
    ├── agenda.md
    ├── raw-notes.md              # capture, kept private to attendees if needed
    ├── decisions.md              # public-facing decisions
    ├── action-items.md           # mirrored to GitHub issues
    └── recording.md              # recording link or publishing status
```

The shared Drive is the canonical notes store. Linear tracks accepted operational state; GitHub carries public execution artifacts such as issues and PRs.

## Action item format

Each action item should be self-sufficient enough to become a GitHub issue:

- **Owner** — single person, not "team"
- **Deliverable** — specific, observable
- **Deadline** — explicit; "next week" is OK if it's the same weekly call cycle
- **Context** — one or two sentences so the owner doesn't need to listen to the recording

Bad: *"Look at the indexer thing"*
Good: *"@alice — by next Wed, open an issue describing the green-goods indexer schema drift Bob raised today, including which fields diverged and a proposed fix direction."*

## Patterns to watch for

While processing notes, watch for:

- **The same blocker reported 3+ weeks** — escalate; it's a structural issue
- **Repeated partner intros without follow-up** — the guild has a pattern of meeting partners and not closing; surface this
- **Decisions made informally without being captured** — re-ask in the next call to confirm
- **Action items that age out** — owner changed jobs, project shifted; close them honestly

## Tools

The guild has used a few approaches; pick what works:

- **Gemini meeting notes** — good for live capture; needs cleanup
- **Otter transcription** — good for searchable archive; weak for action extraction
- **Parallel oracle agents** (for guild members using AI assistants) — proven workflow for extracting action items from raw transcripts. See your project's `.claude/skills/` if applicable.
- **Manual** — slower but produces the cleanest output

## Public vs private

- **Decisions** — default public unless they involve treasury, personnel, or partner confidentiality
- **Raw notes** — default private to attendees; can be shared on request
- **Action items** — default public (as GitHub issues)
- **Personnel discussions** — always private

## Common pitfalls

- **Capturing without processing** — notes alone are not output; processed action items are.
- **Action items without owners** — they don't happen.
- **Re-litigating decisions in later meetings** — link to the prior decision instead.
- **Letting notes accumulate without weekly digestion** — backlog becomes unsalvageable past 2–3 weeks.

## See also

- [weekly-checkin.md](./weekly-checkin.md)
- [drive-orchestration.md](./drive-orchestration.md) — where shared notes live
- [retro-cadence.md](./retro-cadence.md) — patterns from notes inform retros
