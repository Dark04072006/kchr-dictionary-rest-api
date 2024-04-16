from typing import Any, AsyncIterable, Awaitable, Callable, Coroutine, cast

import httpx
import pytest_asyncio

from app.main.web_api import create_app

_Message = dict[str, Any]
_Receive = Callable[[], Awaitable[_Message]]
_Send = Callable[[dict[str, Any]], Coroutine[None, None, None]]
_ASGIApp = Callable[[dict[str, Any], _Receive, _Send], Coroutine[None, None, None]]


@pytest_asyncio.fixture
async def client() -> AsyncIterable[httpx.AsyncClient]:
    app = cast(_ASGIApp, create_app())
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(
        transport=transport, base_url="http://testserver"
    ) as client:
        yield client
