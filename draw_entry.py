#!/usr/bin/env python3
"""Draw the 26 November 2026 world-news front page (1024x1024 PNG).

Newspaper front page, drawn entirely with PIL primitives. No fetched
images, no network, deterministic output.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

INK = (26, 26, 26)
PAPER = (247, 243, 232)
RED = (176, 42, 32)
NAVY = (31, 58, 95)
TEAL = (14, 96, 92)
GOLD = (184, 134, 11)
GREY = (90, 88, 80)
LIGHT = (238, 232, 216)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def flame(draw, cx, base, s, c1=(230, 90, 20), c2=(245, 180, 40)):
    """Simple two-tone flame, base at (cx, base), size s."""
    outer = [(cx - 0.42 * s, base), (cx - 0.30 * s, base - 0.55 * s),
             (cx - 0.10 * s, base - 0.45 * s), (cx, base - s),
             (cx + 0.12 * s, base - 0.55 * s), (cx + 0.34 * s, base - 0.42 * s),
             (cx + 0.42 * s, base)]
    draw.polygon(outer, fill=c1)
    inner = [(cx - 0.20 * s, base), (cx - 0.14 * s, base - 0.42 * s),
             (cx, base - 0.62 * s), (cx + 0.15 * s, base - 0.30 * s),
             (cx + 0.20 * s, base)]
    draw.polygon(inner, fill=c2)


def globe(draw, cx, cy, r, fg):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=fg, width=4)
    draw.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
                 outline=fg, width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=fg, width=3)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
             200, 340, fill=fg, width=3)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
             20, 160, fill=fg, width=3)


def chart_down(draw, x, y, w, h, fg):
    draw.line([x, y + h, x + w, y + h], fill=fg, width=3)
    draw.line([x, y, x, y + h], fill=fg, width=3)
    pts = [(x + 4, y + 8), (x + w * 0.3, y + h * 0.3),
           (x + w * 0.55, y + h * 0.45), (x + w * 0.8, y + h * 0.75),
           (x + w - 4, y + h - 6)]
    draw.line(pts, fill=fg, width=5, joint="curve")
    ex, ey = pts[-1]
    draw.polygon([(ex, ey), (ex - 12, ey - 2), (ex - 2, ey - 12)], fill=fg)


def bars(draw, x, y, w, h, vals, fg):
    n = len(vals)
    bw = w / n * 0.55
    gap = w / n
    mx = max(vals)
    for i, v in enumerate(vals):
        bh = h * v / mx
        bx = x + i * gap + (gap - bw) / 2
        draw.rectangle([bx, y + h - bh, bx + bw, y + h], fill=fg)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin

    # ---------- masthead ----------
    d.text((W // 2, 16), "THE WORLD TODAY", font=font(SERIF_B, 62),
           fill=INK, anchor="ma")
    d.text((W // 2, 88), "THURSDAY  ·  26 NOVEMBER 2026",
           font=font(SANS_B, 25), fill=RED, anchor="ma")
    d.text((W // 2, 120), "ONE DAY'S NEWS — IN ONE PAGE",
           font=font(SANS, 16), fill=GREY, anchor="ma")
    d.line([M, 146, W - M, 146], fill=INK, width=3)
    d.line([M, 151, W - M, 151], fill=INK, width=1)

    # ---------- lead story: US tariffs ----------
    ly, lh = 162, 168
    d.text((M, ly), "LEAD  ·  TRADE", font=font(SANS_B, 17), fill=RED)
    head = ["US UNVEILS NEW TARIFFS", "ON 14 TRADING PARTNERS"]
    y = ly + 26
    for ln in head:
        d.text((M, y), ln, font=font(SERIF_B, 38), fill=INK)
        y += 44
    cap = ("Washington says the duties target factory overcapacity;\n"
           "China faces the highest rates. Markets slid.")
    draw_lines(d, cap.split("\n"), M, y + 6, font(SANS, 18), INK, 23)
    # lead visual panel: navy, globe + tariff bars
    px0, py0, px1, py1 = 668, ly, W - M, ly + lh
    d.rectangle([px0, py0, px1, py1], fill=NAVY)
    globe(d, 748, py0 + 78, 56, (247, 243, 232))
    d.text((748, py0 + 140), "14 PARTNERS", font=font(SANS_B, 15),
           fill=(247, 243, 232), anchor="ma")
    bars(d, 838, py0 + 42, 130, 84, [3, 5, 8], (245, 180, 40))
    d.text((903, py0 + 132), "CHINA: HIGHEST RATE",
           font=font(SANS_B, 13), fill=(245, 180, 40), anchor="ma")
    d.text((903, py0 + 150), "TAIWAN: UP TO 15%",
           font=font(SANS, 12), fill=(200, 205, 220), anchor="ma")

    # ---------- story cards ----------
    cards = [
        ("MIDDLE EAST", RED,
         "OIL JUMPS AS HOUTHIS CLAIM SAUDI REFINERY STRIKE",
         "Brent crude settled 3.5% higher at $94.61 a barrel after the "
         "claim on Ras Tanura; Riyadh says it shot down four drones.",
         "derrick"),
        ("MARKETS", NAVY,
         "AI ROUT DEEPENS AS NASDAQ SLIDES NEARLY 4%",
         "Tech shares led US stocks down as fears over AI valuations "
         "intensified; futures slid after the tariff news.",
         "chart"),
        ("UKRAINE", TEAL,
         "LEAKED RUSSIAN DATA PUT WAR DEAD NEAR 500,000",
         "BBC analysis of Rosstat records counts at least 490,334 "
         "Russian soldiers killed since February 2022.",
         "bars"),
        ("GAZA", RED,
         "ISRAELI STRIKE KILLS SECOND HAMAS SECURITY CHIEF IN A DAY",
         "Mohammed Abu al-Ouf died with his wife and two daughters in "
         "Gaza City; his superior was killed a day earlier.",
         "building"),
        ("EGYPT", GOLD,
         "31 KILLED AS FUEL TANKER FIRE ENGULFS CAIRO HIGHWAY",
         "A tanker overturned on the Ring Road in Giza; 21 were hurt "
         "and dozens of vehicles burned in the blaze.",
         "flame"),
        ("LATIN AMERICA", NAVY,
         "ALL HOSTAGES FREED IN CARTAGENA SUPERMARKET SIEGE",
         "Colombian forces stormed the store after a day-long standoff; "
         "one gunman was killed and the captives are safe.",
         "store"),
    ]
    cw, ch, gap = 474, 188, 12
    top = 342
    for i, (kick, col, head, cap, icon) in enumerate(cards):
        cx = M + (i % 2) * (cw + gap)
        cy = top + (i // 2) * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], outline=INK, width=2)
        d.rectangle([cx, cy, cx + cw, cy + 30], fill=col)
        d.text((cx + 12, cy + 5), kick, font=font(SANS_B, 16),
               fill=(255, 255, 255))
        # icon panel on the right
        ix = cx + cw - 96
        d.rectangle([ix, cy + 30, cx + cw, cy + ch], fill=LIGHT)
        icx, icy = ix + 48, cy + 30 + (ch - 30) // 2
        if icon == "flame":
            flame(d, icx, icy + 34, 52)
        elif icon == "derrick":
            # oil derrick: tapering tower with crossbars + flame on top
            d.line([icx - 26, icy + 34, icx - 8, icy - 30], fill=INK, width=4)
            d.line([icx + 26, icy + 34, icx + 8, icy - 30], fill=INK, width=4)
            d.line([icx - 8, icy - 30, icx + 8, icy - 30], fill=INK, width=4)
            for fy in (icy - 12, icy + 6, icy + 22):
                d.line([icx - 20, fy, icx + 20, fy], fill=INK, width=3)
            d.line([icx - 20, icy + 6, icx + 20, icy + 22], fill=INK, width=2)
            d.line([icx + 20, icy + 6, icx - 20, icy + 22], fill=INK, width=2)
            flame(d, icx, icy - 30, 26)
        elif icon == "chart":
            chart_down(d, ix + 14, icy - 34, 68, 68, RED)
        elif icon == "bars":
            bars(d, ix + 14, icy - 34, 68, 68, [2, 4, 6, 9], TEAL)
            d.text((icx, icy + 40), "490,334", font=font(SANS_B, 13),
                   fill=TEAL, anchor="ma")
        elif icon == "building":
            d.rectangle([icx - 30, icy - 34, icx + 30, icy + 34],
                        outline=INK, width=3)
            for wy in (icy - 22, icy - 2, icy + 18):
                for wx in (icx - 20, icx, icx + 20):
                    d.rectangle([wx - 6, wy - 6, wx + 6, wy + 6], fill=INK)
            d.line([icx - 34, icy - 34, icx + 34, icy - 34], fill=RED, width=4)
        elif icon == "store":
            d.rectangle([icx - 34, icy - 20, icx + 34, icy + 34],
                        outline=INK, width=3)
            for k in range(4):
                x0 = icx - 34 + k * 17
                d.polygon([(x0, icy - 20), (x0 + 17, icy - 20),
                           (x0 + 12, icy - 34), (x0 + 5, icy - 34)],
                          fill=RED if k % 2 == 0 else NAVY)
            d.rectangle([icx - 10, icy + 8, icx + 10, icy + 34], fill=INK)
        # headline + caption
        tx = cx + 12
        tw = cw - 96 - 24
        hl = wrap(d, head, font(SERIF_B, 22), tw)
        y = draw_lines(d, hl, tx, cy + 42, font(SERIF_B, 22), INK, 25)
        cl = wrap(d, cap, font(SANS, 16), tw)
        draw_lines(d, cl, tx, y + 4, font(SANS, 16), (60, 58, 52), 20)

    # ---------- in-brief strip ----------
    by = top + 3 * ch + 2 * gap + 12
    d.line([M, by, W - M, by], fill=INK, width=2)
    d.text((M, by + 10), "IN BRIEF",
           font=font(SANS_B, 17), fill=RED)
    brief = ("South Korea lifts its rate to 3.25%  ·  Bank of Japan signals "
             "faster hikes  ·  Nasdaq down nearly 4%  ·  Houthi drones also "
             "hit Riyadh's financial district")
    bl = wrap(d, brief, font(SANS, 16), W - 2 * M - 110)
    draw_lines(d, bl, M + 108, by + 10, font(SANS, 16), INK, 21)
    fy = H - 18
    d.line([M, fy - 8, W - M, fy - 8], fill=INK, width=1)
    d.text((W // 2, fy), "Sources: Reuters · BBC · AP · CNN  —  26 November 2026",
           font=font(SANS, 13), fill=GREY, anchor="ma")

    img.save(OUT, optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
