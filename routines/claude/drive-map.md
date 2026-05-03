# Drive map (reference for routine scope)

The cloud routines authenticate against Afo's Google Drive via the Google-Drive connector. They cannot use folder paths reliably — Drive search via the connector exposes only `title`, `fullText`, `mimeType`, `modifiedTime`, `viewedByMeTime` query terms (no `parents` or path globs). So routine scope rules MUST be expressed as content queries.

## Active surfaces (probed 2026-04-25)

### Folders that exist (for human reference; do NOT hardcode in prompts)

| Folder | ID | Notes |
|---|---|---|
| Dev Guild | `1C5rv07P9XGAeL17O6wwzkPeL2Mf5TuY9` | top-level shared guild folder |
| Dev Guild / Daily Synthesis | `17ZqYMPUmTZfGdIfXk1cnVS6XdbBUYqhJ` | where `guild-daily-synthesis` writes its appendix |
| Green Goods (under WEFA) | `1YrcH98Gn0m_Z5hTWbayCNGGi9cTXE6MK` | contains Green Goods Deck |
| Green Goods (separate) | `1b3ZNBe8NTTqoDl7Z_Vdsoj9eYYn5IeFl` | older project folder |
| Research | `1Bo0RrdPT4fV3YokI4Wd9iqAYo-7rAseK` | guild research |
| Grants (Yoruba) | `1y_5eSi317pYjgQHs6jc1xteqwuxCIC4Y` | |
| Grants GP DEV GUILD | `18NFXWl_ajKKguRp-eHh6_HNvX5gJLgpo` | |
| Proposals | `1R91xwq50_iKkuriNyavQYzheQcHUCxmA` | |
| Design Patterns | `1ddob1s5S5VWrxcsaFbSJ3iPnzy9r6wQb` | |

The "Notes by Gemini" automatic-meeting-notes parent folder appears to be `15rffge0LlFlD_sa7hH5vv2SFag7SEDfa` based on observation.

### Reliable title patterns (for routine queries)

| Pattern | What it captures | Used by |
|---|---|---|
| `title contains 'Notes by Gemini'` | every Gemini-generated meeting note (consistent format) | `bug-intake`, `metrics`, `guild-daily-synthesis`, `guild-product-development-synthesis`, `guild-weekly-checkin` |
| `title contains 'daily synthesis'` | prior `guild-daily-synthesis` outputs | `guild-daily-synthesis` (read prior) |
| `title contains 'Proposal' or title contains 'Grant'` | grant/funding docs | `guild-grant-scout` (allow), all others (reject) |
| `title contains 'Sync'` | recurring guild sync notes (often Gemini-generated) | informational |
| `title contains 'Green Goods'` | GG-tagged docs | `bug-intake`, `metrics` (project filter) |

### Topic indicators (use in `fullText contains` for content classification)

- **Design**: `'mockup'`, `'figma'`, `'storybook'`, `'token'`, `'palette'`, `'AdminCard'`, `'M3'`, `'liquid glass'`, `'warm earth'`
- **Research**: `'paper'`, `'protocol'`, `'mechanism design'`, `'attestation'`, `'CRDT'`, `'EAS'`, `'Hypercert'`
- **Grants**: `'grant'`, `'proposal'`, `'NLnet'`, `'Octant'`, `'Gitcoin'`, `'EthGlobal'`, `'milestone'`, `'budget'`
- **Treasury**: `'treasury'`, `'multisig'`, `'runway'`, `'working capital'`, `'payment'`
- **Bug-intake (Green Goods user pain)**: `'doesn\'t work'`, `'broken'`, `'confusing'`, `'crashed'`, `'lost data'`, `'operator'`, `'gardener'`

## Query patterns by routine

### `bug-intake` — Drive Phase 3
```
title contains 'Notes by Gemini' and modifiedTime > '<48h ago>' and (title contains 'Green Goods' or fullText contains 'Green Goods' or fullText contains 'gardener' or fullText contains 'operator')
```
After fetch, drop any doc whose primary topic matches the grant/treasury/strategy denylist above.

### `metrics` — Drive enrichment
```
title contains 'Notes by Gemini' and modifiedTime > '<14d ago>' and (fullText contains 'target' or fullText contains 'commitment' or fullText contains 'KPI' or fullText contains 'metric')
```
Only confirm explicit targets that were stated in meetings — never fabricate context from grant/strategy docs.

### `design-synthesis` — Drive supplement (only when channel had >=5 messages)
```
modifiedTime > '<7d ago>' and (title contains 'design' or title contains 'mockup' or fullText contains 'figma.com')
```
Plus: any Drive doc directly linked from a `#design` Discord message in the 7-day window (follow links by file ID). Drop grant/treasury/strategy hits.

### `research-synthesis` — Drive supplement (only when channel had >=5 messages)
```
modifiedTime > '<7d ago>' and (fullText contains 'paper' or fullText contains 'protocol' or fullText contains 'mechanism design' or title contains 'research')
```
Plus: any Drive doc directly linked from a `#research` Discord message in the 7-day window. Drop grant/treasury/strategy hits.

### `guild-daily-synthesis` — Drive context (24-48h)
```
modifiedTime > '<48h ago>' and (title contains 'Notes by Gemini' or title contains 'Dev Guild' or title contains 'Greenpill') and (fullText contains 'Green Goods' or fullText contains 'Coop' or fullText contains 'Cookie Jar' or fullText contains 'TAS-Hub' or fullText contains 'Dev Guild' or fullText contains 'Greenpill Network' or fullText contains 'gardener' or fullText contains 'operator' or fullText contains 'guild lead' or fullText contains 'lead council')
```
Dual-clause: title narrows to intentionally guild-relevant docs (drop bare 'Sync'/'Council' personal-calendar artifacts); fullText proves the doc actually mentions a guild project, ecosystem, or known role. Then drop docs whose title contains `'WEFA'` / `'wefa.world'` (Afo's separate project — not dev-guild scope) or where `'WEFA'` appears 5+ times in the body but no guild project name appears at all. This routine is still the broadest reader by intent — the dual-clause + reject step prevents personal-project leakage without forcing a narrow query.

### `guild-product-development-synthesis` — Drive (14-day)
```
modifiedTime > '<14d ago>' and (title contains 'Notes by Gemini' or title contains 'Sync' or title contains 'Workshop' or title contains 'Roadmap' or fullText contains 'product')
```
Reject grants/treasury hits. Output is private (Drive memo + lead-council).

### `guild-weekly-checkin` — Drive (7-day)
```
modifiedTime > '<7d ago>' and (title contains 'Notes by Gemini' or title contains 'Sync' or title contains 'Workshop' or title contains 'Council' or title contains 'Retro')
```
Output's public excerpt is gated by the existing redaction rules; full check-in stays private.

### `guild-grant-scout` — Drive (broad-by-design)
```
modifiedTime > '<14d ago>' and (title contains 'Proposal' or title contains 'Grant' or fullText contains 'grant' or fullText contains 'NLnet' or fullText contains 'Octant')
```
This routine OWNS the grant lane; broad scope is intentional.

## Maintenance

When the canonical Drive layout shifts (new shared folders, naming convention changes), update this file and the affected routine prompts together. Folder IDs are kept here only to help humans verify queries against actual content — they should not be referenced in prompts.
