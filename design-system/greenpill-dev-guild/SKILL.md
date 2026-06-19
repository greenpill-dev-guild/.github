---
name: greenpill-dev-guild-design
description: Use this skill to generate well-branded interfaces and assets for Greenpill Dev Guild, a Web3 ReFi fellowship — pitch decks, microsites, one-pagers, social graphics, prototypes, mocks. Contains brand guidelines, color and type tokens, fonts, hand-drawn illustration motifs, the pill mark, and ready-made HTML/CSS components for slides and marketing surfaces.
user-invocable: true
---

# Greenpill Dev Guild — Design skill

Read **`README.md`** in this skill first — it covers brand context, voice & tone, visual foundations, iconography, and where every file lives. Then explore:

- **`colors_and_type.css`** — drop-in CSS variables, type classes, gradients, glow tokens.
- **`assets/`** — pill mark (Spring & Creme variants), horizontal lockup, the Capital Journey fantasy map, brand-guidelines reference.
- **`preview/`** — small swatch / specimen / component cards.
- **`slides/index.html`** — sample 7-slide pitch deck (built on `deck-stage.js`).
- **`ui_kits/marketing/index.html`** — full-page marketing-site recreation.

## When invoked

If creating a **visual artifact** (slide, mock, throwaway prototype, social graphic, microsite section), copy the assets you need out of `assets/`, link `colors_and_type.css`, and produce a static HTML file the user can view. Match the brand vocabulary:

- Pill is the hero shape. Use `border-radius: 999px` everywhere it makes sense.
- Spring Green on Cal Poly Green is the signature pair. Don't dilute it with extra accents.
- Glow only on dark backgrounds. Never on parchment.
- Hand-drawn fantasy-map illustration where storytelling is needed; don't try to draw it yourself with SVG — reference `assets/capital-journey-map.png` or ask the user for source illustrations.
- Voice is mythic-but-modern: *fellowship, guild, quest, stewards, switched on for change, take the Greenpill*.

If working in **production code**, copy assets and tokens into the project, and act as an expert in the brand — answering "what color/font/component should I use here?" using the rules in `README.md`.

If invoked **without specific guidance**, ask the user what they want to build, ask 4–6 clarifying questions (audience, format, length/scope, tone, variations), then act as an expert designer outputting HTML or production code.
