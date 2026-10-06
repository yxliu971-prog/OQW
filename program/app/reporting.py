"""内存生成中文诊断 PDF：嵌入本机字体，所有用户文本先转义。"""

from datetime import timedelta, timezone
from functools import lru_cache
from hashlib import sha256
from html import escape
from io import BytesIO
from math import cos, pi, sin
from pathlib import Path
from threading import Lock

from reportlab.graphics.shapes import Circle, Drawing, Line, Polygon, String
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from chem_engine.metrics import DIMENSION_LABELS
from database.models import utc_now

INK = colors.HexColor("#183f38")
GREEN = colors.HexColor("#23856c")
MUTED = colors.HexColor("#65776f")
PALE = colors.HexColor("#eef5f1")
AMBER = colors.HexColor("#9a631c")
_font_lock = Lock()


@lru_cache(maxsize=8)
def _font(path: str | None) -> str:
    candidates = (
        [Path(path)]
        if path
        else [
            Path("C:/Windows/Fonts/simhei.ttf"),
            Path("C:/Windows/Fonts/simsun.ttc"),
            Path("/usr/share/fonts/truetype/noto/NotoSansSC-Regular.ttf"),
            Path("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"),
        ]
    )
    for candidate in candidates:
        if candidate.is_file():
            name = "OQW-CN-" + sha256(str(candidate).encode()).hexdigest()[:10]
            with _font_lock:
                if name not in pdfmetrics.getRegisteredFontNames():
                    pdfmetrics.registerFont(TTFont(name, str(candidate), subfontIndex=0))
            return name
    raise FileNotFoundError("未找到中文 TrueType 字体，请配置 OQW_PDF_FONT")


def _display(value, digits=2):
    if value is None:
        return "未评估"
    return f"{value:.{digits}f}" if isinstance(value, (int, float)) else str(value)


def _radar(dimensions: dict, font: str) -> Drawing:
    drawing = Drawing(252, 218)
    cx, cy, radius = 126, 110, 69
    labels = list(DIMENSION_LABELS.values())
    values = list(dimensions[key] for key in DIMENSION_LABELS)
    # 与 ECharts 的逆时针维度顺序保持一致，便于屏幕与报告核对。
    angles = [pi / 2 + index * pi / 3 for index in range(6)]
    for level in (0.25, 0.5, 0.75, 1):
        points = [
            coord
            for angle in angles
            for coord in (cx + radius * level * cos(angle), cy + radius * level * sin(angle))
        ]
        drawing.add(
            Polygon(
                points, fillColor=None, strokeColor=colors.HexColor("#dce7e0"), strokeWidth=0.65
            )
        )
    for angle, label in zip(angles, labels, strict=True):
        drawing.add(
            Line(
                cx,
                cy,
                cx + radius * cos(angle),
                cy + radius * sin(angle),
                strokeColor=colors.HexColor("#dce7e0"),
                strokeWidth=0.65,
            )
        )
        drawing.add(
            String(
                cx + 101 * cos(angle),
                cy + 91 * sin(angle) - 3,
                label,
                fontName=font,
                fontSize=8,
                textAnchor="middle",
                fillColor=MUTED,
            )
        )
    if all(value is not None for value in values):
        points = [
            coord
            for angle, value in zip(angles, values, strict=True)
            for coord in (
                cx + radius * value / 100 * cos(angle),
                cy + radius * value / 100 * sin(angle),
            )
        ]
        drawing.add(
            Polygon(
                points, fillColor=colors.HexColor("#d3ebe0"), strokeColor=GREEN, strokeWidth=1.6
            )
        )
        for index in range(0, len(points), 2):
            drawing.add(
                Circle(points[index], points[index + 1], 2.3, fillColor=GREEN, strokeColor=None)
            )
    else:
        drawing.add(
            String(
                cx,
                cy - 3,
                "部分维度未评估",
                fontName=font,
                fontSize=9,
                textAnchor="middle",
                fillColor=AMBER,
            )
        )
    return drawing


def build_report(
    evaluation: dict, result: dict, *, font_path: Path | None = None, snapshot: bool = True
) -> bytes:
    """只接收服务器计算结果/历史快照，不信任客户端上传的分数或图像。"""
    font = _font(str(font_path) if font_path else None)
    stream = BytesIO()
    width = A4[0] - 36 * mm
    styles = {
        "body": ParagraphStyle(
            "body",
            fontName=font,
            fontSize=9,
            leading=14,
            textColor=INK,
            wordWrap="CJK",
            splitLongWords=True,
            spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "small",
            fontName=font,
            fontSize=8,
            leading=12,
            textColor=MUTED,
            wordWrap="CJK",
            splitLongWords=True,
        ),
        "title": ParagraphStyle(
            "title", fontName=font, fontSize=23, leading=31, textColor=INK, spaceAfter=8
        ),
        "heading": ParagraphStyle(
            "heading",
            fontName=font,
            fontSize=12,
            leading=19,
            textColor=INK,
            spaceBefore=12,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "number": ParagraphStyle(
            "number", fontName=font, fontSize=23, leading=31, alignment=TA_CENTER, textColor=INK
        ),
    }

    def p(value, style="body"):
        return Paragraph(escape(str(value)).replace("\n", "<br/>"), styles[style])

    def table(headers, rows, widths=None):
        data = [[p(cell, "small") for cell in headers]] + [
            [p(cell, "small") for cell in row] for row in rows
        ]
        item = Table(
            data, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1, splitInRow=1
        )
        item.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), PALE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.HexColor("#c6dacf")),
                    ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#e1e9e3")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 9),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )
        return item

    created = (
        utc_now().astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M UTC+08:00")
    )
    identifier = result.get("evaluation_id") or "未保存评估"
    score = result["score"]
    story = [
        p("OQW  /  GREEN CHEMISTRY", "small"),
        Spacer(1, 7 * mm),
        p("绿色化学诊断报告", "title"),
        p("可解释指标 · 数据来源可追溯 · 本地生成", "small"),
        Spacer(1, 5 * mm),
    ]
    if result.get("demo_only"):
        story.append(
            table(
                ["合成数据演示"],
                [["本报告使用合成溶剂/危害示例，仅用于功能验证，不可作为真实实验或法规判断依据。"]],
                [width],
            )
        )
    story.extend(
        [
            p(f"报告生成：{created}", "small"),
            p(f"评估编号：{identifier}", "small"),
            p(f"评估时间：{result['evaluated_at']}（原始 UTC 时间）", "small"),
            p("01  评估概览", "heading"),
        ]
    )
    metrics = result["metrics"]
    cards = Table(
        [
            [
                p(_display(score["overall_score"]), "number"),
                p(_display(metrics["atom_economy"]) + "%", "number"),
                p(_display(metrics["rme"]) + "%", "number"),
                p(_display(metrics["e_factor"]), "number"),
            ],
            [
                p("OQW 综合分 / 100", "small"),
                p("原子经济性 AE", "small"),
                p("质量效率 RME", "small"),
                p("E-Factor", "small"),
            ],
        ],
        colWidths=[width / 4] * 4,
    )
    cards.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE),
                ("TOPPADDING", (0, 0), (-1, 0), 12),
                ("BOTTOMPADDING", (0, -1), (-1, -1), 12),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )
    story.extend(
        [
            cards,
            Spacer(1, 3 * mm),
            p(
                f"权重覆盖率 {score['coverage'] * 100:.0f}% · "
                f"{'部分评估' if score['status'] == 'partial' else '已启用维度完整'} · "
                f"规则 {score['scoring_version']}",
                "small",
            ),
            p("02  六维绿色指标", "heading"),
        ]
    )
    dimension_table = table(
        ["维度", "得分 / 100"],
        [
            [label, _display(score["dimension_scores"][key])]
            for key, label in DIMENSION_LABELS.items()
        ],
        [135, width - 260 - 135],
    )
    chart = Table(
        [[_radar(score["dimension_scores"], font), dimension_table]], colWidths=[260, width - 260]
    )
    chart.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.extend(
        [
            chart,
            p(
                "缺失维度不填零、不连成闭合图形。综合分为已有维度的归一化加权平均，比较时应保持相同规则与覆盖率。",
                "small",
            ),
            PageBreak(),
            p("03  配方与质量边界", "heading"),
        ]
    )
    unit = evaluation.get("mass_unit", "g")
    input_rows = [
        [
            f"反应物 {index}",
            item["smiles"],
            f"{_display(item['mass'], 4)} {unit}",
            _display(item.get("coefficient", 1), 4),
        ]
        for index, item in enumerate(evaluation["reactants"], 1)
    ]
    item = evaluation["product"]
    input_rows.append(
        [
            "目标产物",
            item["smiles"],
            f"{_display(item['mass'], 4)} {unit}",
            _display(item.get("coefficient", 1), 4),
        ]
    )
    story.append(
        table(
            ["物料", "SMILES", "实际质量", "计量系数"],
            input_rows,
            [65, width - 65 - 90 - 65, 90, 65],
        )
    )
    if evaluation.get("solvents"):
        story.extend(
            [
                Spacer(1, 3 * mm),
                table(
                    ["溶剂标识", "质量"],
                    [
                        [
                            item.get("cas") or item.get("name"),
                            "未提供"
                            if item.get("mass") is None
                            else f"{_display(item['mass'], 4)} {unit}",
                        ]
                        for item in evaluation["solvents"]
                    ],
                    [width - 100, 100],
                ),
            ]
        )
    story.extend(
        [
            Spacer(1, 3 * mm),
            p(
                f"废弃物质量：{_display(evaluation.get('total_waste_mass'), 4)} "
                f"{unit if evaluation.get('total_waste_mass') is not None else ''}"
            ),
            p(f"废物流边界：{evaluation.get('waste_boundary') or '未声明，E-Factor 未评估'}"),
            p("04  溶剂预警与数据缺口", "heading"),
        ]
    )
    for warning in result.get("solvent_warnings", []):
        severity = {"danger": "高关注", "warning": "需关注", "info": "信息"}.get(
            warning["severity"], "信息"
        )
        story.append(
            p(
                f"[{severity}] {warning.get('name') or warning.get('cas') or '未知溶剂'}："
                f"{warning['message']}"
            )
        )
        if warning.get("ghs_codes"):
            story.append(p("GHS：" + "、".join(warning["ghs_codes"]), "small"))
        if warning.get("conditions"):
            story.append(p("适用条件：" + warning["conditions"], "small"))
    if not result.get("solvent_warnings"):
        story.append(p("本次未返回溶剂预警；这不等于已证明无危害。"))
    for note in result.get("data_notes", []):
        story.append(p(note, "small"))
    story.append(p("05  方法与数据来源", "heading"))
    story.append(
        p(
            "AE 根据 RDKit 平均摩尔质量和理论配平系数计算；RME 使用实际反应物质量；"
            "E-Factor 使用声明边界内的废弃物质量。OQW 综合评分是自定义辅助规则，"
            "不是 GSK/ACS 官方认证。"
        )
    )
    story.append(
        p(
            f"E-Factor 半分参数：{score['method']['e_factor_half_score']}；原始权重："
            + "，".join(
                f"{DIMENSION_LABELS[key]} {value:.0%}" for key, value in score["weights"].items()
            ),
            "small",
        )
    )
    for name, key in (("能源效率", "energy_assessment"), ("工艺安全", "process_safety_assessment")):
        if evaluation.get(key):
            value = evaluation[key]
            story.append(p(f"{name}外部评分：{value['score']}；依据：{value['basis']}", "small"))
    sources = {}
    for fields in result.get("dataset_versions", {}).get("solvents", {}).values():
        for source in fields.values():
            sources[(source.get("source_id"), source.get("version"))] = source
    for source in result.get("dataset_versions", {}).get("hazards", {}).values():
        sources[(source.get("source_id"), source.get("version"))] = source
    for (source_id, version), source in sources.items():
        story.append(p(f"{source_id} · 版本 {version}", "body"))
        for field, label in (
            ("location", "出处"),
            ("license", "许可/使用条款"),
            ("score_method", "评分口径"),
        ):
            if source.get(field):
                story.append(p(f"{label}：{source[field]}", "small"))
    if not sources:
        story.append(p("本次未使用可匹配的公开溶剂/危害数据。", "small"))
    story.extend(
        [
            Spacer(1, 4 * mm),
            p(
                "报告来源：已保存评估快照，未重新计算。"
                if snapshot
                else "报告来源：按提交配方和导出时的数据库重新评估；未增加历史记录。",
                "small",
            ),
            p(
                "质量指标不能替代反应可行性、工艺风险或法规适用性评审；HSP 候选仍需实验验证。",
                "small",
            ),
        ]
    )

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#d3dfd7"))
        canvas.line(18 * mm, 16 * mm, A4[0] - 18 * mm, 16 * mm)
        canvas.setFont(font, 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 11 * mm, "OQW 绿色化学诊断报告  |  本地生成")
        canvas.drawRightString(A4[0] - 18 * mm, 11 * mm, f"第 {doc.page} 页")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        stream,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=23 * mm,
        title="OQW 绿色化学诊断报告",
        author="OQW",
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return stream.getvalue()
