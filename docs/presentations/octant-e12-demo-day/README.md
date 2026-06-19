# Greenpill Dev Guild · Octant Epoch 12 Demo Day deck

A 16-slide, roughly 5-minute talk deck. Built on the **Greenpill Dev Guild design system** (`colors_and_type.css` plus the `deck-stage.js` web component, both copied from the exported system), so it stays on-brand: forest ground, spring-green accent, Space Grotesk and Satoshi type, the pill mark.

## Run it

- **Easiest:** double-click `index.html` (opens in your browser via `file://`). Everything is local except the fonts, which load from Google Fonts and Fontshare, so be online the first time or vendor the fonts (see below).
- **Served (recommended for presenting):** from this folder run `python3 -m http.server 8099`, then open `http://localhost:8099/index.html`.

The deck auto-scales to any screen and letterboxes, so it is fine for screen-share or a projector at any resolution.

## Present

Keyboard:

| Key | Action |
|---|---|
| `→` `Space` `PgDn` | next slide |
| `←` `PgUp` | previous slide |
| `Home` / `End` | first / last |
| `1`–`9`, `0` | jump to slide |
| `R` | reset to slide 1 |
| `N` | toggle the presenter notes panel |
| `F` | fullscreen |

Clicking anywhere also advances. The bottom-center control bar appears on mouse move.

### Speaker notes and timer

Press **`N`** for the presenter panel (bottom-left): the current slide's note, the **next slide's label**, and an **elapsed timer**. The timer starts on your first advance and turns amber at **4:30** and red at **5:00** to keep you inside the 5-minute budget. Notes live in the `#speaker-notes` JSON block inside `index.html`; edit them there.

> The panel renders in the deck window, so it shows on a shared screen while toggled on. Use it during rehearsal, or glance and toggle off. A separate-window private presenter view can be added on request.

## Export to PDF

`Cmd/Ctrl-P`, then **Save as PDF**. The engine paginates one slide per landscape page at 1920×1080 and forces all animated content visible for print. Set margins to **None** and enable **Background graphics** in the print dialog. Confirm it produces **16 pages**.

## Swap in your media

All photos and web assets are **labeled placeholders** that show a dashed box until you drop the real file at the named path, so the deck is fully presentable before you add any of them. See `NEEDS_MEDIA.md` for the exact list. In short:

- **Your photos** go in `assets/photos/` (TAS hub, Omo Yoruba, community). Filenames appear on each placeholder.
- **Web-sourced** go in `assets/sourced/` (marathon GIF, the five ecosystem logos). The Green Goods product screen on slide 6 is already filled from the repo.
- **Codex-generated textures** go in `assets/generated/` (optional atmospheric frames; see `NEEDS_MEDIA.md`).

Any missing file simply keeps its placeholder. Nothing breaks.

## What's in here

```
index.html            the deck (16 slides, inline SVG diagrams, speaker notes, presenter overlay)
deck-stage.js         GPDG deck engine (nav, auto-scale, print pagination), copied from the design system
colors_and_type.css   GPDG tokens, type, gradients, glow, copied from the design system
assets/brand/         pill mark, horizontal logo, Capital Journey map (from the design system)
assets/photos/        your photos (placeholders until added)
assets/sourced/        web assets plus the Green Goods product screen
assets/generated/      optional Codex raster frames
NEEDS_MEDIA.md        running checklist of everything that needs your action
```

## Offline and vendoring fonts (optional)

The deck pulls Space Grotesk, Satoshi, and JetBrains Mono from CDNs. To present with no internet, download the woff2 files, drop them in a `fonts/` folder, and replace the three `@import` lines at the top of `colors_and_type.css` with local `@font-face` rules. System fallbacks (system sans, serif, mono) keep it readable either way.

## Design system source

`../../../design-system/greenpill-dev-guild/`: brand bible (`README.md`), tokens (`colors_and_type.css`), component previews, and the `slides/` reference deck.
