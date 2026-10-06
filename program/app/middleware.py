"""在 JSON / multipart 解析前限制请求体，并拒绝含歧义的 JSON。"""

from fastapi.responses import JSONResponse

from database.validation import strict_json

from .errors import error_content


class BodyLimitMiddleware:
    def __init__(self, app, max_bytes: int):
        self.app = app
        self.max_bytes = max_bytes

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or scope["method"] not in ("POST", "PUT", "PATCH"):
            return await self.app(scope, receive, send)
        headers = dict(scope["headers"])
        try:
            declared = int(headers.get(b"content-length", b"0"))
            if declared < 0:
                raise ValueError("negative length")
        except ValueError:
            response = JSONResponse(
                status_code=400,
                content=error_content("invalid_content_length", "Content-Length 无效"),
            )
            return await response(scope, receive, send)
        body = bytearray()
        if declared <= self.max_bytes:
            while True:
                message = await receive()
                if message["type"] == "http.disconnect":
                    return
                body.extend(message.get("body", b""))
                if len(body) > self.max_bytes or not message.get("more_body", False):
                    break
        if declared > self.max_bytes or len(body) > self.max_bytes:
            response = JSONResponse(
                status_code=413,
                content=error_content("request_too_large", "请求体超过服务配置上限"),
            )
            return await response(scope, receive, send)
        content_type = headers.get(b"content-type", b"").split(b";", 1)[0].lower()
        if body and (
            not content_type
            or content_type == b"application/json"
            or content_type.endswith(b"+json")
        ):
            try:
                strict_json(body.decode("utf-8-sig"))
            except (ValueError, RecursionError, OverflowError):
                response = JSONResponse(
                    status_code=400,
                    content=error_content(
                        "invalid_json", "JSON 格式无效、重复键、嵌套过深或包含非有限数"
                    ),
                )
                return await response(scope, receive, send)
        consumed = False

        async def buffered_receive():
            nonlocal consumed
            if not consumed:
                consumed = True
                return {"type": "http.request", "body": bytes(body), "more_body": False}
            return await receive()

        return await self.app(scope, buffered_receive, send)
