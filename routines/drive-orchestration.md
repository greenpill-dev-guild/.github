# Drive Orchestration

> Shared Google Drive folder taxonomy and a sorting flow that keeps it usable.

**When to use this**: You're maintaining the guild's shared Drive, or you're contributing files and want to know where they go.

## Why this exists

Shared drives without a taxonomy turn into search-only. The guild generates meeting notes, grant drafts, partner decks, design files, and treasury exports — when these aren't sorted, they're effectively gone.

## Top-level taxonomy

The shared Drive root has a small, stable set of top-level folders. Resist the urge to add more.

```
greenpill-dev-guild/
├── 00-org/                  # mission, charter, governance, foundational docs
├── 01-meetings/             # weekly call notes, monthly recaps, partner meetings
├── 02-grants/               # active and past grant applications, by funder
├── 03-projects/             # one folder per first-party project
├── 04-partners/             # one folder per active partner relationship
├── 05-treasury/             # financial reports, payouts, multi-sig records
├── 06-design/               # brand assets, design files, references
├── 07-workshops/            # slides, recordings, materials
└── 99-archive/              # things we keep but don't actively use
```

Numbers force ordering and make taxonomy questions ("does this go in 03 or 06?") explicit.

## Per-folder conventions

### 00-org

Mission docs, governance, this `.github` repo's authoritative copy if you keep one. Rarely changes.

### 01-meetings

```
01-meetings/
└── YYYY-MM-DD-<type>/
    ├── agenda.md
    ├── raw-notes.md
    ├── decisions.md
    ├── action-items.md
    └── recording.md              # recording link or publishing status
```

Types: `weekly`, `monthly`, `quarterly`, `partner-X`, `workshop`.

### 02-grants

```
02-grants/
├── octant/
│   ├── epoch-5/
│   └── epoch-6/
├── gitcoin/
├── giveth/
├── nlnet/
└── _shared-language.md       # mission language reused across applications
```

`_shared-language.md` is the canonical positioning copy — pulls from the [grant-application routine](./grant-application.md).

### 03-projects

One subfolder per first-party project. Mirrors the GitHub org.

```
03-projects/
├── green-goods/
├── coop/
├── cookie-jar/
└── network-website/
```

Each can have its own internal structure; common pattern: `briefs/`, `designs/`, `research/`, `decisions/`.

### 04-partners

One subfolder per active partner. Closed/dormant partners move to `99-archive/04-partners/`.

### 05-treasury

```
05-treasury/
├── monthly-reports/
├── payouts/
└── multisig-records/
```

Most files here are read-only mirrors of on-chain or on-platform records. Don't make this the source of truth — it's a working copy.

### 06-design

```
06-design/
├── brand/                    # logos, color palettes, typography
├── references/               # screenshots, inspiration, comparable products
└── per-project/              # links to each project's Figma
```

### 07-workshops

```
07-workshops/
└── YYYY-MM-DD-<topic>/
    ├── slides.pdf
    ├── repo-link.md
    └── recording-link.md
```

### 99-archive

Things we keep but don't actively use. Move here rather than deleting. Honest deletion is fine when something is truly noise.

## Sorting flow

When you encounter an unsorted file:

1. **Identify the type** — meeting notes? Grant draft? Design file? Partner doc?
2. **Find the right folder** — use the numbered taxonomy.
3. **Check naming** — does it follow the folder's convention? Rename if not.
4. **If you can't classify it** — that's a sign it doesn't belong in the shared Drive (probably personal). Either give it a clear classification or delete.

## Periodic cleanup

Quarterly:

- Move dormant partners and projects to archive
- Audit grant folders for closed-out applications
- Review 99-archive for things that can be honestly deleted
- Check that `_shared-language.md` reflects current guild positioning

This is best done as part of the [quarterly retro](./retro-cadence.md).

## Permissions

- **Default**: guild-member edit, public view (where applicable)
- **05-treasury**: stewards-only edit
- **04-partners**: edit limited to partner workstream leads
- **00-org foundational docs**: stewards-only edit, public view

## Common pitfalls

- **Top-level folder proliferation** — adding `08-something` is almost always a sign it belongs inside an existing folder.
- **Personal files in the shared Drive** — your project notes belong in your own Drive.
- **Links instead of files** — for grant deadlines or contracts, keep the actual file. Links rot.
- **Dropping unsorted files at root** — they accumulate. Sort weekly.

## See also

- [meeting-notes.md](./meeting-notes.md)
- [grant-application.md](./grant-application.md)
