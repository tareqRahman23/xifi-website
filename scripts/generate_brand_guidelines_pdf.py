from __future__ import annotations

import math
import shutil
from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "XIFI_Brand_Guidelines_v1.0.pdf"
PUBLIC = ROOT / "public" / "assets" / "XIFI-Brand-Guidelines-v1.0.pdf"
LOGO = ROOT / "public" / "assets" / "xifi-app-icon.png"
OUTFIT = ROOT / "scripts" / "assets" / "Outfit-Variable.ttf"

W = 960
H = 600
M = 48

INK = HexColor("#101239")
MUTED = HexColor("#69708F")
CLOUD = HexColor("#FAFBFF")
PINK = HexColor("#D83F9B")
BLUE = HexColor("#2F63F5")
VIOLET = HexColor("#7552ED")
CORAL = HexColor("#FF6E73")
GREEN = HexColor("#28AA76")
LINE = Color(0.25, 0.28, 0.52, alpha=0.17)


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Outfit", str(OUTFIT)))
    pdfmetrics.registerFont(TTFont("SegoeBold", r"C:\Windows\Fonts\segoeuib.ttf"))
    pdfmetrics.registerFont(TTFont("GeorgiaItalic", r"C:\Windows\Fonts\georgiai.ttf"))


def set_alpha(c: canvas.Canvas, fill: float = 1, stroke: float | None = None) -> None:
    if hasattr(c, "setFillAlpha"):
        c.setFillAlpha(fill)
    if stroke is not None and hasattr(c, "setStrokeAlpha"):
        c.setStrokeAlpha(stroke)


def gradient_rect(c: canvas.Canvas, x: float, y: float, width: float, height: float,
                  colors: list[Color], positions: list[float], radius: float = 0) -> None:
    """Paint a linear gradient inside a bounded rectangular clipping path."""
    c.saveState()
    path = c.beginPath()
    if radius:
        path.roundRect(x, y, width, height, radius)
    else:
        path.rect(x, y, width, height)
    c.clipPath(path, stroke=0, fill=0)
    c.linearGradient(x, y, x + width, y + height, colors, positions)
    c.restoreState()


def text(c: canvas.Canvas, x: float, y: float, value: str, size: float, color=INK,
         font: str = "Outfit", bold: bool = False) -> None:
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.setFont(font, size)
    if bold and font == "Outfit":
        c.setLineWidth(max(0.25, size * 0.012))
        obj = c.beginText(x, y)
        obj.setFont(font, size)
        obj.setFillColor(color)
        obj.setStrokeColor(color)
        obj.setTextRenderMode(2)
        obj.textLine(value)
        c.drawText(obj)
    else:
        c.drawString(x, y, value)
    c.restoreState()


def right_text(c: canvas.Canvas, x: float, y: float, value: str, size: float,
               color=INK, font: str = "Outfit") -> None:
    c.saveState()
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawRightString(x, y, value)
    c.restoreState()


def wrap_lines(value: str, font: str, size: float, width: float) -> list[str]:
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if pdfmetrics.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(c: canvas.Canvas, x: float, y: float, value: str, width: float,
              size: float = 10, color=MUTED, leading: float | None = None,
              font: str = "Outfit") -> float:
    leading = leading or size * 1.45
    lines = wrap_lines(value, font, size, width)
    for line in lines:
        text(c, x, y, line, size, color, font)
        y -= leading
    return y


def top_label(c: canvas.Canvas, number: str, label: str, dark: bool = False) -> None:
    accent = CORAL if dark else PINK
    secondary = Color(1, 1, 1, 0.62) if dark else MUTED
    text(c, M, H - 47, number, 12, accent, bold=True)
    text(c, M + 30, H - 46, "/", 9, secondary)
    text(c, M + 45, H - 46, label.upper(), 7.5, secondary, bold=True)


def footer(c: canvas.Canvas, page: int, dark: bool = False) -> None:
    color = Color(1, 1, 1, 0.42) if dark else Color(0.18, 0.2, 0.38, 0.46)
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(0.6)
    c.line(M, 30, W - M, 30)
    text(c, M, 16, "XIFI BRAND GUIDELINES", 6.5, color, bold=True)
    right_text(c, W - M, 16, f"{page:02d} / 08", 6.5, color)
    c.restoreState()


def draw_logo(c: canvas.Canvas, x: float, y: float, size: float) -> None:
    c.drawImage(ImageReader(str(LOGO)), x, y, size, size, mask="auto")


def glass_tile(c: canvas.Canvas, x: float, y: float, size: float) -> None:
    c.saveState()
    set_alpha(c, 0.14)
    c.setFillColor(VIOLET)
    c.roundRect(x + 16, y - 12, size, size, size * 0.25, fill=1, stroke=0)
    set_alpha(c, 0.88)
    c.setFillColor(white)
    c.setStrokeColor(Color(1, 1, 1, 0.94))
    c.setLineWidth(1)
    c.roundRect(x, y, size, size, size * 0.25, fill=1, stroke=1)
    set_alpha(c, 1)
    draw_logo(c, x + size * 0.17, y + size * 0.17, size * 0.66)
    c.restoreState()


def ribbon(c: canvas.Canvas, y: float, dark: bool = False) -> None:
    c.saveState()
    set_alpha(c, 0.18 if not dark else 0.52, 0.25)
    c.setLineCap(1)
    path = c.beginPath()
    path.moveTo(-80, y)
    path.curveTo(150, y + 72, 275, y - 90, 500, y + 5)
    path.curveTo(675, y + 82, 790, y - 42, 1040, y + 22)
    c.setStrokeColor(PINK)
    c.setLineWidth(64 if dark else 46)
    c.drawPath(path, stroke=1, fill=0)
    set_alpha(c, 0.14 if not dark else 0.28, 0.2)
    c.setStrokeColor(BLUE)
    c.setLineWidth(28 if dark else 18)
    c.drawPath(path, stroke=1, fill=0)
    set_alpha(c, 1, 1)
    c.restoreState()


def icon_bubble(c: canvas.Canvas, x: float, y: float, color=PINK) -> None:
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(2.3)
    c.roundRect(x, y, 34, 24, 6, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(x + 8, y)
    p.lineTo(x + 5, y - 7)
    p.lineTo(x + 14, y)
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def icon_check(c: canvas.Canvas, x: float, y: float, color=VIOLET) -> None:
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(2.3)
    c.circle(x + 17, y + 12, 15, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(x + 9, y + 12)
    p.lineTo(x + 14, y + 7)
    p.lineTo(x + 24, y + 18)
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def icon_people(c: canvas.Canvas, x: float, y: float, color=BLUE) -> None:
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(2.3)
    c.circle(x + 17, y + 19, 8, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(x + 3, y - 3)
    p.curveTo(x + 5, y + 10, x + 29, y + 10, x + 31, y - 3)
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def page_cover(c: canvas.Canvas) -> None:
    c.setFillColor(CLOUD)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    text(c, M, H - 48, "XIFI", 9, VIOLET, bold=True)
    right_text(c, W - M, H - 48, "BRAND SYSTEM / VERSION 1.0", 7.5, MUTED)
    text(c, M, 342, "Brand", 88, INK, bold=True)
    text(c, M, 260, "system", 88, INK, bold=True)
    text(c, M, 218, "Intelligence", 19, BLUE, bold=True)
    text(c, M + 111, 218, "in motion.", 22, PINK, "GeorgiaItalic")
    paragraph(c, M, 174,
              "A visual system for an AI-native contact center that moves customer intent toward a grounded answer, an approved action, or a context-rich human handoff.",
              390, 9.5, MUTED, 14)
    ribbon(c, 122)
    glass_tile(c, 625, 172, 245)
    footer(c, 1)
    c.showPage()


def page_foundation(c: canvas.Canvas) -> None:
    c.setFillColor(CLOUD)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    top_label(c, "00", "Foundation")
    text(c, 230, 465, "One useful", 58, INK, bold=True)
    text(c, 230, 410, "outcome.", 61, PINK, "GeorgiaItalic")
    paragraph(c, 655, 460,
              "The brand makes sophisticated contact-center infrastructure understandable. Begin with intent, show controlled intelligence at work, and end with a clear next step.",
              245, 9.2, MUTED, 14)

    cards = [
        (M, "01", "Grounded answer", "Approved knowledge, expressed with clarity and source-aware confidence.", icon_bubble),
        (M + 290, "02", "Approved action", "Permissioned work with visible control, verification, and a receipt.", icon_check),
        (M + 580, "03", "Human handoff", "A calm transition with customer context intact and no forced restart.", icon_people),
    ]
    for x, num, title, body, draw_icon in cards:
        c.setStrokeColor(LINE)
        c.line(x, 340, x, 185)
        text(c, x + 17, 320, num, 7, MUTED, bold=True)
        draw_icon(c, x + 17, 255)
        text(c, x + 17, 220, title, 16, INK, bold=True)
        paragraph(c, x + 17, 198, body, 235, 7.8, MUTED, 11)

    text(c, M, 128, "BRAND CHARACTER", 7, PINK, bold=True)
    characters = [
        ("Precise", "Exact about what the system knows and did."),
        ("Human", "Natural language without pretending to be a person."),
        ("Composed", "Complex operations feel calm and ordered."),
        ("Progressive", "Every frame implies useful forward motion."),
    ]
    for i, (title, body) in enumerate(characters):
        x = M + i * 218
        text(c, x, 96, title, 13, INK, bold=True)
        paragraph(c, x, 77, body, 186, 7.2, MUTED, 10)
    footer(c, 2)
    c.showPage()


def page_mark(c: canvas.Canvas) -> None:
    c.setFillColor(CLOUD)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    top_label(c, "01", "Mark")
    text(c, 300, 467, "A coordinated", 54, INK, bold=True)
    text(c, 300, 412, "handoff.", 59, PINK, "GeorgiaItalic")
    glass_tile(c, 56, 180, 220)

    center_y = 274
    c.saveState()
    c.setLineWidth(2.2)
    c.setStrokeColor(PINK)
    c.line(355, center_y + 24, 515, center_y + 6)
    c.line(608, center_y + 6, 775, center_y + 24)
    c.setStrokeColor(BLUE)
    c.line(355, center_y - 24, 515, center_y - 6)
    c.line(608, center_y - 6, 775, center_y - 24)
    c.restoreState()
    draw_logo(c, 520, center_y - 42, 84)

    labels = [(355, "Two paths", "approach."), (508, "They meet, resolve,", "and align."), (742, "Together,", "they continue.")]
    for x, line1, line2 in labels:
        text(c, x, 183, line1, 8, INK, bold=True)
        text(c, x, 170, line2, 8, INK, bold=True)

    c.setStrokeColor(LINE)
    c.line(M, 135, W - M, 135)
    text(c, M, 111, "CORE IDEA", 7, PINK, bold=True)
    paragraph(c, 150, 112,
              "Two forms approach, meet, and continue together. The rounded field, pink spectrum, and white symbol are one protected unit.",
              540, 8.5, MUTED, 13)
    text(c, 760, 105, "Simple.", 12, INK, bold=True)
    text(c, 760, 89, "Controlled.", 12, INK, bold=True)
    text(c, 760, 73, "Connected.", 12, PINK, bold=True)
    footer(c, 3)
    c.showPage()


def page_logo_rules(c: canvas.Canvas) -> None:
    c.setFillColor(CLOUD)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    top_label(c, "01.1", "Logo rules")
    text(c, M, 470, "Keep it", 54, INK, bold=True)
    text(c, M, 418, "recognizable.", 57, PINK, "GeorgiaItalic")

    columns = [(M, 280), (340, 280), (632, 280)]
    for x, width in columns:
        c.setStrokeColor(LINE)
        c.roundRect(x, 175, width, 205, 14, fill=0, stroke=1)

    text(c, 66, 355, "CLEAR SPACE", 7, PINK, bold=True)
    c.setDash(4, 3)
    c.setStrokeColor(Color(0.85, 0.25, 0.61, alpha=0.45))
    c.rect(112, 218, 145, 125, fill=0, stroke=1)
    c.rect(137, 238, 95, 85, fill=0, stroke=1)
    c.setDash()
    draw_logo(c, 144, 245, 80)
    text(c, 117, 329, "x", 8, PINK, bold=True)
    text(c, 244, 329, "x", 8, PINK, bold=True)
    paragraph(c, 66, 201, "Use clear space equal to one quarter of the icon width on every side.", 238, 7.4, MUTED, 10)

    text(c, 358, 355, "MINIMUM SIZE", 7, PINK, bold=True)
    draw_logo(c, 400, 252, 48)
    c.setStrokeColor(PINK)
    c.line(457, 276, 516, 276)
    text(c, 525, 271, "24 px", 10, PINK, bold=True)
    paragraph(c, 358, 215, "Keep the icon at 24 px or larger. Use the full wordmark lockup at 120 px or larger.", 238, 7.4, MUTED, 10)

    text(c, 650, 355, "APPROVED BACKGROUNDS", 7, PINK, bold=True)
    c.setFillColor(white)
    c.roundRect(653, 242, 72, 72, 12, fill=1, stroke=0)
    c.setFillColor(INK)
    c.roundRect(738, 242, 72, 72, 12, fill=1, stroke=0)
    gradient_rect(c, 823, 242, 72, 72, [BLUE, VIOLET, PINK, CORAL], [0, 0.36, 0.7, 1], 12)
    draw_logo(c, 665, 254, 48)
    draw_logo(c, 750, 254, 48)
    draw_logo(c, 835, 254, 48)
    paragraph(c, 650, 215, "Use Cloud White, Deep Ink, or the controlled XIFI spectrum.", 235, 7.4, MUTED, 10)

    c.setFillColor(HexColor("#F3F4FA"))
    c.roundRect(M, 70, W - 2 * M, 75, 14, fill=1, stroke=0)
    text(c, 68, 117, "NEVER", 7, PINK, bold=True)
    rules = ["Stretch or skew", "Recolor the symbol", "Add outlines or effects", "Place on visual noise"]
    for i, rule in enumerate(rules):
        x = 178 + i * 183
        c.setStrokeColor(PINK)
        c.setLineWidth(1.5)
        c.line(x, 103, x + 10, 93)
        c.line(x + 10, 103, x, 93)
        text(c, x + 20, 94, rule, 7.4, INK, bold=True)
    footer(c, 4)
    c.showPage()


def page_color(c: canvas.Canvas) -> None:
    c.linearGradient(0, 0, W, H, [PINK, VIOLET, BLUE, CORAL, INK], [0, 0.27, 0.5, 0.74, 1])
    top_label(c, "02", "System", dark=True)
    text(c, M, 432, "Color carries", 61, white, bold=True)
    text(c, M, 372, "the conversation.", 61, white, bold=True)
    paragraph(c, 612, 425,
              "The spectrum moves from signal to intelligence to human resolution. Use it directionally, with restraint, and beside generous neutral space.",
              292, 9, Color(1, 1, 1, 0.78), 14)

    palette = [
        ("XIFI Pink", "#D83F9B", PINK, True),
        ("Electric Blue", "#2F63F5", BLUE, True),
        ("Signal Violet", "#7552ED", VIOLET, True),
        ("Warm Coral", "#FF6E73", CORAL, True),
        ("Deep Ink", "#101239", INK, True),
        ("Cloud White", "#FAFBFF", CLOUD, False),
    ]
    sw = W / len(palette)
    for i, (name, hex_value, color, dark) in enumerate(palette):
        x = i * sw
        c.setFillColor(color)
        c.rect(x, 70, sw, 190, fill=1, stroke=0)
        tc = white if dark else INK
        text(c, x + 16, 225, name, 9.2, tc, bold=True)
        text(c, x + 16, 207, hex_value, 7.5, tc)
        set_alpha(c, 0.13)
        c.setFillColor(white if dark else INK)
        c.rect(x, 70, sw, 63, fill=1, stroke=0)
        set_alpha(c, 1)
    footer(c, 5, dark=True)
    c.showPage()


def page_type(c: canvas.Canvas) -> None:
    c.setFillColor(CLOUD)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    top_label(c, "02.1", "Typography")
    text(c, M, 472, "Outfit", 78, INK, bold=True)
    paragraph(c, M, 422, "Geometric enough for technology. Open enough for people.", 260, 9, MUTED, 13)
    c.setStrokeColor(LINE)
    c.line(330, 150, 330, 510)
    text(c, 374, 452, "Human clarity.", 45, INK, bold=True)
    text(c, 374, 402, "Machine precision.", 45, INK, bold=True)
    c.setStrokeColor(PINK)
    c.line(374, 376, 894, 376)
    text(c, 374, 342, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 11.5, INK)
    text(c, 374, 316, "abcdefghijklmnopqrstuvwxyz", 11.5, INK)
    text(c, 374, 290, "0123456789  ! @ # $ % & * ( ) +", 11.5, INK)

    samples = [
        ("DISPLAY / 72-120", "Move with purpose.", 28, 210),
        ("HEADING / 40-72", "Clear at every turn.", 21, 152),
        ("BODY / 16-20", "Short paragraphs make a complex system easier to navigate.", 10, 98),
    ]
    for label, sample, size, y in samples:
        text(c, 374, y + 24, label, 6.5, PINK, bold=True)
        text(c, 374, y, sample, size, INK, bold=True if size > 12 else False)
    footer(c, 6)
    c.showPage()


def page_expression(c: canvas.Canvas) -> None:
    c.setFillColor(HexColor("#070B21"))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    ribbon(c, 308, dark=True)
    top_label(c, "03", "Expression", dark=True)
    text(c, M, 450, "Simple.", 54, white, bold=True)
    text(c, M, 398, "Controlled.", 54, white, bold=True)
    text(c, M, 340, "Connected.", 59, CORAL, "GeorgiaItalic")

    icon_bubble(c, 62, 252, CORAL)
    text(c, 58, 222, "Grounded", 8, white, bold=True)
    text(c, 61, 210, "answer", 8, white, bold=True)
    text(c, 150, 233, ">", 16, Color(1, 1, 1, 0.6), bold=True)
    icon_check(c, 190, 252, CORAL)
    text(c, 187, 222, "Approved", 8, white, bold=True)
    text(c, 194, 210, "action", 8, white, bold=True)
    text(c, 278, 233, ">", 16, Color(1, 1, 1, 0.6), bold=True)
    icon_people(c, 320, 252, CORAL)
    text(c, 315, 222, "Human", 8, white, bold=True)
    text(c, 313, 210, "handoff", 8, white, bold=True)

    cards = [(M, "SAY", ["Here's what I found.", "Based on your context...", "Here's what we can do next.", "I'll connect you with a person who can help."]),
             (W / 2 + 6, "DON'T SAY", ["I think...", "You need to...", "As an AI model...", "Please hold while I transfer you."])]
    for x, title, lines in cards:
        c.saveState()
        c.setFillColor(HexColor("#F7F8FC"))
        c.setStrokeColor(Color(1, 1, 1, 0.22))
        c.roundRect(x, 62, W / 2 - M - 14, 122, 14, fill=1, stroke=1)
        text(c, x + 22, 158, title, 10, CORAL, bold=True)
        for i, line in enumerate(lines):
            text(c, x + 22, 134 - i * 19, line, 8.2, INK)
        c.restoreState()
    footer(c, 7, dark=True)
    c.showPage()


def page_applications(c: canvas.Canvas) -> None:
    c.setFillColor(CLOUD)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    top_label(c, "04", "Applications")
    text(c, 230, 470, "Recognizable", 52, INK, bold=True)
    text(c, 230, 418, "at every scale.", 55, PINK, "GeorgiaItalic")
    paragraph(c, 710, 458,
              "The identity stays calm and exact as an app icon, a product surface, or a single campaign statement.",
              190, 8.6, MUTED, 13)

    c.saveState()
    c.setFillColor(INK)
    c.roundRect(55, 115, 210, 245, 20, fill=1, stroke=0)
    draw_logo(c, 105, 225, 110)
    text(c, 78, 155, "XIFI", 12, white, bold=True)
    text(c, 78, 136, "Customer operations", 7, Color(1, 1, 1, 0.55))
    c.restoreState()

    c.setFillColor(white)
    c.setStrokeColor(LINE)
    c.roundRect(300, 102, 360, 280, 18, fill=1, stroke=1)
    c.setStrokeColor(LINE)
    c.line(300, 332, 660, 332)
    c.setFillColor(GREEN)
    c.circle(322, 352, 4, fill=1, stroke=0)
    text(c, 334, 348, "XIFI SESSION", 7, INK, bold=True)
    right_text(c, 640, 348, "POLICY CONTROLLED", 5.8, MUTED)
    gradient_rect(c, 438, 278, 182, 32, [BLUE, VIOLET], [0, 1], 8)
    text(c, 453, 291, "Help me understand my billing change.", 6.5, white)
    icon_check(c, 322, 226, VIOLET)
    text(c, 364, 250, "Intent understood", 8, INK, bold=True)
    text(c, 364, 236, "Account and policy context resolved", 6, MUTED)
    c.setFillColor(HexColor("#F7F8FC"))
    c.roundRect(320, 135, 320, 72, 11, fill=1, stroke=0)
    text(c, 338, 184, "Here's what changed.", 8, INK, bold=True)
    paragraph(c, 338, 168, "Your plan moved to the current rate at renewal.", 270, 6.5, MUTED, 9)

    gradient_rect(c, 695, 118, 205, 244, [PINK, VIOLET, BLUE], [0, 0.58, 1], 16)
    text(c, 720, 332, "XIFI", 7, white, bold=True)
    text(c, 720, 258, "Clarity", 27, white, bold=True)
    text(c, 720, 230, "moves the", 27, white, bold=True)
    text(c, 720, 202, "conversation.", 27, white, bold=True)
    c.saveState()
    set_alpha(c, 0.45, 0.45)
    c.setStrokeColor(white)
    c.ellipse(708, 143, 896, 200, fill=0, stroke=1)
    c.restoreState()
    text(c, 720, 137, "SIMPLE. CONTROLLED. CONNECTED.", 5.8, Color(1, 1, 1, 0.72), bold=True)

    text(c, M, 73, "CORE ASSETS", 7, PINK, bold=True)
    text(c, 155, 70, "SVG mark  /  PNG app icon  /  PDF brand guide", 8, INK, bold=True)
    right_text(c, W - M, 70, "getxifi.com", 8, BLUE)
    footer(c, 8)
    c.showPage()


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(W, H), pageCompression=1)
    pdf.setTitle("XIFI Brand Guidelines v1.0")
    pdf.setAuthor("XIFI")
    pdf.setSubject("XIFI identity system, logo, color, typography, voice, and applications")
    pdf.setCreator("XIFI brand system generator")
    for draw_page in (
        page_cover,
        page_foundation,
        page_mark,
        page_logo_rules,
        page_color,
        page_type,
        page_expression,
        page_applications,
    ):
        draw_page(pdf)
    pdf.save()
    shutil.copy2(OUTPUT, PUBLIC)
    print(OUTPUT)
    print(PUBLIC)


if __name__ == "__main__":
    build()
