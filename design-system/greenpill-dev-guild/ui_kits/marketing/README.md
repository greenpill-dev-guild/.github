# Marketing UI kit

A high-fidelity recreation of the Greenpill Dev Guild marketing surface — the kind of single-page site or microsite that introduces the Guild, sells services, lists the stack, and invites people to join the fellowship.

## What's here

`index.html` is the live, navigable demo. Sections in order:

1. **Sticky nav** — pill-mark lockup, primary `Take the Greenpill` CTA.
2. **Hero** — Forest Pulse gradient + pill-watermark, glowing pill-mark, two-CTA stack.
3. **Stats strip** — high-contrast `#0F1F0F` band, Spring Green numerals.
4. **Services grid** — 3×2 dark service cards on pill-watermark, each with a glowing badge disc.
5. **Stack** — light parchment section with the 4-layer Ethereum stack (App / Social / Protocol / Blockchain) and annotations.
6. **The Quest / fantasy map** — dark section with the Capital Journey illustration framed in parchment, and the role-tag legend.
7. **Partners grid** — 4-up parchment cards.
8. **Closing CTA** — Forest Pulse gradient with display-xl "Take the Greenpill."
9. **Footer** — `#0F1F0F`, JetBrains Mono legal line.

## Components used

- `btn-primary` (pill, glow on dark) and `btn-secondary` (outline, Spring Green border)
- `service-card` (dark `#254D32` card with glow disc)
- `partner` (light card with Spring Green badge placeholder)
- `layer` (4 stack-layer variants)
- `role-tag` (Steward · Lead · Contributor)
- `disc` (64px Spring Green badge with line icon)

All tokens come from `../../colors_and_type.css`. Lucide-style line icons are inlined as SVG inside discs.

## Caveats

- Partner wordmarks are placeholder (Spring Green badge + plain name). When real partner logos are produced, swap the `<div class="badge">` for an `<img>`.
- The fellowship section uses the single supplied `capital-journey-map.png`. Other illustration vignettes need to be commissioned.
