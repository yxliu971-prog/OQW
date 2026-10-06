"""统一错误结构，不回显数据库参数、HTTP 令牌或完整配方。"""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException


class APIError(Exception):
    def __init__(self, status: int, code: str, message: str, details=None):
        self.status = status
        self.code = code
        self.message = message
        self.details = details
        super().__init__(message)


def validation_details(exc):
    return [
        {"location": list(error["loc"]), "message": error["msg"], "type": error["type"]}
        for error in exc.errors()
    ]


def error_content(code: str, message: str, details=None) -> dict:
    return {"error": {"code": code, "message": message, "details": details}}


def install_handlers(app: FastAPI):
    @app.exception_handler(APIError)
    async def domain_error(request: Request, exc: APIError):
        return JSONResponse(
            status_code=exc.status, content=error_content(exc.code, exc.message, exc.details)
        )

    @app.exception_handler(RequestValidationError)
    async def invalid_request(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content=error_content("validation_error", "请求字段校验失败", validation_details(exc)),
        )

    @app.exception_handler(SQLAlchemyError)
    async def database_error(request: Request, exc: SQLAlchemyError):
        return JSONResponse(
            status_code=503,
            content=error_content("database_error", "数据库操作失败，本次写入未提交"),
        )

    @app.exception_handler(HTTPException)
    async def http_error(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            headers=exc.headers,
            content=error_content("http_error", str(exc.detail)),
        )

    @app.exception_handler(Exception)
    async def unexpected_error(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=error_content("internal_error", "内部处理失败，请查看本地服务状态"),
        )
