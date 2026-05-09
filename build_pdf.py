"""
Crew Manual — A5 PDF generator (v2)
Mothership-inspired typography, clean and table-readable.
A5 single pages in reading order. Worksheet pages have fillable form fields.
"""

import os
import re
import html
from pathlib import Path
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import black, HexColor
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    PageBreak, Table, TableStyle, KeepTogether, Preformatted, Flowable,
    CondPageBreak,
    NextPageTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ============================================================ FONTS
FONT_DIR = "/usr/share/fonts"
pdfmetrics.registerFont(TTFont('Body',
    f"{FONT_DIR}/liberation-fonts/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont('Body-Bold',
    f"{FONT_DIR}/liberation-fonts/LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont('Body-Italic',
    f"{FONT_DIR}/liberation-fonts/LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont('Body-BoldItalic',
    f"{FONT_DIR}/liberation-fonts/LiberationSans-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont('Mono',
    f"{FONT_DIR}/dejavu/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont('Heading',
    f"{FONT_DIR}/dejavu/DejaVuSansCondensed-Bold.ttf"))
registerFontFamily('Body', normal='Body', bold='Body-Bold',
                   italic='Body-Italic', boldItalic='Body-BoldItalic')

# ============================================================ LAYOUT
PAGE_W, PAGE_H = A5
MARGIN_TOP = 16 * mm
MARGIN_BOTTOM = 16 * mm
MARGIN_L = 14 * mm
MARGIN_R = 14 * mm
FRAME_W = PAGE_W - MARGIN_L - MARGIN_R
FRAME_H = PAGE_H - MARGIN_TOP - MARGIN_BOTTOM
INK = black
SUBTLE = HexColor('#555555')

# ============================================================ STYLES
S = {
    'body': ParagraphStyle('body', fontName='Body', fontSize=9, leading=12.5,
        alignment=TA_JUSTIFY, spaceAfter=4, textColor=INK),
    'callout': ParagraphStyle('callout', fontName='Body-Italic', fontSize=8.5,
        leading=11.5, alignment=TA_LEFT, leftIndent=8, rightIndent=8,
        spaceAfter=4, spaceBefore=2, textColor=INK),
    'callout_panel': ParagraphStyle('callout_panel', fontName='Body-Italic',
        fontSize=8.5, leading=11.5, alignment=TA_LEFT,
        leftIndent=0, rightIndent=0, spaceAfter=3, spaceBefore=0,
        textColor=INK),
    'chapter_num': ParagraphStyle('chapter_num', fontName='Heading',
        fontSize=10, leading=12, alignment=TA_LEFT, textColor=SUBTLE, spaceAfter=2),
    'chapter_title': ParagraphStyle('chapter_title', fontName='Heading',
        fontSize=22, leading=26, alignment=TA_LEFT, textColor=INK, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Heading', fontSize=12, leading=15,
        alignment=TA_LEFT, textColor=INK, spaceBefore=10, spaceAfter=4,
        keepWithNext=1),
    'h3': ParagraphStyle('h3', fontName='Body-Bold', fontSize=10, leading=13,
        alignment=TA_LEFT, textColor=INK, spaceBefore=7, spaceAfter=2,
        keepWithNext=1),
    'bullet': ParagraphStyle('bullet', fontName='Body', fontSize=9, leading=12.5,
        alignment=TA_LEFT, leftIndent=14, bulletIndent=2, spaceAfter=2,
        textColor=INK),
    'numbered': ParagraphStyle('numbered', fontName='Body', fontSize=9,
        leading=12.5, alignment=TA_LEFT, leftIndent=18, bulletIndent=2,
        spaceAfter=2, textColor=INK),
    'code': ParagraphStyle('code', fontName='Mono', fontSize=6.8, leading=8.6,
        alignment=TA_LEFT, textColor=INK, spaceBefore=4, spaceAfter=6),
    'cover_super': ParagraphStyle('cs', fontName='Heading', fontSize=11,
        leading=14, alignment=TA_CENTER, textColor=INK),
    'cover_title': ParagraphStyle('ct', fontName='Heading', fontSize=42,
        leading=46, alignment=TA_CENTER, textColor=INK),
    'cover_sub': ParagraphStyle('csub', fontName='Body-Italic', fontSize=11,
        leading=15, alignment=TA_CENTER, textColor=INK),
    'cover_foot': ParagraphStyle('cf', fontName='Body', fontSize=9,
        leading=12, alignment=TA_CENTER, textColor=SUBTLE),
    'toc1': ParagraphStyle('toc1', fontName='Body-Bold', fontSize=10,
        leading=14, leftIndent=0, spaceBefore=4, spaceAfter=0, textColor=INK),
}

# ============================================================ STATE
class DocState:
    chapter_num = ""
    chapter_title = ""
doc_state = DocState()


# ============================================================ FLOWABLES
class HeaderRule(Flowable):
    def __init__(self, width=None, thickness=0.6):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
    def wrap(self, aW, aH):
        if self.width is None:
            self.width = aW
        return (self.width, self.thickness + 4)
    def draw(self):
        self.canv.setStrokeColor(INK)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 2, self.width, 2)


class ChapterMarker(Flowable):
    def __init__(self, num, title):
        Flowable.__init__(self)
        self.num = num; self.title = title
    def wrap(self, aW, aH):
        return (0, 0)
    def draw(self):
        doc_state.chapter_num = self.num
        doc_state.chapter_title = self.title
        key = f"chapter_{self.num.replace('.', '_').replace(' ', '_')}"
        self.canv.bookmarkPage(key)
        if self.num.isdigit() and self.num != "0":
            label = f"{self.num}. {self.title}"
        elif self.num == "A":
            label = f"Appendix A — {self.title}"
        else:
            label = self.title
        self.canv.addOutlineEntry(label, key, level=0)


class HeaderUpdater(Flowable):
    """Update header state without adding outline (use before page break)."""
    def __init__(self, num, title):
        Flowable.__init__(self)
        self.num = num; self.title = title
    def wrap(self, aW, aH):
        return (0, 0)
    def draw(self):
        doc_state.chapter_num = self.num
        doc_state.chapter_title = self.title


class SectionMarker(Flowable):
    def __init__(self, num, title, level=1):
        Flowable.__init__(self)
        self.num = num; self.title = title; self.level = level
    def wrap(self, aW, aH):
        return (0, 0)
    def draw(self):
        key = f"section_{self.num.replace('.', '_')}"
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(f"{self.num} {self.title}", key, level=self.level)


# ============================================================ PARSER
def outline_level(section_num):
    parts = section_num.split('.')
    return max(1, len(parts) - 1)


def pdf_chapter_title(num, title):
    if num == "6":
        return "Integrity & Atmosphere"
    if num == "7":
        return "EVA & Submersion Ops."
    return title


FORCED_SECTION_PAGEBREAKS = {
    "1.5",
    "3.2",
    "8.2",
    "10.4",
    "10.5",
    "11.10",
    "13.2",
    "13.3",
    "13.4",
    "13.5",
    "13.6",
    "13.7",
}
FORCED_HEADING_PAGEBREAKS = {"4.2"}


def forced_break_heading_num(line):
    stripped = line.strip()
    m = re.match(r'^#{2,4}\s+([0-9A-Z]+\.\d+(?:\.\d+)?)\s+.+$', stripped)
    if not m:
        return None
    num = m.group(1)
    if num in FORCED_SECTION_PAGEBREAKS:
        return num
    return None


def append_forced_pagebreak_if_needed(lines, n, i, story):
    j = i
    while j < n and not lines[j].strip():
        j += 1
    if j < n and forced_break_heading_num(lines[j]):
        story.append(PageBreak())


def append_pagebreak_if_not_top(story):
    story.append(CondPageBreak(FRAME_H - 1))


def md_inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!_)__([^_]+)__(?!_)', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!_)_([^_\n]+)_(?!_)', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+)`', r'<font face="Mono" size="8">\1</font>', text)
    return text

def is_table_separator(line):
    s = line.strip()
    if not s.startswith('|'):
        return False
    return bool(re.match(r'^\|[\s\-:|]+\|$', s))


def table_col_widths(headers):
    normalized = tuple(h.strip().lower() for h in headers)
    if normalized == ("resource", "default", "step trigger", "when empty"):
        ratios = (0.23, 0.12, 0.19, 0.46)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("state", "description"):
        ratios = (0.22, 0.78)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("protocol", "triggered by"):
        ratios = (0.30, 0.70)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("tier", "category", "examples"):
        ratios = (0.08, 0.24, 0.68)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("level", "description"):
        ratios = (0.18, 0.82)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("effect", "nominal", "brownout", "dead"):
        ratios = (0.24, 0.16, 0.23, 0.37)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("suit type", "rating", "typical use"):
        ratios = (0.24, 0.33, 0.43)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("role", "typical station", "key skills"):
        ratios = (0.18, 0.28, 0.54)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("section state", "stress per scene"):
        ratios = (0.64, 0.36)
        return [FRAME_W * ratio for ratio in ratios]
    if normalized == ("d20", "event"):
        ratios = (0.08, 0.92)
        return [FRAME_W * ratio for ratio in ratios]
    return [FRAME_W / len(headers)] * len(headers)


def build_table(headers, rows, table_width):
    n_cols = len(headers)
    header_style = ParagraphStyle('th', fontName='Body-Bold', fontSize=8,
        leading=10, alignment=TA_LEFT, textColor=INK)
    cell_style = ParagraphStyle('td', fontName='Body', fontSize=8,
        leading=10, alignment=TA_LEFT, textColor=INK)
    tbl_data = [[Paragraph(md_inline(h), header_style) for h in headers]]
    for r in rows:
        tbl_data.append([Paragraph(md_inline(c), cell_style) for c in r])
    col_widths = table_col_widths(headers)
    if table_width != FRAME_W:
        scale = table_width / FRAME_W
        col_widths = [w * scale for w in col_widths]
    t = Table(tbl_data, colWidths=col_widths, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Body-Bold', 8),
        ('LINEBELOW', (0, 0), (-1, 0), 0.8, INK),
        ('LINEABOVE', (0, 0), (-1, 0), 0.8, INK),
        ('LINEBELOW', (0, -1), (-1, -1), 0.4, INK),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [None, HexColor('#F4F4F4')]),
    ]))
    return t


def make_table(headers, rows, table_width=FRAME_W):
    t = build_table(headers, rows, table_width)
    return KeepTogether([t, Spacer(1, 6)])


def make_callout_panel(flowables):
    rows = [[flowable] for flowable in flowables]
    panel = Table(rows, colWidths=[FRAME_W])
    style = [
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#EFEFEF')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LINEBEFORE', (0, 0), (0, -1), 1.4, INK),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]
    style.append(('TOPPADDING', (0, 0), (-1, 0), 6))
    style.append(('BOTTOMPADDING', (0, len(rows) - 1), (-1, len(rows) - 1), 6))
    panel.setStyle(TableStyle(style))
    return panel


def parse_markdown(md_text, story):
    lines = md_text.split('\n')
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1; continue

        # Chapter heading. Most chapters use H1, but tolerate numbered H2
        # chapter titles so a single markdown inconsistency does not break
        # the PDF chapter opener.
        m = re.match(r'^#{1,2} (.+)$', stripped)
        if m:
            title_line = m.group(1).strip()
            m2 = re.match(r'^(\d+)\.\s+(.+)$', title_line)
            is_appendix = title_line.startswith('APPENDIX')
            is_h1 = stripped.startswith('# ')
            if m2 or is_appendix or is_h1:
                if m2:
                    num = m2.group(1)
                    title = m2.group(2).title().replace('Eva', 'EVA').replace('Ai', 'AI').replace('Gme', 'GME')
                elif is_appendix:
                    num = "A"
                    title = "Worksheet & Procedures"
                else:
                    num = ""
                    title = title_line.title()
                title = pdf_chapter_title(num, title)
                # Update header state BEFORE page break
                story.append(HeaderUpdater(num, title))
                append_pagebreak_if_not_top(story)
                story.append(ChapterMarker(num, title))
                story.append(Spacer(1, 18))
                label = ""
                if num.isdigit():
                    label = f"CHAPTER {num}"
                elif num == "A":
                    label = "APPENDIX A"
                if label:
                    story.append(Paragraph(label, S['chapter_num']))
                story.append(Paragraph(title.upper(), S['chapter_title']))
                story.append(HeaderRule(thickness=1.0))
                story.append(Spacer(1, 8))
                i += 1; continue

        # H2
        m = re.match(r'^## (.+)$', stripped)
        if m:
            heading = m.group(1).strip()
            mh = re.match(r'^([0-9A-Z]+\.\d+(?:\.\d+)?)\s+(.+)$', heading)
            if mh:
                if mh.group(1) in FORCED_HEADING_PAGEBREAKS:
                    story.append(PageBreak())
                story.append(SectionMarker(mh.group(1), mh.group(2),
                                           level=outline_level(mh.group(1))))
            story.append(Paragraph(md_inline(heading), S['h2']))
            i += 1; continue

        # H3 / H4
        m = re.match(r'^#{3,4} (.+)$', stripped)
        if m:
            heading = m.group(1).strip()
            mh = re.match(r'^([0-9A-Z]+\.\d+(?:\.\d+)?)\s+(.+)$', heading)
            if mh:
                if mh.group(1) in FORCED_HEADING_PAGEBREAKS:
                    story.append(PageBreak())
                story.append(SectionMarker(mh.group(1), mh.group(2),
                                           level=outline_level(mh.group(1))))
            story.append(Paragraph(md_inline(heading), S['h3']))
            i += 1; continue

        # Code fence
        if stripped.startswith('```'):
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1
            story.append(KeepTogether(Preformatted('\n'.join(code_lines), S['code'])))
            append_forced_pagebreak_if_needed(lines, n, i, story)
            continue

        # Blockquote — render as a light-grey panel
        if stripped.startswith('>'):
            quote_lines = []
            while i < n and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            segments = []
            q = 0
            while q < len(quote_lines):
                qs = quote_lines[q].strip()
                if not qs:
                    q += 1
                    continue
                if qs.startswith('|') and q + 1 < len(quote_lines) and is_table_separator(quote_lines[q + 1]):
                    header_cells = [c.strip() for c in qs.strip('|').split('|')]
                    q += 2
                    rows = []
                    while q < len(quote_lines) and quote_lines[q].strip().startswith('|'):
                        row_cells = [c.strip() for c in quote_lines[q].strip().strip('|').split('|')]
                        while len(row_cells) < len(header_cells):
                            row_cells.append('')
                        rows.append(row_cells)
                        q += 1
                    segments.append(("table", (header_cells, rows)))
                    continue
                para_lines = [qs]
                q += 1
                while q < len(quote_lines):
                    nxt = quote_lines[q].strip()
                    if not nxt:
                        break
                    if nxt.startswith('|') and q + 1 < len(quote_lines) and is_table_separator(quote_lines[q + 1]):
                        break
                    para_lines.append(nxt)
                    q += 1
                segments.append(("paragraph", ' '.join(para_lines)))
            if segments:
                inner = []
                panel_width = FRAME_W - 16
                for kind, payload in segments:
                    if kind == "paragraph":
                        inner.append(Paragraph(md_inline(payload), S['callout_panel']))
                    else:
                        headers, rows = payload
                        inner.append(build_table(headers, rows, panel_width))
                panel = make_callout_panel(inner)
                story.append(Spacer(1, 3))
                story.append(panel)
                story.append(Spacer(1, 4))
            append_forced_pagebreak_if_needed(lines, n, i, story)
            continue

        # Tables
        if stripped.startswith('|') and i + 1 < n and is_table_separator(lines[i + 1]):
            header_cells = [c.strip() for c in stripped.strip('|').split('|')]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith('|'):
                row_cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                while len(row_cells) < len(header_cells):
                    row_cells.append('')
                rows.append(row_cells)
                i += 1
            story.append(make_table(header_cells, rows))
            append_forced_pagebreak_if_needed(lines, n, i, story)
            continue

        # Bullets
        if re.match(r'^- ', stripped):
            while i < n and re.match(r'^- ', lines[i].strip()):
                content = lines[i].strip()[2:].strip()
                story.append(Paragraph(md_inline(content), S['bullet'],
                                       bulletText='\u2022'))
                i += 1
            append_forced_pagebreak_if_needed(lines, n, i, story)
            continue

        # Numbered
        if re.match(r'^\d+\. ', stripped):
            while i < n and re.match(r'^\d+\. ', lines[i].strip()):
                m = re.match(r'^(\d+)\.\s+(.+)$', lines[i].strip())
                num = m.group(1); content = m.group(2)
                j = i + 1
                while j < n and lines[j].startswith('   ') and lines[j].strip():
                    content += ' ' + lines[j].strip()
                    j += 1
                story.append(Paragraph(md_inline(content), S['numbered'],
                                       bulletText=f"{num}."))
                i = j
            append_forced_pagebreak_if_needed(lines, n, i, story)
            continue

        # HR
        if stripped == '---':
            story.append(Spacer(1, 6))
            story.append(HeaderRule(thickness=0.4))
            story.append(Spacer(1, 6))
            i += 1; continue

        # Paragraph
        para_lines = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].rstrip()
            if not nxt.strip():
                break
            ns = nxt.strip()
            if (ns.startswith('#') or ns.startswith('- ') or
                ns.startswith('> ') or ns.startswith('|') or
                ns.startswith('```') or re.match(r'^\d+\. ', ns) or
                ns == '---'):
                break
            para_lines.append(ns)
            i += 1
        story.append(Paragraph(md_inline(' '.join(para_lines)), S['body']))
        append_forced_pagebreak_if_needed(lines, n, i, story)


# ============================================================ DECORATION
def draw_page_decoration(canv, doc):
    canv.saveState()
    page_num = canv.getPageNumber()
    if page_num == 1:
        canv.restoreState()
        return
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.4)
    header_y = PAGE_H - MARGIN_TOP + 6
    canv.line(MARGIN_L, header_y, PAGE_W - MARGIN_R, header_y)
    canv.setFont('Body', 7.5)
    canv.setFillColor(SUBTLE)
    chapter_label = ""
    if doc_state.chapter_num and doc_state.chapter_title:
        cn = doc_state.chapter_num
        if cn.isdigit() and cn != "0":
            chapter_label = f"CH {cn} — {doc_state.chapter_title.upper()}"
        elif cn == "A":
            chapter_label = f"APP A — {doc_state.chapter_title.upper()}"
        elif cn == "0":
            chapter_label = doc_state.chapter_title.upper()
    canv.drawString(MARGIN_L, header_y + 3, chapter_label)
    canv.drawRightString(PAGE_W - MARGIN_R, header_y + 3, "CREW MANUAL")
    footer_y = MARGIN_BOTTOM - 6
    canv.line(MARGIN_L, footer_y + 8, PAGE_W - MARGIN_R, footer_y + 8)
    canv.setFont('Body', 8)
    canv.setFillColor(INK)
    canv.drawCentredString(PAGE_W / 2, footer_y, f"— {page_num} —")
    canv.restoreState()


def draw_cover_page(canv, doc):
    canv.saveState()
    canv.setStrokeColor(INK)
    canv.setLineWidth(2.0)
    canv.line(MARGIN_L, PAGE_H - 24*mm, PAGE_W - MARGIN_R, PAGE_H - 24*mm)
    canv.line(MARGIN_L, 24*mm, PAGE_W - MARGIN_R, 24*mm)
    canv.setLineWidth(0.4)
    canv.line(MARGIN_L, PAGE_H - 22*mm, PAGE_W - MARGIN_R, PAGE_H - 22*mm)
    canv.line(MARGIN_L, 26*mm, PAGE_W - MARGIN_R, 26*mm)
    canv.restoreState()


# ============================================================ FORM HELPERS
def add_textfield(canv, name, x, y, width, height, fontSize=8, tooltip=''):
    canv.acroForm.textfield(
        name=name, tooltip=tooltip or name,
        x=x, y=y, width=width, height=height,
        borderStyle='underlined', borderWidth=0.5, forceBorder=False,
        fontName='Helvetica', fontSize=fontSize,
        textColor=INK, fillColor=None, relative=False,
    )

def add_checkbox(canv, name, x, y, size=8, tooltip=''):
    canv.acroForm.checkbox(
        name=name, tooltip=tooltip or name,
        x=x, y=y, size=size,
        buttonStyle='check', borderStyle='solid', borderWidth=0.5,
        relative=False,
    )


def draw_ws_header(canv, num, title, hint=""):
    """Worksheet page header. Returns Y where content can start."""
    canv.saveState()
    canv.setFillColor(INK)
    # The page-decoration header is at PAGE_H - MARGIN_TOP + 6 (top rule).
    # We start below that with our own title.
    title_y = PAGE_H - MARGIN_TOP - 18
    canv.setFont('Heading', 13)
    canv.drawString(MARGIN_L, title_y, f"{num}  {title.upper()}")
    if hint:
        canv.setFont('Body-Italic', 7.5)
        canv.setFillColor(SUBTLE)
        canv.drawString(MARGIN_L, title_y - 11, hint)
        canv.setFillColor(INK)
    # Heavy rule
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.8)
    rule_y = title_y - 18
    canv.restoreState()
    return rule_y - 6


# ============================================================ A.1
def page_ws_a1(canv, doc):
    draw_page_decoration(canv, doc)
    y = draw_ws_header(canv, "A.1", "Resource Track",
        "Mark the current die size. Step left when the die steps down.")
    canv.saveState()

    # Layout within available 120mm:
    #   Resource (38mm) | 5 dice boxes (5×7.5=37.5mm) | Notes (~42mm)
    col_res_x = MARGIN_L
    col_res_w = 38 * mm
    col_dice_x = MARGIN_L + 40 * mm
    col_dice_box_w = 7.5 * mm
    col_notes_x = col_dice_x + 5 * col_dice_box_w + 2 * mm
    col_notes_w = (PAGE_W - MARGIN_R) - col_notes_x

    canv.setFont('Body-Bold', 7)
    canv.setFillColor(INK)
    canv.drawString(col_res_x, y, "RESOURCE")
    canv.drawString(col_dice_x, y, "DIE")
    canv.drawString(col_notes_x, y, "NOTES")
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.4)
    canv.line(MARGIN_L, y - 2, PAGE_W - MARGIN_R, y - 2)

    resources = [
        ("Battery", "battery", "d8 default"),
        ("O2 (EVA only)", "o2", "d10 default"),
        ("Ammo — weapon 1", "ammo1", "d8 default"),
        ("Ammo — weapon 2", "ammo2", "d8 default"),
        ("Stims / Medkit", "stims", "d6 default"),
        ("Rations / Water", "rations", "d10 default"),
        ("Heating (suit)", "heating", "EVA cold"),
        ("Filter (suit)", "filter", "EVA toxic"),
        ("Custom", "custom1", ""),
        ("Custom", "custom2", ""),
    ]
    dice_labels = ["d10", "d8", "d6", "d4", "0"]
    row_h = 10 * mm

    for label, key, hint in resources:
        y -= row_h
        canv.setFont('Body-Bold', 8)
        canv.drawString(col_res_x, y + 5, label)
        if hint:
            canv.setFont('Body-Italic', 6)
            canv.setFillColor(SUBTLE)
            canv.drawString(col_res_x, y - 1, hint)
            canv.setFillColor(INK)
        for idx, dl in enumerate(dice_labels):
            cx = col_dice_x + idx * col_dice_box_w
            display = "—" if dl == "0" else dl
            canv.setFont('Body', 6.5)
            canv.setFillColor(SUBTLE)
            canv.drawCentredString(cx + 3, y + 7.5, display)
            canv.setFillColor(INK)
            add_checkbox(canv, f"{key}_{dl}",
                         cx, y + 1, size=5,
                         tooltip=f"{label} = {display}")
        add_textfield(canv, f"{key}_notes",
                      col_notes_x, y + 1.5, col_notes_w, 7,
                      fontSize=7, tooltip=f"{label} notes")

    # Emergency packs
    y -= 18
    canv.setFont('Body-Bold', 8)
    canv.drawString(MARGIN_L, y, "EMERGENCY PACKS CARRIED")
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.4)
    canv.line(MARGIN_L, y - 2, PAGE_W - MARGIN_R, y - 2)
    y -= 4
    pack_items = [
        ("Battery Emergency Packs", "packs_battery"),
        ("O2 Auxiliary Tanks", "packs_o2"),
        ("Sealing Foam Patches", "packs_foam"),
    ]
    canv.setFont('Body', 8)
    for label, key in pack_items:
        y -= 8 * mm
        canv.drawString(MARGIN_L, y + 3, label)
        add_textfield(canv, key,
                      MARGIN_L + 50 * mm, y + 1,
                      (PAGE_W - MARGIN_R) - (MARGIN_L + 50 * mm), 7,
                      fontSize=7, tooltip=label)
    canv.restoreState()


# ============================================================ A.2
def page_ws_a2(canv, doc):
    draw_page_decoration(canv, doc)
    y_top = draw_ws_header(canv, "A.2", "Crew Roster",
        "Update station when crew moves. Mark Silent when contact fails.")
    canv.saveState()

    n_crew = 5

    # Row 1: NAME (36) | ROLE (26) | STATION (rest)
    name_w = 36 * mm
    role_w = 26 * mm
    station_x = MARGIN_L + name_w + role_w + 2 * mm
    station_w = (PAGE_W - MARGIN_R) - station_x

    # Row 2: SKILLS (56) | STRESS (28) | STATUS (rest)
    skills_w = 56 * mm
    stress_x = MARGIN_L + skills_w + 2 * mm
    stress_w = 28 * mm
    status_x = stress_x + stress_w + 2 * mm
    status_w = (PAGE_W - MARGIN_R) - status_x

    field_h = 8

    # Available vertical space
    avail_h = y_top - MARGIN_BOTTOM - 4
    block_h = avail_h / n_crew  # ~30mm per crew

    for c in range(n_crew):
        # Block top is at y_top - c*block_h
        block_top = y_top - c * block_h
        block_bottom = block_top - block_h

        # Row 1: label at top of block, field below
        label_y1 = block_top - 8
        field_y1 = label_y1 - 11

        # Row 2: positioned in lower half of block
        label_y2 = field_y1 - 14
        field_y2 = label_y2 - 11

        canv.setFont('Body-Bold', 6.5)
        canv.setFillColor(SUBTLE)
        canv.drawString(MARGIN_L, label_y1, "NAME")
        canv.drawString(MARGIN_L + name_w + 2 * mm, label_y1, "ROLE")
        canv.drawString(station_x, label_y1, "STATION")
        canv.setFillColor(INK)

        add_textfield(canv, f"crew{c+1}_name",
                      MARGIN_L, field_y1, name_w, field_h,
                      fontSize=8, tooltip=f"Crew {c+1} name")
        add_textfield(canv, f"crew{c+1}_role",
                      MARGIN_L + name_w + 2 * mm, field_y1, role_w - 2 * mm, field_h,
                      fontSize=7, tooltip=f"Crew {c+1} role")
        add_textfield(canv, f"crew{c+1}_station",
                      station_x, field_y1, station_w, field_h,
                      fontSize=7, tooltip=f"Crew {c+1} station")

        canv.setFont('Body-Bold', 6.5)
        canv.setFillColor(SUBTLE)
        canv.drawString(MARGIN_L, label_y2, "SKILLS")
        canv.drawString(stress_x, label_y2, "STRESS")
        canv.drawString(status_x, label_y2, "STATUS")
        canv.setFillColor(INK)

        add_textfield(canv, f"crew{c+1}_skills",
                      MARGIN_L, field_y2, skills_w, field_h,
                      fontSize=7, tooltip="Skills")
        add_textfield(canv, f"crew{c+1}_stress",
                      stress_x, field_y2, stress_w, field_h,
                      fontSize=7, tooltip="Steady / Strained / Breaking / Lost")
        add_textfield(canv, f"crew{c+1}_status",
                      status_x, field_y2, status_w, field_h,
                      fontSize=7, tooltip="On station / Moved / Silent / Dead")

        # Block separator (except after last block)
        if c < n_crew - 1:
            canv.setStrokeColor(SUBTLE)
            canv.setLineWidth(0.1)
            sep_y = block_bottom + 2
            canv.line(MARGIN_L, sep_y, PAGE_W - MARGIN_R, sep_y)
            canv.setStrokeColor(INK)
    canv.restoreState()


# ============================================================ A.3
def page_ws_a3(canv, doc):
    draw_page_decoration(canv, doc)
    y = draw_ws_header(canv, "A.3", "Section Map",
        "Sketch the section graph on a separate sheet. Track state below.")
    canv.saveState()

    sec_w = 48 * mm
    pwr_w = 20 * mm
    int_x = MARGIN_L + sec_w + pwr_w + 2 * mm
    int_w = 22 * mm
    atm_x = int_x + int_w + 2 * mm
    atm_w = (PAGE_W - MARGIN_R) - atm_x

    canv.setFont('Body-Bold', 7)
    canv.setFillColor(INK)
    canv.drawString(MARGIN_L, y, "SECTION")
    canv.drawString(MARGIN_L + sec_w + 2 * mm, y, "POWER")
    canv.drawString(int_x, y, "INTEGRITY")
    canv.drawString(atm_x, y, "ATMOS")
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.4)
    canv.line(MARGIN_L, y - 2, PAGE_W - MARGIN_R, y - 2)

    n_sections = 9
    field_h = 8
    for s in range(n_sections):
        y -= 9 * mm
        add_textfield(canv, f"section{s+1}_name",
                      MARGIN_L, y - 1, sec_w, field_h,
                      fontSize=8, tooltip=f"Section {s+1}")
        add_textfield(canv, f"section{s+1}_power",
                      MARGIN_L + sec_w + 2 * mm, y - 1, pwr_w - 2 * mm, field_h,
                      fontSize=7, tooltip="Nom / Brn / Dead")
        add_textfield(canv, f"section{s+1}_integrity",
                      int_x, y - 1, int_w, field_h,
                      fontSize=7, tooltip="Sealed / Comp / Vac / Flood")
        add_textfield(canv, f"section{s+1}_atmos",
                      atm_x, y - 1, atm_w, field_h,
                      fontSize=7, tooltip="Brth / Tox / Vac / Flood")

    # Recovery anchors
    y -= 18
    canv.setFont('Body-Bold', 8)
    canv.drawString(MARGIN_L, y, "RECOVERY ANCHORS")
    canv.setLineWidth(0.4)
    y -= 12

    sec_w2 = 36 * mm
    type_x = MARGIN_L + sec_w2 + 2 * mm
    type_w = 42 * mm
    clr_x = type_x + type_w + 2 * mm
    clr_w = 12 * mm
    state_x = clr_x + clr_w + 2 * mm
    state_w = (PAGE_W - MARGIN_R) - state_x

    canv.setFont('Body-Bold', 6.5)
    canv.drawString(MARGIN_L, y, "SECTION")
    canv.drawString(type_x, y, "TYPE")
    canv.drawString(clr_x, y, "CLR")
    canv.drawString(state_x, y, "STATE")
    canv.setLineWidth(0.3)
    canv.line(MARGIN_L, y - 2, PAGE_W - MARGIN_R, y - 2)

    n_anchors = 6
    for a in range(n_anchors):
        y -= 8 * mm
        add_textfield(canv, f"anchor{a+1}_section",
                      MARGIN_L, y - 1, sec_w2, field_h,
                      fontSize=7, tooltip="Section")
        add_textfield(canv, f"anchor{a+1}_type",
                      type_x, y - 1, type_w, field_h,
                      fontSize=7, tooltip="Recharge / O2 / Med / Galley / Ammo")
        add_textfield(canv, f"anchor{a+1}_clearance",
                      clr_x, y - 1, clr_w, field_h,
                      fontSize=7, tooltip="W / Y / R / G")
        add_textfield(canv, f"anchor{a+1}_state",
                      state_x, y - 1, state_w, field_h,
                      fontSize=7, tooltip="Last known state")
    canv.restoreState()


# ============================================================ A.4
def page_ws_a4(canv, doc):
    draw_page_decoration(canv, doc)
    y = draw_ws_header(canv, "A.4", "Code Log",
        "Strike through codes when wiped. Do not erase.")
    canv.saveState()

    code_w = 28 * mm
    opens_x = MARGIN_L + code_w + 2 * mm
    opens_w = 50 * mm
    found_x = opens_x + opens_w + 2 * mm
    found_w = 28 * mm
    valid_x = found_x + found_w + 2 * mm
    valid_w = (PAGE_W - MARGIN_R) - valid_x

    canv.setFont('Body-Bold', 7)
    canv.setFillColor(INK)
    canv.drawString(MARGIN_L, y, "CODE")
    canv.drawString(opens_x, y, "OPENS")
    canv.drawString(found_x, y, "FOUND AT")
    canv.drawString(valid_x, y, "VALID")
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.4)
    canv.line(MARGIN_L, y - 2, PAGE_W - MARGIN_R, y - 2)

    n_rows = 16
    field_h = 8
    for r in range(n_rows):
        y -= 9 * mm
        add_textfield(canv, f"code{r+1}_value",
                      MARGIN_L, y - 1, code_w, field_h,
                      fontSize=8, tooltip=f"Code {r+1}")
        add_textfield(canv, f"code{r+1}_opens",
                      opens_x, y - 1, opens_w, field_h,
                      fontSize=7, tooltip="What it opens")
        add_textfield(canv, f"code{r+1}_found",
                      found_x, y - 1, found_w, field_h,
                      fontSize=7, tooltip="Where found")
        add_checkbox(canv, f"code{r+1}_valid",
                     valid_x + 4, y, size=7,
                     tooltip="Valid? Uncheck if wiped")
    canv.restoreState()


# ============================================================ A.5
def page_ws_a5(canv, doc):
    draw_page_decoration(canv, doc)
    y = draw_ws_header(canv, "A.5", "Comms Log",
        "Brief lines. Radio chatter, not novel-writing.")
    canv.saveState()

    sc_w = 7 * mm
    time_x = MARGIN_L + sc_w + 1 * mm
    time_w = 11 * mm
    in_x = time_x + time_w + 1 * mm
    in_w = 50 * mm
    out_x = in_x + in_w + 1 * mm
    out_w = (PAGE_W - MARGIN_R) - out_x

    canv.setFont('Body-Bold', 7)
    canv.setFillColor(INK)
    canv.drawString(MARGIN_L, y, "SC")
    canv.drawString(time_x, y, "TIME")
    canv.drawString(in_x, y, "IN  (crew → char.)")
    canv.drawString(out_x, y, "OUT  (char. → crew)")
    canv.setStrokeColor(INK)
    canv.setLineWidth(0.4)
    canv.line(MARGIN_L, y - 2, PAGE_W - MARGIN_R, y - 2)

    n_rows = 17
    field_h = 8
    for r in range(n_rows):
        y -= 8.5 * mm
        add_textfield(canv, f"log{r+1}_scene",
                      MARGIN_L, y - 1, sc_w, field_h,
                      fontSize=7, tooltip="Scene #")
        add_textfield(canv, f"log{r+1}_time",
                      time_x, y - 1, time_w, field_h,
                      fontSize=7, tooltip="Time")
        add_textfield(canv, f"log{r+1}_in",
                      in_x, y - 1, in_w, field_h,
                      fontSize=7, tooltip="From crew")
        add_textfield(canv, f"log{r+1}_out",
                      out_x, y - 1, out_w, field_h,
                      fontSize=7, tooltip="From character")
    canv.restoreState()


# ============================================================ A.7
def page_ws_a7(canv, doc):
    draw_page_decoration(canv, doc)
    y = draw_ws_header(canv, "A.7", "Session Setup",
        "Fill in once per session, before play.")
    canv.saveState()

    fields = [
        ("STATION NAME", "setup_station", 1),
        ("OWNER / OPERATOR", "setup_owner", 1),
        ("LAYOUT TYPE", "setup_layout", 1),
        ("ENVIRONMENT", "setup_env", 1),
        ("CHARACTER", "setup_char", 1),
        ("CLASS", "setup_class", 1),
        ("DEFAULT CLEARANCE", "setup_clr", 1),
        ("TEMPORARY CLEARANCE", "setup_tempclr", 1),
        ("CONTRACT / SITUATION", "setup_contract", 3),
        ("ACTIVE PROTOCOLS", "setup_protocols", 2),
        ("COMPROMISE STAGE (private)", "setup_compromise", 1),
        ("PROGRESSION METHOD", "setup_prog", 1),
        ("INITIAL CHAOS FACTOR", "setup_chaos", 1),
        ("RECOVERY ANCHORS KNOWN", "setup_anchors", 2),
    ]
    avail_w = PAGE_W - MARGIN_R - MARGIN_L

    for label, key, lines in fields:
        canv.setFont('Body-Bold', 7)
        canv.setFillColor(SUBTLE)
        canv.drawString(MARGIN_L, y, label)
        for li in range(lines):
            y -= 12
            fname = f"{key}_{li+1}" if lines > 1 else key
            add_textfield(canv, fname,
                          MARGIN_L, y - 1, avail_w, 7,
                          fontSize=8, tooltip=label)
        y -= 12
    canv.restoreState()


# ============================================================ FILLER FLOWABLE
class WorksheetFiller(Flowable):
    """Consumes the entire frame so the page is reserved for canvas drawing."""
    def wrap(self, aW, aH):
        return (aW, aH)
    def draw(self):
        pass


# ============================================================ DOC
class CrewManualDoc(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, pagesize=A5,
            leftMargin=MARGIN_L, rightMargin=MARGIN_R,
            topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
            title="Crew Manual — A Solo-Play Supplement for Mothership",
            author="Crew Manual",
            **kwargs)
        frame_normal = Frame(MARGIN_L, MARGIN_BOTTOM, FRAME_W, FRAME_H,
            id='normal', leftPadding=0, rightPadding=0,
            topPadding=0, bottomPadding=0)
        frame_cover = Frame(MARGIN_L, MARGIN_BOTTOM, FRAME_W, FRAME_H,
            id='cover', leftPadding=0, rightPadding=0,
            topPadding=0, bottomPadding=0)
        frame_ws = Frame(MARGIN_L, MARGIN_BOTTOM, FRAME_W, FRAME_H,
            id='ws', leftPadding=0, rightPadding=0,
            topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='Cover', frames=[frame_cover], onPage=draw_cover_page),
            PageTemplate(id='Normal', frames=[frame_normal], onPage=draw_page_decoration),
            PageTemplate(id='WS_A1', frames=[frame_ws], onPage=page_ws_a1),
            PageTemplate(id='WS_A2', frames=[frame_ws], onPage=page_ws_a2),
            PageTemplate(id='WS_A3', frames=[frame_ws], onPage=page_ws_a3),
            PageTemplate(id='WS_A4', frames=[frame_ws], onPage=page_ws_a4),
            PageTemplate(id='WS_A5', frames=[frame_ws], onPage=page_ws_a5),
            PageTemplate(id='WS_A7', frames=[frame_ws], onPage=page_ws_a7),
        ])


# ============================================================ COVER
def build_cover_story():
    s = []
    s.append(Spacer(1, 28 * mm))
    s.append(Paragraph("A SOLO-PLAY SUPPLEMENT FOR", S['cover_super']))
    s.append(Paragraph("MOTHERSHIP", S['cover_super']))
    s.append(Spacer(1, 18 * mm))
    s.append(Paragraph("CREW", S['cover_title']))
    s.append(Paragraph("MANUAL", S['cover_title']))
    s.append(Spacer(1, 14 * mm))
    s.append(Paragraph(
        "Crew on the radio. Doors that won't open.<br/>"
        "Power that runs out. An AI that may be lying.",
        S['cover_sub']))
    s.append(Spacer(1, 32 * mm))
    s.append(Paragraph(
        "Resource Dice — Remote Crew — Section States — EVA — "
        "Station AI — Hot-Wire — System Compromise",
        S['cover_foot']))
    return s


# ============================================================ MAIN
def build_pdf(output_path):
    src_dir = Path("./chapters")
    chapter_files = sorted([f for f in src_dir.glob("crew_manual_ch*.md")])
    appendix_file = src_dir / "crew_manual_appendix_a.md"

    doc = CrewManualDoc(output_path)
    story = []

    # Cover
    story.extend(build_cover_story())
    story.append(NextPageTemplate('Normal'))
    story.append(PageBreak())

    # TOC
    story.append(HeaderUpdater("0", "Contents"))
    story.append(ChapterMarker("0", "Contents"))
    story.append(Spacer(1, 12))
    story.append(Paragraph("CONTENTS", S['chapter_title']))
    story.append(HeaderRule(thickness=1.0))
    story.append(Spacer(1, 12))
    chapter_titles = [
        "1.   Introduction & Core Loop",
        "2.   Resource Dice",
        "3.   Crew & Comms",
        "4.   Security Clearance",
        "5.   Power & Section Status",
        "6.   Section Integrity & Atmosphere",
        "7.   EVA & Submersion Operations",
        "8.   Station Protocols & Lockdown",
        "9.   Station AI",
        "10.  Hot-Wire & Power Sacrifice",
        "11.  System Compromise",
        "12.  Mythic GME Integration",
        "13.  Random Events",
        "14.  Resource Recovery",
        "Appendix A — Worksheet & Procedures",
    ]
    for ct in chapter_titles:
        story.append(Paragraph(ct, S['toc1']))

    # Body
    for f in chapter_files:
        text = f.read_text()
        # Strip trailing "--- + italic teaser" sequence (chapter outro lines)
        text = re.sub(r'\n---\s*\n+\*[^*\n]+\*\s*\n*\Z', '\n', text)
        parse_markdown(text, story)

    # Appendix A
    app_text = appendix_file.read_text()
    sections = re.split(r'(?m)^## ', app_text)
    intro = sections[0]
    parse_markdown(intro, story)

    for sec in sections[1:]:
        full = "## " + sec
        m = re.match(r'^## (A\.\d+)', full)
        sec_id = m.group(1) if m else None

        if sec_id in ('A.1', 'A.2', 'A.3', 'A.4', 'A.5'):
            tpl = f'WS_A{sec_id[-1]}'
            # Update outline / bookmark before form page
            story.append(SectionMarker(sec_id, _ws_title(sec_id), level=1))
            story.append(NextPageTemplate(tpl))
            story.append(PageBreak())
            story.append(WorksheetFiller())
            story.append(NextPageTemplate('Normal'))
        elif sec_id == 'A.7':
            story.append(SectionMarker(sec_id, "Session Setup", level=1))
            story.append(NextPageTemplate('WS_A7'))
            story.append(PageBreak())
            story.append(WorksheetFiller())
            story.append(NextPageTemplate('Normal'))
        else:
            parse_markdown(full, story)

    doc.build(story)
    print(f"Built: {output_path}")


def _ws_title(sec_id):
    return {
        'A.1': 'Resource Track',
        'A.2': 'Crew Roster',
        'A.3': 'Section Map',
        'A.4': 'Code Log',
        'A.5': 'Comms Log',
    }.get(sec_id, sec_id)


if __name__ == '__main__':
    build_pdf("crew_manual.pdf")
