# Middleware definitions

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Custom Value"
        return response


# More middleware classes can be added here
