# NEEDS_MEDIA: what needs your action

The deck is complete and presentable right now. Every item below is a **labeled placeholder** that shows a dashed box until you drop the real file at the exact path. Nothing breaks if you present without them.

---

## 1. Photos you will provide

Drop these into `assets/photos/` with these exact filenames (the placeholders show the path on-slide):

| Path | Slide(s) | What goes there |
|---|---|---|
| `assets/photos/awka-hub.jpg` | 8 (the bridge) | Tech and Sun hub in Awka: the container hub or a wide establishing shot |
| `assets/photos/tas-hub-build.jpg` | 9 (Tech and Sun) | TAS build: container, solar install, Starlink dish, or students at work |
| `assets/photos/odunde-masquerade.jpg` | 8 (bridge) and 10 (Omo Yoruba) | Omo Yoruba: Egungun masquerade, GanGan procession, kids zone, or banners |
| `assets/photos/community.jpg` | 15 (close) | A community group photo (sits faintly behind "Let's Fucking Grow") |

> Note: the 6 images you pasted in chat arrived as broken file-icons (the system captured generic JPEG thumbnails, not the photos), so none are embedded. Save the originals to the paths above.

Landscape 16:9 crops look best on slides 8, 9, and 15. Slide 10 is full-bleed, so any orientation works (it fills and is scrimmed).

---

## 2. Web-sourced assets

Drop into `assets/sourced/`, or send me a URL and I can fetch:

| Path | Slide | Find it |
|---|---|---|
| `marathon-water-station.gif` | 13 | Search: "marathon water station volunteer handing cup to runner, GIF, warm documentary tone." Full-bleed; muted and warm reads best behind the headline. |
| `logo-eas.svg` | 14 | Ethereum Attestation Service brand mark (attest.org press kit). |
| `logo-octant.svg` | 14 | Octant logo (octant.app or Golem brand assets). |
| `logo-hypercerts.svg` | 14 | Hypercerts logo (hypercerts.org). |
| `logo-solidity.svg` | 14 | Solidity logo (soliditylang.org brand). |
| `logo-dappnode.svg` | 14 | Dappnode logo (dappnode.com press). |

The logos render as light marks on forest. SVG preferred, PNG fine. Each shows a text placeholder until added.

**Already filled (no action needed):** slide 6's Green Goods product screen uses `assets/sourced/greengoods-app-mock.png` from the repo. Swap for a fresher `greengoods.app/impact` screenshot if you want.

**Optional:** slide 1 currently uses an inline SVG mesh (no GIF needed). If you would rather a dial-up modem GIF there, drop `assets/sourced/dialup.gif` and tell me, and I will wire it in.

---

## 3. Confirmations for me

1. **Codex image command.** To generate the 5 atmospheric raster frames (`cover-bg.png` first, then `infrastructure-bg`, `tagline-bg`, `problem-texture`, `warm-regen-texture` into `assets/generated/`). The Codex binary is at `/Applications/Codex.app/Contents/Resources/codex`, but the documented invocations are code-only and the `sora` image skill in `~/.codex/config.toml` is disabled, so send me the exact image-generation command and I will run the prompts you provided. The deck is complete without these; they are optional polish.
2. **Image background hex.** OK to change the shared style block in your Codex prompts doc from near-black `#171717` to Cal Poly Green `#1F3D1F`, so generated frames match the deck's forest ground? (Spring-green accent `#C2FF1A` unchanged.)
3. **Garden count refresh.** Slide 7 says "14 gardens" with your curated list. The repo's live snapshot shows the count drifts (16 to 18). Re-pull the current number and list the morning of the talk if you want it exact; tell me and I will update the pins and subhead.

---

## Known-good as-is

- All 16 slides render at 1920×1080 with no overflow or overlap (verified in browser).
- Keyboard nav, presenter notes (`N`) with timer and next-slide, and reduced-motion handling all work.
- PDF export via `Cmd/Ctrl-P`, then Save as PDF (margins None, Background graphics on) gives 16 pages. Do a quick preview before the talk.
