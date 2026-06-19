from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageSequence
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "octant-e12-demo-day.pdf"
TMP = ROOT / "tmp" / "pdfs"

PAGE_W = 1920
PAGE_H = 1080
PDF_W = 960
PDF_H = 540
SCALE = PDF_W / PAGE_W
TOTAL_PAGES = 15

FOREST = HexColor("#1F3D1F")
FOREST_DEEP = HexColor("#254D32")
INK = HexColor("#0F1F0F")
PARCHMENT = HexColor("#FFF8E1")
CREME = HexColor("#FCECA6")
SPRING = HexColor("#C2FF1A")
MINT = HexColor("#B1FDEB")
ALICE = HexColor("#DCEDFF")
RED = HexColor("#FF6978")
FOG = HexColor("#E8EFE3")
STEADY = HexColor("#7DC400")

FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_OBLIQUE = "Helvetica-Oblique"


def asset(path: str) -> Path:
    return ROOT / path


def ensure_dirs() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)


def first_frame(path: Path, name: str) -> Path:
    out = TMP / f"{name}.png"
    if out.exists() and out.stat().st_mtime >= path.stat().st_mtime:
        return out
    with Image.open(path) as im:
        frame = next(ImageSequence.Iterator(im)).convert("RGBA")
        frame.save(out)
    return out


def crop_cover(path: Path, name: str, width: int, height: int) -> Path:
    out = TMP / f"{name}-{width}x{height}.png"
    if out.exists() and out.stat().st_mtime >= path.stat().st_mtime:
        return out
    with Image.open(path) as im:
        im = im.convert("RGB")
        src_w, src_h = im.size
        target_ratio = width / height
        src_ratio = src_w / src_h
        if src_ratio > target_ratio:
            new_w = int(src_h * target_ratio)
            left = (src_w - new_w) // 2
            box = (left, 0, left + new_w, src_h)
        else:
            new_h = int(src_w / target_ratio)
            top = (src_h - new_h) // 2
            box = (0, top, src_w, top + new_h)
        im = im.crop(box).resize((width, height), Image.Resampling.LANCZOS)
        im.save(out)
    return out


def begin_page(c: canvas.Canvas) -> None:
    c.saveState()
    c.scale(SCALE, SCALE)
    c.setFillColor(PARCHMENT)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    draw_watermark(c)


def end_page(c: canvas.Canvas, page: int, total: int = TOTAL_PAGES, show_number: bool = True) -> None:
    draw_brand(c)
    if show_number:
        c.setFont(FONT_BOLD, 22)
        c.setFillColor(HexColor("#6D7B54"))
        c.drawRightString(PAGE_W - 96, 70, f"{page:02d} / {total:02d}")
    c.restoreState()
    c.showPage()


def draw_watermark(c: canvas.Canvas) -> None:
    c.saveState()
    c.setStrokeColor(HexColor("#F4E7B3"))
    c.setLineWidth(3)
    try:
        c.setStrokeAlpha(0.38)
        c.setFillAlpha(0.16)
    except Exception:
        pass
    for y in range(120, PAGE_H, 180):
        for x in range(-80, PAGE_W + 160, 260):
            c.saveState()
            c.translate(x, y)
            c.rotate(42)
            c.roundRect(-45, -110, 90, 220, 45, stroke=1, fill=0)
            c.circle(0, -55, 26, stroke=0, fill=1)
            c.restoreState()
    try:
        c.setStrokeAlpha(1)
        c.setFillAlpha(1)
    except Exception:
        pass
    c.restoreState()


def draw_brand(c: canvas.Canvas) -> None:
    c.saveState()
    x = PAGE_W - 410
    y = PAGE_H - 92
    c.translate(x, y)
    c.rotate(20)
    c.setStrokeColor(FOREST)
    c.setLineWidth(6)
    c.roundRect(0, -42, 46, 84, 23, stroke=1, fill=0)
    c.setFillColor(FOREST)
    c.circle(23, 21, 13, stroke=0, fill=1)
    c.line(4, -5, 42, -5)
    c.restoreState()
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 28)
    c.drawString(PAGE_W - 332, PAGE_H - 82, "Greenpill Dev Guild")


def eyebrow(c: canvas.Canvas, text: str, x: int = 96, y: int = 1000) -> None:
    c.setFont(FONT_BOLD, 20)
    c.setFillColor(FOREST_DEEP)
    c.drawString(x, y, text.upper())


def title(c: canvas.Canvas, text: str, x: int, y: int, width: int, size: int = 96, leading: int | None = None) -> int:
    return text_box(c, text, x, y, width, FONT_BOLD, size, FOREST, leading or int(size * 1.05))


def body(c: canvas.Canvas, text: str, x: int, y: int, width: int, size: int = 38, leading: int | None = None) -> int:
    return text_box(c, text, x, y, width, FONT, size, INK, leading or int(size * 1.34))


def small_caps(c: canvas.Canvas, text: str, x: int, y: int, width: int = 720) -> int:
    return text_box(c, text.upper(), x, y, width, FONT_BOLD, 22, HexColor("#66724D"), 32)


def text_box(
    c: canvas.Canvas,
    text: str,
    x: int,
    y: int,
    width: int,
    font: str,
    size: int,
    color,
    leading: int,
    max_lines: int | None = None,
) -> int:
    c.setFillColor(color)
    c.setFont(font, size)
    lines: list[str] = []
    for part in text.split("\n"):
        if not part:
            lines.append("")
            continue
        words = part.split()
        line = ""
        for word in words:
            trial = word if not line else f"{line} {word}"
            if stringWidth(trial, font, size) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    if max_lines is not None:
        lines = lines[:max_lines]
    for idx, line in enumerate(lines):
        c.drawString(x, y - idx * leading, line)
    return y - len(lines) * leading


def draw_image_contain(c: canvas.Canvas, path: Path, x: int, y: int, w: int, h: int, mask: str | None = "auto") -> None:
    with Image.open(path) as im:
        iw, ih = im.size
    scale = min(w / iw, h / ih)
    dw = iw * scale
    dh = ih * scale
    c.drawImage(ImageReader(str(path)), x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, preserveAspectRatio=True, mask=mask)


def draw_image_fill(c: canvas.Canvas, path: Path, x: int, y: int, w: int, h: int, name: str) -> None:
    cropped = crop_cover(path, name, int(w), int(h))
    c.drawImage(ImageReader(str(cropped)), x, y, w, h, mask=None)


def rounded_panel(c: canvas.Canvas, x: int, y: int, w: int, h: int, fill, stroke=FOREST, radius: int = 26) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(4)
    c.roundRect(x, y, w, h, radius, stroke=1, fill=1)


def photo_card(c: canvas.Canvas, path: Path, x: int, y: int, w: int, h: int, caption: str, sub: str, name: str) -> None:
    rounded_panel(c, x, y, w, h, HexColor("#F7EFBF"), FOREST, 22)
    draw_image_fill(c, path, x + 12, y + 12, w - 24, h - 24, name)
    c.setFillColor(HexColor("#FCECA6"))
    c.roundRect(x + 34, y + 34, 430, 86, 18, stroke=0, fill=1)
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 31)
    c.drawString(x + 58, y + 82, caption)
    c.setFont(FONT, 22)
    c.drawString(x + 58, y + 52, sub)


def draw_pill(c: canvas.Canvas, x: int, y: int, w: int, h: int, text: str, fill=FOREST, text_color=PARCHMENT) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(FOREST)
    c.setLineWidth(3)
    c.roundRect(x, y, w, h, h / 2, stroke=1, fill=1)
    c.setFillColor(text_color)
    c.setFont(FONT_BOLD, 34)
    tw = stringWidth(text, FONT_BOLD, 34)
    c.drawString(x + (w - tw) / 2, y + h / 2 - 12, text)


def draw_disc_icon(c: canvas.Canvas, x: int, y: int, label: str, detail: str, fill) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(FOREST)
    c.setLineWidth(5)
    c.circle(x, y, 76, stroke=1, fill=1)
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 54)
    c.drawCentredString(x, y - 18, label[:1])
    c.setFont(FONT_BOLD, 32)
    c.drawCentredString(x, y - 128, label)
    c.setFont(FONT, 23)
    c.setFillColor(INK)
    c.drawCentredString(x, y - 162, detail)


def draw_rings(c: canvas.Canvas, cx: int, cy: int) -> None:
    rings = [
        (360, CREME, "GLOBAL FUNDERS"),
        (285, ALICE, "DIASPORA"),
        (210, MINT, "FRIENDS + FAMILY"),
        (135, SPRING, "COMMUNITY"),
    ]
    for radius, fill, label in rings:
        c.setFillColor(fill)
        c.setStrokeColor(FOREST)
        c.setLineWidth(5)
        c.circle(cx, cy, radius, stroke=1, fill=1)
        c.setFillColor(FOREST)
        c.setFont(FONT_BOLD, 30 if radius > 150 else 28)
        c.drawCentredString(cx, cy + radius - 58, label)
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 35)
    c.drawCentredString(cx, cy - 8, "LOCAL")
    c.drawCentredString(cx, cy - 48, "ENDOWMENT")
    c.setStrokeColor(FOREST)
    c.setLineWidth(5)
    c.line(cx - 26, cy - 72, cx + 26, cy - 72)


def slide_cover(c: canvas.Canvas) -> None:
    begin_page(c)
    c.setFont(FONT_BOLD, 132)
    c.setFillColor(FOREST)
    c.drawString(112, 770, "Greenpill")
    c.drawString(112, 638, "Dev")
    c.setFillColor(FOREST_DEEP)
    c.drawString(360, 638, "Guild")
    body(c, "Abstracting Ethereum through Trust, Relationships, Culture and Ownership.", 112, 535, 640, 42, 56)
    small_caps(c, "Octant Epoch 12 Demo Day", 112, 390)
    draw_image_contain(c, asset("assets/generated/octant-cover-tree.png"), 920, 70, 880, 930)
    end_page(c, 1, show_number=False)


def slide_infrastructure(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Unseen Layer")
    title(c, "Ethereum is infrastructure. Like the Internet.", 96, 790, 780, 94)
    body(c, "Protocols you never see, holding up everything you do.", 100, 500, 690, 44, 58)
    img = first_frame(asset("assets/sourced/dialup.gif"), "dialup")
    rounded_panel(c, 1040, 250, 700, 430, CREME)
    draw_image_fill(c, img, 1060, 270, 660, 390, "dialup-fill")
    small_caps(c, "Nobody fell in love with the protocol", 1080, 205, 650)
    end_page(c, 2)


def slide_people(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "What Actually Grew")
    title(c, "What grew the Internet wasn't the protocol. It was people.", 96, 820, 1180, 86)
    y = 390
    draw_disc_icon(c, 330, y, "E-commerce", "Buying and selling, together.", CREME)
    draw_disc_icon(c, 750, y, "Social networks", "Finding each other.", MINT)
    draw_disc_icon(c, 1170, y, "Forums", "Gathering to talk.", ALICE)
    draw_disc_icon(c, 1590, y, "Messaging", "Staying in touch.", SPRING)
    end_page(c, 3)


def slide_thesis(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Fellowship")
    rounded_panel(c, 250, 315, 1420, 350, SPRING, FOREST, 40)
    text_box(c, "Today, we're not here to focus on protocols.", 350, 525, 1220, FONT_BOLD, 86, FOREST, 96)
    end_page(c, 4)


def slide_problem(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Problem")
    title(c, "Impact lives in silos. Funding lives far away.", 96, 795, 620, 76, 82)
    body(c, "Proof of real work sits in someone else's database, hard to see or trust.", 100, 520, 650, 34, 48)
    body(c, "Capital struggles to reach growing economies like Nigeria: high fees, slow rails.", 100, 380, 650, 34, 48)
    body(c, "And when it arrives it rarely flows transparently, which raises risk and deters investment.", 100, 240, 650, 34, 48)
    draw_image_contain(c, asset("assets/generated/octant-funding-problem.png"), 760, 150, 1030, 735)
    end_page(c, 5)


def slide_staking(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "Layer 1 - The Ground - Roadmap")
    title(c, "Public Goods Staking Protocol.", 300, 880, 1320, 72, 80)
    body(
        c,
        "Community-owned infrastructure. Squads run the hardware together with Obol and Dappnode. Staking rewards flow into a community endowment, built on Octant vaults and Lido.",
        330,
        780,
        1260,
        31,
        43,
    )
    draw_image_contain(c, asset("assets/generated/octant-staking-flow.png"), 250, 60, 600, 540)
    photo_card(c, asset("assets/photos/obol-node.webp"), 1040, 85, 560, 535, "Squad staking node", "Obol + Dappnode", "obol-node")
    end_page(c, 6)


def slide_green_goods(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "Layer 2 - The Front Door - Live")
    title(c, "Green Goods.", 96, 820, 620, 88)
    body(c, "Impact reporting anyone can use. Real regenerative work becomes verified, funder-ready proof, tied to a local endowment the community controls.", 100, 660, 650, 38, 52)
    body(c, "Four domains: agroforestry, waste, solar, and education. 14 gardens across five continents.", 100, 440, 650, 38, 52)
    draw_pill(c, 100, 250, 515, 72, "No wallet. Offline. Local.")
    rounded_panel(c, 880, 150, 330, 720, FOG, FOREST, 32)
    draw_image_fill(c, asset("assets/sourced/greengoods-home.webp"), 902, 172, 286, 676, "gg-home")
    rounded_panel(c, 1270, 150, 330, 720, FOG, FOREST, 32)
    draw_image_fill(c, asset("assets/sourced/greengoods-action.webp"), 1292, 172, 286, 676, "gg-action")
    end_page(c, 7)


def slide_bridge(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Bridge")
    title(c, "Where it becomes real.", 530, 910, 860, 66, 74)
    body(c, "Tech and Sun in Nigeria. Omo Yoruba in California. Green Goods is the bridge.", 440, 810, 1040, 40, 52)
    photo_card(c, asset("assets/photos/awka-hub.jpg"), 140, 165, 690, 560, "Tech and Sun", "Awka, Nigeria", "awka-hub")
    photo_card(c, asset("assets/photos/omo-yoruba-bridge.jpg"), 1090, 165, 690, 560, "Omo Yoruba", "Southern California", "omo-bridge")
    c.setStrokeColor(STEADY)
    c.setLineWidth(8)
    c.setDash(14, 14)
    c.line(835, 445, 1085, 445)
    c.setDash()
    draw_pill(c, 760, 395, 400, 92, "Green Goods", SPRING, FOREST)
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 25)
    c.drawCentredString(960, 360, "the bridge")
    end_page(c, 8)


def slide_tech_sun(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "In the Field - Nigeria")
    photo_card(c, asset("assets/photos/tas-hub-build.jpg"), 110, 145, 790, 705, "The hub at Awka", "Container, solar, Starlink, students", "tas-hub")
    title(c, "Tech and Sun: power, internet, and a place to build.", 990, 780, 710, 68, 75)
    draw_pill(c, 995, 480, 290, 64, "Solar power", CREME, FOREST)
    draw_pill(c, 1310, 480, 330, 64, "Starlink internet", MINT, FOREST)
    draw_pill(c, 995, 390, 560, 64, "Ethereum staking infrastructure", ALICE, FOREST)
    body(c, "A live hub in Awka, near UNIZIK, owned and run by the community. Enugu, Abuja and Lagos next.", 995, 285, 690, 35, 48)
    end_page(c, 9)


def slide_omo(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Diaspora - California")
    title(c, "Omo Yoruba: keeping the culture alive.", 110, 790, 660, 72, 78)
    draw_pill(c, 115, 510, 425, 64, "Yoruba heritage", CREME, FOREST)
    draw_pill(c, 115, 425, 500, 64, "Cultural programming", MINT, FOREST)
    draw_pill(c, 115, 340, 545, 64, "A diaspora bridge home", ALICE, FOREST)
    body(c, "A Southern California community preserving Yoruba heritage, and a bridge for the diaspora to invest back home.", 115, 245, 620, 35, 48)
    photo_card(c, asset("assets/photos/odunde-masquerade.jpg"), 930, 140, 780, 720, "Omo Yoruba", "Egungun masquerade, procession, banners", "odunde")
    end_page(c, 10)


def slide_rings(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "Grassroots Growth")
    title(c, "Funding that starts at home.", 96, 790, 650, 78, 84)
    body(c, "Ownership stays with the community. Support flows in from the diaspora, friends and family connected to the land, and then from global funders.", 100, 560, 670, 38, 52)
    draw_rings(c, 1280, 520)
    end_page(c, 11)


def slide_flywheel(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "How It Compounds")
    title(c, "The diaspora flywheel.", 96, 790, 620, 82, 88)
    body(c, "Sponsorship to hubs to proof to capital to reputation, and around again.", 100, 555, 620, 40, 54)
    draw_image_contain(c, asset("assets/generated/octant-flywheel.png"), 740, 115, 1040, 820)
    end_page(c, 12)


def slide_marathon(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Long Game")
    title(c, "We are running a marathon. This Epoch is a water station.", 96, 795, 830, 78, 84)
    body(c, "Fuel for the road, not the finish line.", 100, 410, 620, 42, 58)
    img = first_frame(asset("assets/sourced/marathon-water-station.gif"), "marathon")
    photo_card(c, img, 1080, 180, 600, 620, "Marathon", "water-station handoff", "marathon-fill")
    end_page(c, 13)


def slide_ask(c: canvas.Canvas) -> None:
    begin_page(c)
    eyebrow(c, "The Ask")
    title(c, "Let's run it together.", 96, 815, 650, 82)
    body(
        c,
        "We are looking for partners, communities, and funders to build the plumbing of trust with us. Donors, your allocation this epoch funds the core team dedicating countless hours to this work.",
        100,
        650,
        720,
        36,
        50,
    )
    small_caps(c, "A few of the protocols we build upon, in this round with us", 100, 390, 780)
    labels = ["Ethereum Attestation Service", "Hypercerts", "Solidity", "Dappnode"]
    x = 100
    y = 300
    fills = [MINT, ALICE, CREME, SPRING]
    for i, label in enumerate(labels):
        w = int(stringWidth(label, FONT_BOLD, 34)) + 64
        draw_pill(c, x, y - (i // 2) * 84, w, 58, label, fills[i], FOREST)
        x += w + 24
        if i == 1:
            x = 100
    img = first_frame(asset("assets/sourced/run-together.gif"), "run-together")
    photo_card(c, img, 1040, 230, 620, 520, "Run it together", "partners, communities, funders", "run-fill")
    end_page(c, 14)


def slide_close(c: canvas.Canvas) -> None:
    begin_page(c)
    title(c, "Thank you, Octant and the Ethereum ecosystem.", 300, 775, 1320, 80, 88)
    c.setFillColor(FOREST)
    c.setFont(FONT_BOLD, 86)
    c.drawCentredString(960, 430, "Let's Fucking Grow")
    draw_pill(c, 455, 280, 290, 60, "greengoods.app", MINT, FOREST)
    draw_pill(c, 785, 280, 380, 60, "@greenpilldevguild", CREME, FOREST)
    draw_pill(c, 1205, 280, 300, 60, "@greenpilldevs", ALICE, FOREST)
    end_page(c, 15)


def build() -> None:
    ensure_dirs()
    c = canvas.Canvas(str(OUT), pagesize=(PDF_W, PDF_H))
    c.setTitle("Greenpill Dev Guild - Octant Epoch 12 Demo Day")
    slides = [
        slide_cover,
        slide_infrastructure,
        slide_people,
        slide_thesis,
        slide_problem,
        slide_staking,
        slide_green_goods,
        slide_bridge,
        slide_tech_sun,
        slide_omo,
        slide_rings,
        slide_flywheel,
        slide_marathon,
        slide_ask,
        slide_close,
    ]
    for draw in slides:
        draw(c)
    c.save()
    print(OUT)


if __name__ == "__main__":
    build()
