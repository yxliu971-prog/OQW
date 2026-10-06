"""替换推荐与基于用户报价的处置成本比较。"""

from fastapi import APIRouter, Request

from ..dependencies import DBSession
from ..schemas import SwapRequest, SwapResponse
from ..services import recommend_swap

router = APIRouter(tags=["绿色替换"])


@router.post("/recommend-swap", response_model=SwapResponse, summary="按 HSP 排序绿色替换候选")
def recommend(payload: SwapRequest, request: Request, session: DBSession):
    return recommend_swap(session, payload, allow_demo=request.app.state.settings.allow_demo)
