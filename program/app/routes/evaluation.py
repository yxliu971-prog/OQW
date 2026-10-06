"""单次反应评估与配方 CSV 批量诊断。"""

from typing import Annotated

from fastapi import APIRouter, File, Query, Request, UploadFile
from pydantic import ValidationError

from ..dependencies import DBSession
from ..errors import APIError, error_content, validation_details
from ..importer import parse_csv, row_to_request
from ..schemas import EvaluationRequest, EvaluationResponse, ImportResponse
from ..services import evaluate_reaction, persist_evaluation

router = APIRouter(tags=["绿色评估"])


@router.post(
    "/evaluate", response_model=EvaluationResponse, summary="计算反应绿色指标并按需保存历史"
)
def evaluate(payload: EvaluationRequest, request: Request, session: DBSession):
    result = evaluate_reaction(session, payload, allow_demo=request.app.state.settings.allow_demo)
    if payload.persist:
        persist_evaluation(session, payload, result)
        session.commit()
    return result


@router.post("/import-user-data", response_model=ImportResponse, summary="上传配方 CSV，逐行诊断")
def import_user_data(
    request: Request,
    session: DBSession,
    file: Annotated[UploadFile, File(description="UTF-8 CSV，每行一个反应")],
    persist: Annotated[bool, Query(description="是否保存成功行；无效行不写入")] = True,
):
    settings = request.app.state.settings
    try:
        if not file.filename or not file.filename.lower().endswith(".csv"):
            raise APIError(415, "unsupported_file", "此接口仅接受 .csv 配方文件")
        content = file.file.read(settings.max_upload_bytes + 1)
    finally:
        file.file.close()
    if len(content) > settings.max_upload_bytes:
        raise APIError(413, "file_too_large", "上传 CSV 超过文件大小限制")
    rows = parse_csv(content, settings.max_csv_rows)
    responses, successful = [], []
    for index, (line_end, row) in enumerate(rows, start=1):
        item = {"row_index": index, "csv_line_end": line_end, "record_id": row.get("record_id")}
        try:
            payload = EvaluationRequest.model_validate(row_to_request(row, persist))
            result = evaluate_reaction(session, payload, allow_demo=settings.allow_demo)
            successful.append((payload, result))
            item.update(status="success", result=result, evaluation_input=payload.model_dump())
        except ValidationError as exc:
            item.update(
                status="failed",
                **error_content("validation_error", "该行字段校验失败", validation_details(exc)),
            )
        except APIError as exc:
            item.update(status="failed", **error_content(exc.code, exc.message, exc.details))
        except (ValueError, KeyError, OverflowError) as exc:
            item.update(status="failed", **error_content("invalid_csv_row", str(exc)))
        responses.append(item)
    # 先完成所有诊断，再提交全部成功行；数据库故障时不返回虚假的已保存 ID。
    if persist and successful:
        for payload, result in successful:
            persist_evaluation(session, payload, result, input_format="csv")
        session.commit()
    return {
        "total_rows": len(rows),
        "successful_rows": len(successful),
        "failed_rows": len(rows) - len(successful),
        "persisted_rows": len(successful) if persist else 0,
        "rows": responses,
    }
