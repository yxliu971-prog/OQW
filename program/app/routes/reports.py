"""诊断报告导出：历史快照或服务器重新评估，禁止伪造客户端分数。"""

from urllib.parse import quote

from fastapi import APIRouter, Request, Response

from database.models import UserEvaluations

from ..dependencies import DBSession
from ..errors import APIError
from ..reporting import build_report
from ..schemas import ReportRequest
from ..services import evaluate_reaction

router = APIRouter(tags=["PDF 报告"])


@router.post(
    "/reports/pdf",
    summary="导出中文绿色化学诊断报告",
    response_class=Response,
    responses={
        200: {"content": {"application/pdf": {"schema": {"type": "string", "format": "binary"}}}}
    },
)
def export_pdf(payload: ReportRequest, request: Request, session: DBSession):
    if payload.evaluation_id:
        history = session.get(UserEvaluations, payload.evaluation_id)
        if history is None:
            raise APIError(404, "evaluation_not_found", "评估记录不存在，请重新评估")
        evaluation, result = history.amounts, history.evaluation_result
    else:
        evaluation = payload.evaluation.model_dump()
        result = evaluate_reaction(
            session, payload.evaluation, allow_demo=request.app.state.settings.allow_demo
        )
    try:
        content = build_report(
            evaluation,
            result,
            font_path=request.app.state.settings.pdf_font_path,
            snapshot=payload.evaluation_id is not None,
        )
    except FileNotFoundError as exc:
        raise APIError(503, "pdf_font_unavailable", str(exc)) from exc
    filename = quote("OQW绿色化学诊断报告.pdf")
    return Response(
        content=content,
        media_type="application/pdf",
        headers={
            "Content-Disposition": (
                f"attachment; filename=oqw-green-report.pdf; filename*=UTF-8''{filename}"
            ),
            "Cache-Control": "no-store",
            "X-Content-Type-Options": "nosniff",
        },
    )
