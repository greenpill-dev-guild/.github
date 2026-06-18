# Greenpill Dev Guild — Design System

A fellowship-of-builders design system for **Greenpill Dev Guild**, a Web3 guild working in service of Regenerative Finance (ReFi). The brand fuses **mythic Lord-of-the-Rings storytelling** — fellowships, guilds, journeys, stewards, the Shire of our regenerative journey — with **crisp Web3-native design**: vibrant Spring Green as a "switched-on" signal, deep forest green as the steady ground, and hand-drawn fantasy-map illustration as connective tissue.

---

## Who they are

Greenpill Dev Guild is the technical and creative wing supporting Greenpill Chapters, regen communities, and aligned partners across the Ethereum ecosystem and beyond. Where most dev shops sell hours, the Guild offers **fellowship**: mission-aligned stewards, leads, and contributors who help partners go from spark to systems.

**What they do**
- Regenerative tooling — open-source apps and protocols for ReFi.
- Product feedback & tech support, from people who run the rails.
- Workshops on impact reporting, capital formation, allocation, coordination.
- Grant round design & operations, including Ethereum staking for public goods.
- Design & engineering services — UI/UX, graphic design, Web3 consultation.

**Where they walk** — Ethereum, Blockchain Space (Celo, Optimism, Arbitrum, Octant, VeChain, Solana, Hedera), Traditional Markets (NGOs, Non-Profits, Governments).

**Branches** — Community · Growth · Product · Engineering.

**Roles** — **Stewards** (Spring Green tag) · **Leads** (Creme tag) · **Contributors** (Alice Blue tag).

**Projects across the Ethereum stack**
- **Green Goods** — App layer
- **GreenWill** — Social layer
- **Allo Alliance** — Protocol layer
- **Public Good Staking** — Blockchain layer

**Partners** — Gardens · Flowstate · DAO Masons · Hypercerts · Greenpill Network · CFCE · Cloudlines · Greenpill Brasil · Greenpill Nigeria.

---

## Sources

- **Branding v2.fig** — primary brand book (mounted as VFS). Focused pages: `/Brand-Book/Brand-Identity`, `/Brand-Book`, `/Brand-Book/Google-Drive`, `/Brand-Book/ZGreenpill-Dev-Guild-Brand-Guide-Presentation-01`.
- **Marketing v2.fig** — pitch deck reference (`/Pitch-Deck`).
- **Brand book PDF** (linked in figma): https://drive.google.com/drive/folders/1OFZHu3Ihhgs3IaaCBuf6orAgQwz6EsWp?usp=drive_link
- **User uploads** — `logo (1).png`, `pill logo lime green.png`, `Group 1000004518.png`, `gpdg-graphic-capital-formation.png` (the Capital Journey fantasy-map graphic).

---

## Content fundamentals — voice & tone

The Guild speaks **mythic-but-modern**. Tolkien cadence and Web3 precision in the same sentence.

### Pronouns & address
- **"We" and "the fellowship"** — never corporate "you." We address ourselves as a collective walking a road.
- "Our quest", "our partners", "our chapters" — possessive plural is the default.

### Casing
- **Title Case** for headings, slide titles, project names.
- **UPPERCASE** with letter-spacing for eyebrows ("BRAND GUIDELINES", "OUR GUILD", "CHAPTER 02") and role tags ("STEWARD", "LEAD").
- **Sentence case** for body copy, captions, button labels.

### Vocabulary (use)
- Mythic — *fellowship · guild · quest · journey · stewards · leads · builders · the Shire of our regenerative journey · ancient traditions meeting modern innovation · forging symbiotic pathways · tending the steady flame of governance · switched on for change · take the Greenpill.*
- Web3-crisp — *ReFi · public goods · capital allocation · impact reporting · grant rounds · Allo · retroactive funding · staking · hypercerts · coordination.*

The contrast between these two registers IS the brand. Don't soften it.

### Vocabulary (avoid)
- No "you" addressing customers.
- No Tolkien parody — no "thou", no Elvish, no faux-archaic spelling. Mythic, not costume.
- No corporate filler — "leverage", "synergy", "best-in-class", "stakeholders", "solutions provider".

### Sentence shape
Short, declarative, occasionally lyrical. Open with a verb when you can. One idea per sentence. Long paragraphs become a sequence of short ones.

### Examples
- *"The fellowship gathers where ancient traditions meet modern innovation — and forges the pathways regeneration needs."*
- *"A quest across diverse lands: from the Shire of Ethereum to the realms of Celo, Optimism, and beyond."*
- *"We tend the steady flame of governance, so the round runs true."*
- *"Take the Greenpill. Switch on for change."*

### Emoji
Generally **avoided** in formal collateral (decks, brand book, partner-facing one-pagers). Acceptable in community-facing social posts and Discord. Never decorative; use sparingly.

### Tone dials
Confident **8/10** · Communal **9/10** · Warm **8/10** · Playful **5/10** · Formal **3/10**.

---

## Visual foundations

### Colors
- **Spring Green `#C2FF1A`** — the pill, the "switched-on" signal. Use for headlines on dark, primary buttons, badge discs, accents, glow. Note: figma's most-used green is actually `#A8FF00` (a punchier yellow-green) — both are in scope as `--color-spring-green` and `--color-spring-green-bright`.
- **Cal Poly Green `#1F3D1F`** / **Forest Deep `#254D32`** — the dark ground. Default dark backgrounds, illustration linework, text on light. Forest-deep `#254D32` is the figma's most-used surface tone; treat them as a pair, with `#1F3D1F` reserved for the most authoritative chrome and `#254D32` for general dark surfaces.
- **Creme `#FCECA6`** — warm parchment. Map fills, secondary surfaces, **Lead** role tag.
- **Mint Green `#B1FDEB`** · **Alice Blue `#DCEDFF`** · **Cryola `#FF6978`** — the pastel "land" colors.
- **Parchment `#FFF8E1`** — page background for fantasy-map slides and light decks.
- **Ink `#0F1F0F`** — body text on light surfaces.
- **Steady Flame `#7DC400`** — AA-safe darker spring green for green text on light.

### Gradients
- **Daybreak** Creme → Spring Green
- **Forest Pulse** Cal Poly Green → Spring Green (the signature)
- **Coral Tide** Cryola → Mint Green
- **Sky Shore** Alice Blue → Mint Green

### Typography
- **Space Grotesk** (Google Fonts, weights 500/600/700) — display, headlines, eyebrows, tags. Bold mythic talking.
- **Satoshi** (Fontshare, 400/500/700) — body, UI, captions. Clear modern speaking.
- **JetBrains Mono** — code, technical specs, address strings, hashes, the brand-book "download" callouts.
- **Clash Display** appears in the figma as an alternate display face on a few hero moments — it's a Fontshare family and is loaded in `colors_and_type.css` for those rare moments. Default is Space Grotesk.

**Rules**: never use Space Grotesk under 12px. Never use Satoshi above 28px. `text-wrap: balance` on `display-*` and `h1`–`h2`.

### Spacing & rhythm
8px base. Card padding default 32px (`--space-6`); dark hero cards 48px. Eyebrow→title 12px, title→body 24px, body→CTA 32px. Section gaps 96px on deck, 64px on web.

### Backgrounds
- **Forest Pulse gradient** — primary hero background.
- **Pill watermark pattern** — dark Cal Poly Green with low-opacity (5–8%) Spring Green capsules tiled on a 12° diagonal. Adds "switched-on" texture on dark hero blocks.
- **Parchment flat** — light surface, warm `#FFF8E1`.
- **Hand-drawn fantasy-map vignettes** — parchment-filled containers with Cal Poly Green ink-line illustration and pastel-fill "lands" (creme, mint, alice blue, cryola at 60–80% opacity).
- **Full-bleed imagery** is reserved for hero moments and fantasy-map slides; inner content always sits on flat parchment or flat forest.

### Shapes & radius
- **Pill `999px`** — the brand's hero shape: buttons, role tags, badge discs, callouts. Always preferred over rectangular CTAs.
- **xl `28px`** — full-bleed map containers, hero blocks.
- **lg `20px`** — cards, slide blocks.
- **md `14px`** — stack-diagram layers, partner-grid items.
- **sm `8px`** — inputs, inline chips.

### Elevation
Restrained drop-shadows (`elev-1`/`elev-2`/`elev-3`). Real depth comes from **glow** — Spring Green `glow-spring-sm/md/lg` reserved for elements on dark backgrounds. Never glow on parchment.

### Borders
1.5px Cal Poly Green outlines on illustrative containers and ink-line elements. UI cards usually unbordered; rely on background contrast or `elev-1`. Buttons: `button-secondary` is the only bordered button (1px Spring Green).

### Hover & press states
- **Hover** — primary button lightens to `--color-primary-container` (`#E5FF8A`); ghost/secondary buttons fade in a 12% Spring Green wash; cards lift with `elev-2`. All transitions `220ms` `--ease-out`.
- **Press** — 96–98% scale; opacity drop to 0.92 on text; brief.

### Animation
- Subtle, regenerative, never extractive. 220ms ease-out is the default.
- Glow pulses on the pill mark are slow (~4s) and gentle. Always provide a `prefers-reduced-motion` fallback that holds the brightest frame.
- No bouncy spring physics. No flashy reveals.

### Transparency & blur
- Watermark patterns at 5–8% opacity are the main use of transparency.
- Avoid frosted/blurred glass — that's not the brand's vocabulary. Solid surfaces preferred.

### Imagery style
- **Hand-drawn ink-line on parchment** is the dominant illustration style. Pine forests, castles, mountains, rivers, banners and scrolls.
- **Pastel-filled "lands"** outlined in dark forest green.
- Photography is rare; when used, warm-toned and slightly desaturated to sit beside parchment.
- **Never** mix photography with the fantasy-map style on the same surface.

---

## Iconography

The Guild uses **bold simple line icons, 2px stroke, rounded caps and joins**, drawn on a 24px grid. Icons are always **Cal Poly Green** and almost always live inside a **Spring Green badge disc** (a 64px filled circle). On dark surfaces the disc gets `glow-spring-sm`.

Recommended set: `forest`, `castle`, `mountain`, `river`, `scroll`, `banner`, `compass`, `tree-of-fellowship`, `bridge`, `seedling`, `flame`, `pill`, `key`, `coin`, `handshake`, `globe`.

Where the codebase doesn't ship a custom icon set, this design system uses **[Lucide](https://lucide.dev)** via CDN as the closest match (same 2px stroke, rounded caps, similar geometric weight). Substitution is flagged as such — when proper hand-drawn icons are produced, they should replace Lucide one-for-one.

```html
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="leaf"></i>
<script>lucide.createIcons();</script>
```

**Emoji** — avoided in design surfaces. **Unicode characters** — rare; only the section bullets `•` and arrows `→` are used in body copy.

---

## Index

```
Greenpill-Dev-Guild-Design-System/
├── README.md                    ← you are here
├── SKILL.md                     ← Agent Skills entry point
├── colors_and_type.css          ← all CSS variables, type classes, gradients
├── assets/                      ← logos, pill marks, brand graphics
│   ├── logo-horizontal-spring.png
│   ├── pill-mark-spring.png
│   ├── pill-mark-creme.png
│   ├── capital-journey-map.png  ← the hand-drawn fantasy map
│   └── brand-guidelines-page.png
├── preview/                     ← Design System tab cards
├── slides/                      ← pitch-deck slide samples
│   └── index.html
└── ui_kits/
    └── marketing/               ← marketing-website UI kit
        ├── index.html
        └── components/
```

### Where to look first
- **Building a deck?** → `slides/index.html` for slide layouts, `colors_and_type.css` for tokens.
- **Building a microsite or landing page?** → `ui_kits/marketing/index.html`.
- **Need the pill mark or logo?** → `assets/`.
- **Just want tokens?** → `colors_and_type.css`.

---

## Caveats & flags

- **Font substitution** — Satoshi is loaded from Fontshare CDN. If the user has licensed `.woff2` files, drop them into `fonts/` and switch the `@font-face` rule in `colors_and_type.css`.
- **Iconography** — Lucide is used as a substitute for the (yet unbuilt) hand-drawn line-icon set. Flagged.
- **Hand-drawn illustrations** — only the source-supplied `capital-journey-map.png` is included. Other map vignettes need to be commissioned; placeholders are used in slides.
