# Drive map (reference for active routine scope)

The cloud routines authenticate against Afo's Google Drive via the Google-Drive connector. They cannot use folder paths reliably — Drive search via the connector exposes only `title`, `fullText`, `mimeType`, `modifiedTime`, `viewedByMeTime` query terms (no `parents` or path globs). So active routine scope rules MUST be expressed as content queries plus reject steps inside each prompt.

## Active surfaces (probed 2026-04-25)

### Folders that exist (for human reference; do NOT hardcode in prompts)

| Folder | ID | Notes |
|---|---|---|
| Dev Guild | `1C5rv07P9XGAeL17O6wwzkPeL2Mf5TuY9` | top-level shared guild folder |
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
| `title contains 'Notes by Gemini'` | Gemini-generated meeting notes | active routines may read only when their prompt allow-list and reject step permits |
| `title contains 'Guild Weekly'` | prior `guild-weekly-synthesis` outputs | `guild-weekly-synthesis` prior context |
| `title contains 'Proposal' or title contains 'Grant'` | grant/funding docs | `guild-grant-scout` (allow), all others (reject) |
| `title contains 'Sync'` | recurring guild sync notes (often Gemini-generated) | informational |
| `title contains 'research synthesis'` | prior research memos | `research-synthesis` prior context |

### Topic indicators (use in `fullText contains` for content classification)

- **Design**: `'mockup'`, `'figma'`, `'storybook'`, `'token'`, `'palette'`, `'AdminCard'`, `'M3'`, `'liquid glass'`, `'warm earth'`
- **Research**: `'paper'`, `'protocol'`, `'mechanism design'`, `'attestation'`, `'CRDT'`, `'EAS'`, `'Hypercert'`
- **Grants**: `'grant'`, `'proposal'`, `'NLnet'`, `'Octant'`, `'Gitcoin'`, `'EthGlobal'`, `'milestone'`, `'budget'`
- **Treasury**: `'treasury'`, `'multisig'`, `'runway'`, `'working capital'`, `'payment'`
- **Bug-intake (Green Goods user pain)**: `'doesn\'t work'`, `'broken'`, `'confusing'`, `'crashed'`, `'lost data'`, `'operator'`, `'gardener'`

## Query patterns by active routine

### `research-synthesis` — Drive supplement (only when channel had >=5 messages)
```
modifiedTime > '<7d ago>' and (fullText contains 'paper' or fullText contains 'protocol' or fullText contains 'mechanism design' or title contains 'research')
```
Plus: any Drive doc directly linked from a `#research` Discord message in the 7-day window. Drop grant/treasury/strategy hits.

### `guild-weekly-synthesis` — Drive context (7-day)
```
modifiedTime > '<7d ago>' and (title contains 'Notes by Gemini' or title contains 'Dev Guild' or title contains 'Greenpill' or title contains 'Guild Weekly')
```
The routine prompt applies the full allow-list and reject step. Grants/funding, treasury, private agreements, and unrelated WEFA/personal content are rejected before synthesis.

### `guild-grant-scout` — Drive (broad-by-design)
```
modifiedTime > '<14d ago>' and (title contains 'Proposal' or title contains 'Grant' or fullText contains 'grant' or fullText contains 'NLnet' or fullText contains 'Octant')
```
This routine OWNS the grant lane; broad scope is intentional.

## Maintenance

When the canonical Drive layout shifts (new shared folders, naming convention changes), update this file and the affected routine prompts together. Folder IDs are kept here only to help humans verify queries against actual content — they should not be referenced in prompts.
