#!/usr/bin/env python3
"""Generate transparent hand-drawn PNG assets for the Octant E12 deck."""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"

S = 2

FOREST = "#1F3D1F"
DEEP = "#254D32"
SPRING = "#C2FF1A"
MINT = "#B1FDEB"
ALICE = "#DCEDFF"
CREME = "#FCECA6"
CRYOLA = "#FF6978"
SOIL = "#162F18"

FONT_PATH = "/System/Library/Fonts/Avenir Next.ttc"


def rgba(hex_color: str, alpha: int = 255) -> tuple[int, int, int, int]:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size * S, index=index)


FONT_HEAVY = 8
FONT_BOLD = 0


class Art:
    def __init__(self, width: int, height: int, seed: int):
        self.w = width
        self.h = height
        self.r = random.Random(seed)
        self.im = Image.new("RGBA", (width * S, height * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)

    def p(self, x: float, y: float) -> tuple[int, int]:
        return int(round(x * S)), int(round(y * S))

    def pts(self, points):
        return [self.p(x, y) for x, y in points]

    def jitter(self, value: float) -> float:
        return self.r.uniform(-value, value)

    def line(self, points, fill=FOREST, width=4, jitter=1.8, passes=2, joint="curve"):
        for pass_i in range(passes):
            wobble = [
                (x + self.jitter(jitter), y + self.jitter(jitter))
                for x, y in points
            ]
            self.d.line(
                self.pts(wobble),
                fill=rgba(fill, 225 if pass_i == 0 else 150),
                width=max(1, int(width * S)),
                joint=joint,
            )

    def dashed_line(self, points, fill=FOREST, width=4, dash=18, gap=14):
        if len(points) != 2:
            self.line(points, fill, width)
            return
        (x1, y1), (x2, y2) = points
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        if not dist:
            return
        ux, uy = dx / dist, dy / dist
        t = 0
        while t < dist:
            end = min(t + dash, dist)
            self.line(
                [(x1 + ux * t, y1 + uy * t), (x1 + ux * end, y1 + uy * end)],
                fill,
                width,
                jitter=1.3,
                passes=1,
            )
            t += dash + gap

    def polygon(self, points, fill, outline=FOREST, width=4, jitter=2.0):
        wpoints = [
            (x + self.jitter(jitter), y + self.jitter(jitter)) for x, y in points
        ]
        self.d.polygon(self.pts(wpoints), fill=rgba(fill))
        closed = wpoints + [wpoints[0]]
        self.line(closed, outline, width=width, jitter=jitter * 0.65, passes=2)

    def blob(self, cx, cy, rx, ry, fill, outline=FOREST, width=4, n=24, jitter=0.12):
        pts = []
        for i in range(n):
            a = math.tau * i / n
            rr = 1 + self.r.uniform(-jitter, jitter)
            pts.append((cx + math.cos(a) * rx * rr, cy + math.sin(a) * ry * rr))
        self.polygon(pts, fill, outline, width, jitter=1.4)

    def ellipse(self, box, fill, outline=FOREST, width=4, passes=2):
        x1, y1, x2, y2 = box
        self.d.ellipse(
            (x1 * S, y1 * S, x2 * S, y2 * S),
            fill=rgba(fill),
            outline=None,
        )
        for _ in range(passes):
            off = self.jitter(2)
            self.d.ellipse(
                (
                    (x1 + off) * S,
                    (y1 - off) * S,
                    (x2 - off) * S,
                    (y2 + off) * S,
                ),
                outline=rgba(outline, 225),
                width=int(width * S),
            )

    def rounded(self, box, radius, fill, outline=FOREST, width=5, passes=2):
        x1, y1, x2, y2 = box
        self.d.rounded_rectangle(
            (x1 * S, y1 * S, x2 * S, y2 * S),
            radius=radius * S,
            fill=rgba(fill),
        )
        for _ in range(passes):
            off = self.jitter(2.2)
            self.d.rounded_rectangle(
                (
                    (x1 + off) * S,
                    (y1 - off) * S,
                    (x2 - off) * S,
                    (y2 + off) * S,
                ),
                radius=radius * S,
                outline=rgba(outline, 230),
                width=int(width * S),
            )

    def text_center(self, xy, text, size, fill=FOREST, index=FONT_BOLD, spacing=10):
        f = font(size, index)
        lines = text.split("\n")
        line_boxes = [self.d.textbbox((0, 0), line, font=f) for line in lines]
        heights = [b[3] - b[1] for b in line_boxes]
        total_h = sum(heights) + spacing * S * (len(lines) - 1)
        y = xy[1] * S - total_h / 2
        for line, b, h in zip(lines, line_boxes, heights):
            tw = b[2] - b[0]
            self.d.text(
                (xy[0] * S - tw / 2, y - b[1]),
                line,
                font=f,
                fill=rgba(fill),
            )
            y += h + spacing * S

    def text_left(self, xy, text, size, fill=FOREST, index=FONT_BOLD, spacing=8):
        f = font(size, index)
        y = xy[1] * S
        for line in text.split("\n"):
            self.d.text((xy[0] * S, y), line, font=f, fill=rgba(fill))
            b = self.d.textbbox((0, 0), line, font=f)
            y += (b[3] - b[1]) + spacing * S

    def text_left_fit(self, xy, text, size, max_width, fill=FOREST, index=FONT_BOLD, min_size=26):
        next_size = size
        while next_size >= min_size:
            f = font(next_size, index)
            b = self.d.textbbox((0, 0), text, font=f)
            if (b[2] - b[0]) <= max_width * S:
                self.d.text((xy[0] * S, xy[1] * S), text, font=f, fill=rgba(fill))
                return next_size
            next_size -= 1
        f = font(min_size, index)
        self.d.text((xy[0] * S, xy[1] * S), text, font=f, fill=rgba(fill))
        return min_size

    def text_right(self, xy, text, size, fill=FOREST, index=FONT_BOLD, spacing=8):
        f = font(size, index)
        y = xy[1] * S
        for line in text.split("\n"):
            b = self.d.textbbox((0, 0), line, font=f)
            self.d.text((xy[0] * S - (b[2] - b[0]), y), line, font=f, fill=rgba(fill))
            y += (b[3] - b[1]) + spacing * S

    def save(self, name: str):
        OUT.mkdir(parents=True, exist_ok=True)
        final = self.im.resize((self.w, self.h), Image.Resampling.LANCZOS)
        final.save(OUT / name)


def leaf(art: Art, x, y, angle, scale=1, fill=SPRING):
    pts = []
    for i in range(15):
        t = i / 14
        a = math.sin(t * math.pi) * 20 * scale
        px = (t - 0.5) * 58 * scale
        pts.append((px, -a))
    for i in range(14, -1, -1):
        t = i / 14
        a = math.sin(t * math.pi) * 20 * scale
        px = (t - 0.5) * 58 * scale
        pts.append((px, a))
    ca, sa = math.cos(angle), math.sin(angle)
    rpts = [(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pts]
    art.polygon(rpts, fill, width=3)
    art.line([(x - math.cos(angle) * 25 * scale, y - math.sin(angle) * 25 * scale), (x + math.cos(angle) * 25 * scale, y + math.sin(angle) * 25 * scale)], FOREST, 2)


def seedling(art: Art, x, y, s=1):
    art.line([(x, y + 18 * s), (x, y - 12 * s)], FOREST, width=3, jitter=0.7)
    leaf(art, x - 9 * s, y - 5 * s, -0.55, 0.35 * s, SPRING)
    leaf(art, x + 10 * s, y - 8 * s, 0.55, 0.35 * s, MINT)


def solar_panel(art: Art, x, y, w=118, h=66, angle=0):
    ca, sa = math.cos(angle), math.sin(angle)

    def rot(px, py):
        return x + px * ca - py * sa, y + px * sa + py * ca

    pts = [rot(-w / 2, -h / 2), rot(w / 2, -h / 2), rot(w / 2, h / 2), rot(-w / 2, h / 2)]
    art.polygon(pts, ALICE, width=3, jitter=1.2)
    for i in range(1, 4):
        p1 = rot(-w / 2 + i * w / 4, -h / 2)
        p2 = rot(-w / 2 + i * w / 4, h / 2)
        art.line([p1, p2], FOREST, width=1.5, jitter=0.4, passes=1)
    for i in range(1, 3):
        p1 = rot(-w / 2, -h / 2 + i * h / 3)
        p2 = rot(w / 2, -h / 2 + i * h / 3)
        art.line([p1, p2], FOREST, width=1.5, jitter=0.4, passes=1)
    art.line([rot(0, h / 2), rot(0, h / 2 + 44)], FOREST, width=4, jitter=0.8)


def antenna(art: Art, x, y, h=88):
    art.line([(x, y), (x, y - h)], FOREST, width=4, jitter=0.8)
    art.line([(x - 36, y - h + 18), (x, y - h - 14), (x + 36, y - h + 18)], FOREST, width=3, jitter=0.9)
    for r in (22, 40):
        art.d.arc(
            ((x - r) * S, (y - h - r * 0.55) * S, (x + r) * S, (y - h + r * 0.9) * S),
            205,
            335,
            fill=rgba(FOREST, 210),
            width=int(2.5 * S),
        )


def hand(art: Art, x, y, mirror=1, scale=1):
    art.line([(x, y), (x + mirror * 26 * scale, y - 17 * scale), (x + mirror * 45 * scale, y - 12 * scale)], FOREST, 5, jitter=1.2)
    for i in range(4):
        art.line(
            [
                (x + mirror * (36 + i * 6) * scale, y - 12 * scale),
                (x + mirror * (48 + i * 6) * scale, y - (26 + i % 2 * 4) * scale),
            ],
            FOREST,
            3,
            jitter=0.8,
        )


def paste_rotated(art: Art, layer: Image.Image, cx, cy, angle):
    rotated = layer.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    x = int(cx * S - rotated.width / 2)
    y = int(cy * S - rotated.height / 2)
    art.im.alpha_composite(rotated, (x, y))


def brand_pill(art: Art, cx, cy, w, h, angle=-7):
    layer = Image.new("RGBA", (int((w + 34) * S), int((h + 34) * S)), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    pad = 17 * S
    box = (pad, pad, pad + w * S, pad + h * S)
    radius = h * S / 2
    d.rounded_rectangle(box, radius=radius, fill=rgba(CREME), outline=rgba(FOREST), width=int(5 * S))
    inner = (box[0] + 23 * S, box[1] + 21 * S, box[2] - 23 * S, box[3] - 21 * S)
    d.rounded_rectangle(inner, radius=(h - 42) * S / 2, fill=rgba(SPRING), outline=rgba(FOREST), width=int(5 * S))
    split_x = inner[0] + (inner[2] - inner[0]) * 0.5
    d.line((split_x, inner[1] + 5 * S, split_x, inner[3] - 5 * S), fill=rgba(FOREST), width=int(5 * S))
    dot_r = h * S * 0.18
    dot_cx = inner[0] + (inner[2] - inner[0]) * 0.27
    dot_cy = inner[1] + (inner[3] - inner[1]) * 0.5
    d.ellipse((dot_cx - dot_r, dot_cy - dot_r, dot_cx + dot_r, dot_cy + dot_r), fill=rgba(FOREST))
    paste_rotated(art, layer, cx, cy, angle)


def bird(art: Art, x, y, s=1):
    art.line([(x - 18 * s, y), (x - 5 * s, y - 8 * s), (x, y), (x + 8 * s, y - 8 * s), (x + 20 * s, y)], "#050905", width=4 * s, jitter=0.8, passes=1)


def pine(art: Art, x, y, s=1, fill=DEEP):
    art.polygon([(x, y - 58 * s), (x - 30 * s, y + 2 * s), (x + 30 * s, y + 2 * s)], fill, width=3, jitter=1)
    art.polygon([(x, y - 32 * s), (x - 38 * s, y + 34 * s), (x + 38 * s, y + 34 * s)], fill, width=3, jitter=1)
    art.line([(x, y + 28 * s), (x, y + 56 * s)], FOREST, width=5 * s, jitter=0.6)


def pine_cluster(art: Art, x, y, count=5, scale=1):
    for i in range(count):
        dx = (i - count / 2) * 30 * scale + art.jitter(14 * scale)
        dy = art.jitter(18 * scale)
        pine(art, x + dx, y + dy, scale * art.r.uniform(0.65, 1.05), DEEP if i % 2 else FOREST)


def mountain_range(art: Art, x, y, count=4, scale=1):
    for i in range(count):
        bx = x + i * 44 * scale
        h = art.r.uniform(54, 88) * scale
        w = art.r.uniform(52, 72) * scale
        art.line([(bx - w / 2, y), (bx, y - h), (bx + w / 2, y)], "#050905", width=5 * scale, jitter=1.1, passes=1)
        art.line([(bx - 7 * scale, y - h * 0.72), (bx + 14 * scale, y - h * 0.45)], "#050905", width=3 * scale, jitter=0.8, passes=1)


def hut(art: Art, x, y, s=1, fill=CREME):
    art.polygon([(x - 42 * s, y), (x, y - 42 * s), (x + 42 * s, y), (x + 32 * s, y + 14 * s), (x - 32 * s, y + 14 * s)], DEEP, width=3, jitter=1)
    art.rounded((x - 30 * s, y + 12 * s, x + 30 * s, y + 68 * s), 5 * s, fill, width=3, passes=1)
    art.line([(x - 8 * s, y + 68 * s), (x - 8 * s, y + 34 * s), (x + 10 * s, y + 34 * s), (x + 10 * s, y + 68 * s)], FOREST, width=2.5 * s, jitter=0.4, passes=1)


def crop_patch(art: Art, x, y, w, h, fill=CREME):
    art.blob(x, y, w / 2, h / 2, fill, width=3, n=16, jitter=0.16)
    for i in range(5):
        px = x - w * 0.33 + i * w * 0.17 + art.jitter(3)
        art.line([(px, y - h * 0.25), (px + art.jitter(6), y + h * 0.28)], FOREST, width=2, jitter=0.6, passes=1)
        seedling(art, px + 6, y + h * 0.2, 0.45)


def data_scroll(art: Art, x, y, s=1, fill=CREME):
    art.rounded((x - 28 * s, y - 38 * s, x + 28 * s, y + 38 * s), 6 * s, fill, width=2.5 * s, passes=1)
    for i in range(4):
        yy = y - 20 * s + i * 12 * s
        art.line([(x - 16 * s, yy), (x + 16 * s, yy + art.jitter(1.5))], FOREST, width=1.8 * s, jitter=0.3, passes=1)
    art.ellipse((x - 6 * s, y + 18 * s, x + 6 * s, y + 30 * s), SPRING, width=1.4 * s, passes=1)


def database_mark(art: Art, x, y, s=1):
    art.ellipse((x - 28 * s, y - 18 * s, x + 28 * s, y + 8 * s), ALICE, width=2.5 * s, passes=1)
    art.rounded((x - 28 * s, y - 8 * s, x + 28 * s, y + 42 * s), 4 * s, ALICE, width=2.5 * s, passes=1)
    for yy in (y + 8 * s, y + 24 * s):
        art.line([(x - 24 * s, yy), (x + 24 * s, yy)], FOREST, width=1.8 * s, jitter=0.4, passes=1)


def dotted_path(art: Art, points, fill=FOREST):
    for i in range(len(points) - 1):
        (x1, y1), (x2, y2) = points[i], points[i + 1]
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        if dist == 0:
            continue
        steps = max(3, int(dist / 28))
        for j in range(steps):
            if j % 2 == 0:
                t = j / steps
                art.ellipse((x1 + dx * t - 3, y1 + dy * t - 3, x1 + dx * t + 3, y1 + dy * t + 3), fill, fill, width=1, passes=1)


def cover_tree():
    art = Art(1024, 1536, 12)

    # Sun-like branded capsule.
    brand_pill(art, 716, 160, 350, 144, angle=-5)
    for x, y, s in [(882, 320, 0.75), (805, 282, 0.55), (720, 292, 0.45)]:
        bird(art, x, y, s)

    # Canopy and trunk, shifted right to leave the left third open.
    art.blob(690, 430, 232, 172, DEEP, width=5, n=34, jitter=0.18)
    art.blob(572, 478, 184, 142, MINT, width=5, n=30, jitter=0.16)
    art.blob(784, 472, 178, 132, SPRING, width=5, n=29, jitter=0.15)
    art.blob(700, 350, 138, 96, CREME, width=4, n=24, jitter=0.18)
    pine_cluster(art, 576, 366, 3, 0.58)
    pine_cluster(art, 826, 386, 3, 0.52)
    for x1, x2, y2, width in [(620, 662, 850, 18), (705, 690, 850, 20), (762, 714, 848, 14)]:
        art.line([(x1, 580), ((x1 + x2) / 2 + art.jitter(14), 690), (x2, y2)], DEEP, width=width, jitter=3, passes=2)
    art.line([(654, 584), (620, 528), (560, 508)], FOREST, width=7, jitter=2)
    art.line([(710, 594), (760, 536), (835, 520)], FOREST, width=7, jitter=2)

    # Soil mound and root infrastructure.
    art.blob(678, 946, 302, 122, MINT, width=5, n=34, jitter=0.18)
    art.blob(672, 930, 238, 70, CREME, width=3, n=26, jitter=0.17)
    root_starts = [(642, 836), (680, 836), (718, 838)]
    root_targets = [
        (330, 1168),
        (450, 1248),
        (592, 1320),
        (730, 1252),
        (848, 1168),
        (934, 1244),
    ]
    for i, target in enumerate(root_targets):
        start = root_starts[i % len(root_starts)]
        mid = ((start[0] + target[0]) / 2 + art.jitter(36), 1048 + art.jitter(44))
        art.line([start, mid, target], FOREST, width=7 if i in (0, 2, 5) else 5, jitter=2.0)
        art.ellipse((target[0] - 15, target[1] - 15, target[0] + 15, target[1] + 15), SPRING if i in (0, 3, 5) else CREME, width=4)
    for x, y, s in [(404, 1160, 0.8), (530, 1212, 0.7), (810, 1216, 0.65)]:
        art.line([(x, y), (x + 38, y + art.jitter(24))], FOREST, 2.5, jitter=0.9, passes=1)
    dotted_path(art, [(386, 1158), (504, 1128), (642, 1188), (786, 1130), (900, 1198)], FOREST)

    for x, y, s in [(452, 1020, 1), (558, 1088, 0.8), (768, 1050, 0.9), (850, 1106, 0.75), (350, 1096, 0.65)]:
        seedling(art, x, y, s)
    hand(art, 404, 962, mirror=1, scale=1.1)
    hand(art, 870, 982, mirror=-1, scale=1)
    solar_panel(art, 438, 956, 132, 70, -0.1)
    solar_panel(art, 858, 930, 122, 66, 0.08)
    antenna(art, 926, 986, 92)
    hut(art, 622, 966, 0.55, CREME)
    pine_cluster(art, 742, 1018, 4, 0.33)
    mountain_range(art, 120, 1370, 5, 0.72)
    pine_cluster(art, 210, 1268, 5, 0.45)

    # Light map glyphs in the open left column.
    for x, y in [(118, 336), (182, 774), (120, 1260), (242, 552)]:
        art.line([(x - 20, y), (x, y - 13), (x + 20, y)], FOREST, width=3, jitter=1.4, passes=1)

    art.save("octant-cover-tree.png")


def lock(art: Art, x, y, scale=1):
    art.rounded((x - 22 * scale, y - 2 * scale, x + 22 * scale, y + 42 * scale), 9 * scale, CREME, CREME, width=2, passes=1)
    art.d.arc(
        ((x - 19 * scale) * S, (y - 35 * scale) * S, (x + 19 * scale) * S, (y + 12 * scale) * S),
        180,
        360,
        fill=rgba(CREME),
        width=int(5 * scale * S),
    )
    art.line([(x, y + 13 * scale), (x, y + 27 * scale)], DEEP, width=3 * scale, jitter=0.4, passes=1)


def silo(art: Art, x, y, w=104, h=282):
    art.rounded((x, y + 36, x + w, y + h), 16, DEEP, width=5, passes=2)
    dome = [(x, y + 48), (x + w * 0.16, y + 12), (x + w / 2, y), (x + w * 0.84, y + 12), (x + w, y + 48)]
    art.polygon(dome + [(x + w, y + 70), (x, y + 70)], DEEP, width=5)
    for yy in range(int(y + 94), int(y + h - 20), 44):
        art.line([(x + 14, yy), (x + w - 14, yy + art.jitter(3))], FOREST, width=2, jitter=0.7, passes=1)
    data_scroll(art, x + w * 0.30, y + h * 0.28, 0.48, CREME)
    database_mark(art, x + w * 0.72, y + h * 0.73, 0.42)
    lock(art, x + w / 2, y + h * 0.52, 1.08)


def coin(art: Art, x, y, r=28):
    art.ellipse((x - r, y - r, x + r, y + r), CREME, width=4)
    art.ellipse((x - r * 0.54, y - r * 0.54, x + r * 0.54, y + r * 0.54), CREME, width=2, passes=1)


def bank(art: Art, x, y):
    art.polygon([(x - 96, y), (x, y - 72), (x + 96, y), (x + 82, y + 18), (x - 82, y + 18)], ALICE, width=4)
    for px in (-54, 0, 54):
        art.rounded((x + px - 14, y + 22, x + px + 14, y + 118), 4, CREME, width=3)
    art.rounded((x - 104, y + 122, x + 104, y + 150), 4, ALICE, width=4)


def funding_problem():
    art = Art(1536, 1024, 21)

    # Locked impact silos.
    for args in [(110, 154, 110, 330), (240, 112, 112, 372), (376, 180, 106, 318), (205, 340, 112, 338)]:
        silo(art, *args)
    mountain_range(art, 72, 202, 3, 0.48)
    pine_cluster(art, 112, 538, 6, 0.42)
    pine_cluster(art, 438, 548, 4, 0.35)
    art.blob(294, 723, 220, 52, MINT, width=4, n=24, jitter=0.15)
    dotted_path(art, [(112, 736), (238, 684), (374, 714), (506, 672)], FOREST)
    art.text_center((296, 858), "IMPACT", 46, index=FONT_HEAVY)

    # Far-away capital.
    bank(art, 1252, 220)
    bird(art, 1370, 178, 0.68)
    bird(art, 1318, 134, 0.5)
    for i in range(5):
        coin(art, 1134 + i * 41, 486 - i * 18, 30)
    for i in range(4):
        coin(art, 1242 + i * 42, 470 - i * 13, 28)
    pine_cluster(art, 1368, 530, 4, 0.34)
    mountain_range(art, 1138, 610, 4, 0.42)
    art.text_center((1235, 858), "CAPITAL", 46, index=FONT_HEAVY)

    # Ravine, broken bridge, falling coins.
    left_ridge = [(590, 158), (620, 296), (602, 408), (642, 550), (610, 724), (652, 906)]
    right_ridge = [(922, 140), (882, 280), (914, 410), (874, 558), (910, 724), (866, 906)]
    art.line(left_ridge, FOREST, width=6, jitter=3)
    art.line(right_ridge, FOREST, width=6, jitter=3)
    for y in range(190, 870, 94):
        art.line([(620 + art.jitter(16), y), (875 + art.jitter(16), y + art.jitter(28))], FOREST, width=2, jitter=3, passes=1)
    for y in range(250, 800, 110):
        mountain_range(art, 678 + art.jitter(14), y, 3, 0.34)
    art.dashed_line([(476, 394), (684, 376)], FOREST, width=5, dash=26, gap=20)
    art.dashed_line([(838, 376), (1080, 322)], FOREST, width=5, dash=26, gap=20)
    art.line([(750, 318), (805, 438)], CRYOLA, width=12, jitter=1.1, passes=1)
    art.line([(812, 318), (742, 438)], CRYOLA, width=12, jitter=1.1, passes=1)
    for x, y in [(714, 486), (764, 596), (822, 514)]:
        coin(art, x, y, 22)
        art.line([(x - 10, y + 32), (x - 28, y + 78)], FOREST, width=2, jitter=2, passes=1)

    # One open field set apart.
    solution_route = [(1004, 708), (1088, 644), (1168, 574), (1242, 506)]
    art.line(solution_route, FOREST, width=12, jitter=1.4, passes=1)
    art.line(solution_route, SPRING, width=6, jitter=1.0, passes=1)
    art.polygon([(1232, 488), (1276, 500), (1242, 528)], SPRING, width=3, jitter=0.8)
    art.blob(956, 750, 148, 74, SPRING, width=5, n=22, jitter=0.16)
    crop_patch(art, 948, 770, 148, 56, SPRING)
    seedling(art, 956, 724, 2.0)
    for x in (860, 906, 1000, 1054):
        seedling(art, x, 780 + art.jitter(18), 0.8)
    hut(art, 1060, 704, 0.42, CREME)
    pine_cluster(art, 842, 726, 3, 0.28)
    art.text_center((956, 930), "ONE OPEN FIELD", 38, index=FONT_HEAVY)

    art.save("octant-funding-problem.png")


def down_arrow(art: Art, cx, cy, scale=1):
    art.line([(cx, cy - 50 * scale), (cx, cy + 32 * scale)], FOREST, width=8 * scale, jitter=1.2)
    art.polygon(
        [
            (cx - 34 * scale, cy + 18 * scale),
            (cx, cy + 66 * scale),
            (cx + 34 * scale, cy + 18 * scale),
        ],
        SPRING,
        width=4,
        jitter=1,
    )


def hardware_icon(art: Art, cx, cy):
    solar_panel(art, cx - 82, cy + 12, 92, 48, -0.12)
    antenna(art, cx + 66, cy + 44, 58)
    mountain_range(art, cx - 118, cy + 72, 3, 0.22)


def rewards_icon(art: Art, cx, cy):
    for i, (dx, dy) in enumerate([(-42, 12), (0, 0), (42, 16), (-2, 42)]):
        coin(art, cx + dx, cy + dy, 22 if i < 3 else 18)
    dotted_path(art, [(cx - 74, cy + 62), (cx - 22, cy + 42), (cx + 34, cy + 58), (cx + 82, cy + 24)], FOREST)


def vault_icon(art: Art, cx, cy):
    art.rounded((cx - 76, cy - 46, cx + 76, cy + 56), 14, CREME, width=4)
    art.ellipse((cx - 30, cy - 28, cx + 30, cy + 32), ALICE, width=4)
    for a in range(0, 360, 60):
        rad = math.radians(a)
        art.line([(cx, cy + 2), (cx + math.cos(rad) * 22, cy + 2 + math.sin(rad) * 22)], FOREST, width=2, jitter=0.4, passes=1)
    pine_cluster(art, cx + 100, cy + 42, 3, 0.23)


def staking_flow():
    art = Art(1024, 1536, 34)

    panels = [
        ((88, 120, 936, 418), CREME, "HARDWARE", "Obol · Dappnode", hardware_icon),
        ((88, 612, 936, 910), MINT, "STAKING REWARDS", "Lido · yield", rewards_icon),
        ((88, 1104, 936, 1402), ALICE, "COMMUNITY ENDOWMENT", "Octant vaults", vault_icon),
    ]
    for box, fill, title, sub, icon_fn in panels:
        art.rounded(box, 42, fill, width=6, passes=3)
        x1, y1, x2, y2 = box
        dotted_path(art, [(x1 + 38, y2 - 36), (x1 + 196, y2 - 56), (x1 + 350, y2 - 42), (x2 - 48, y2 - 62)], FOREST)
        icon_fn(art, x1 + 146, (y1 + y2) / 2 + 20)
        text_x = x1 + 284
        max_w = x2 - text_x - 46
        art.text_left_fit((text_x, y1 + 84), title, 54, max_w, index=FONT_HEAVY, min_size=33)
        art.text_left((text_x + 2, y1 + 174), sub, 32, index=FONT_BOLD)
        if title == "HARDWARE":
            pine_cluster(art, x2 - 126, y1 + 228, 4, 0.28)
        elif title == "STAKING REWARDS":
            crop_patch(art, x2 - 126, y1 + 224, 112, 46, CREME)
        else:
            hut(art, x2 - 132, y1 + 210, 0.46, CREME)
    down_arrow(art, 512, 508, 1.0)
    down_arrow(art, 512, 1000, 1.0)

    art.save("octant-staking-flow.png")


def curved_arrow(art: Art, cx, cy, r, start_deg, end_deg):
    pts = []
    for i in range(24):
        t = i / 23
        a = math.radians(start_deg + (end_deg - start_deg) * t)
        pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r))
    art.line(pts, FOREST, width=6, jitter=1.2)
    a = math.radians(end_deg)
    tip = (cx + math.cos(a) * r, cy + math.sin(a) * r)
    back = (cx + math.cos(a - 0.12) * (r - 38), cy + math.sin(a - 0.12) * (r - 38))
    left = (back[0] + math.cos(a + 2.45) * 24, back[1] + math.sin(a + 2.45) * 24)
    right = (back[0] + math.cos(a - 2.45) * 24, back[1] + math.sin(a - 2.45) * 24)
    art.polygon([tip, left, right], FOREST, FOREST, width=1, jitter=0.4)


def flywheel():
    art = Art(1024, 1024, 55)
    cx = cy = 512
    r = 262

    pine_cluster(art, 128, 208, 4, 0.32)
    pine_cluster(art, 890, 792, 4, 0.3)
    mountain_range(art, 86, 826, 5, 0.38)
    bird(art, 872, 126, 0.52)
    bird(art, 930, 184, 0.44)

    # Main ring.
    for off in (-5, 0, 5):
        art.d.ellipse(
            ((cx - r + off) * S, (cy - r - off) * S, (cx + r - off) * S, (cy + r + off) * S),
            outline=rgba(FOREST, 175),
            width=int(5 * S),
        )
    curved_arrow(art, cx, cy, r, -72, 2)
    curved_arrow(art, cx, cy, r, 18, 92)
    curved_arrow(art, cx, cy, r, 108, 182)
    curved_arrow(art, cx, cy, r, 198, 272)

    # Center community disc.
    art.ellipse((384, 384, 640, 640), SPRING, width=6, passes=3)
    hut(art, 512, 432, 0.34, CREME)
    art.text_center((512, 536), "COMMUNITY", 30, index=FONT_HEAVY, spacing=6)

    nodes = [
        (512, 206, MINT, "1", "DIASPORA\nCAPITAL", (512, 104), "center"),
        (810, 512, SPRING, "2", "LOCAL HUBS", (810, 390), "center"),
        (512, 818, ALICE, "3", "VERIFIED\nIMPACT", (512, 932), "center"),
        (214, 512, CREME, "4", "MORE FUNDING\n+ TRUST", (214, 388), "center"),
    ]
    for x, y, fill, num, label, label_xy, align in nodes:
        art.ellipse((x - 72, y - 72, x + 72, y + 72), fill, width=5, passes=3)
        art.text_center((x, y), num, 48, index=FONT_HEAVY)
        art.text_center(label_xy, label, 24, index=FONT_HEAVY, spacing=4)
        if num == "1":
            dotted_path(art, [(x - 84, y - 18), (x - 132, y - 44), (x - 172, y - 34)], FOREST)
        elif num == "2":
            pine_cluster(art, x + 104, y + 52, 3, 0.22)
        elif num == "3":
            crop_patch(art, x + 110, y - 12, 92, 38, MINT)
        elif num == "4":
            coin(art, x - 108, y + 12, 18)
            coin(art, x - 138, y + 36, 15)

    art.save("octant-flywheel.png")


def validate():
    expected = {
        "octant-cover-tree.png": (1024, 1536),
        "octant-funding-problem.png": (1536, 1024),
        "octant-staking-flow.png": (1024, 1536),
        "octant-flywheel.png": (1024, 1024),
    }
    for name, size in expected.items():
        path = OUT / name
        im = Image.open(path)
        if im.size != size:
            raise SystemExit(f"{name}: expected {size}, got {im.size}")
        if im.mode != "RGBA":
            raise SystemExit(f"{name}: expected RGBA, got {im.mode}")
        corners = [im.getpixel((0, 0)), im.getpixel((size[0] - 1, 0)), im.getpixel((0, size[1] - 1)), im.getpixel((size[0] - 1, size[1] - 1))]
        if any(px[3] != 0 for px in corners):
            raise SystemExit(f"{name}: non-transparent corner detected: {corners}")
    print("generated transparent PNG assets:")
    for name in expected:
        print(OUT / name)


def main():
    cover_tree()
    funding_problem()
    staking_flow()
    flywheel()
    validate()


if __name__ == "__main__":
    main()
