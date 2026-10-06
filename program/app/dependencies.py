"""请求级数据库会话和受控同步鉴权。"""

import secrets
from typing import Annotated

from fastapi import Depends, Request, Security
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from .errors import APIError

admin_key_header = APIKeyHeader(name="X-OQW-Admin-Key", auto_error=False)


def get_session(request: Request):
    with Session(request.app.state.engine) as session:
        yield session  # 未显式 commit 的请求在 close 时回滚。


DBSession = Annotated[Session, Depends(get_session)]


def require_sync_admin(
    request: Request, key: Annotated[str | None, Security(admin_key_header)] = None
):
    expected = request.app.state.settings.sync_api_key
    if expected is None:
        raise APIError(
            503, "sync_not_configured", "同步接口未启用：服务器尚未配置 OQW_SYNC_API_KEY"
        )
    if key is None or not secrets.compare_digest(
        key.encode(), expected.get_secret_value().encode()
    ):
        raise APIError(401, "invalid_admin_key", "同步接口需要有效的 X-OQW-Admin-Key")
