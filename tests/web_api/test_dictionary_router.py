from typing import Any, AsyncIterable, Awaitable, Callable, Coroutine, cast

import httpx
import pytest
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


@pytest.mark.asyncio
async def test_get_list_items_success(client: httpx.AsyncClient) -> None:
    response = await client.get("/items")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_list_items_fail(client: httpx.AsyncClient) -> None:
    response = await client.post("/items")

    assert response.status_code == 405


@pytest.mark.asyncio
async def test_get_list_items_by_lang(client: httpx.AsyncClient) -> None:
    response = await client.get("/items", params={"language": "CS"})

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_translations_success(client: httpx.AsyncClient) -> None:
    response = await client.get(
        "/translations",
        params={
            "original": "Привет",
            "original_language": "RUSS",
            "translation_language": "CS",
        },
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_translations_fail(client: httpx.AsyncClient) -> None:
    response = await client.post(
        "/translations",
        params={
            "original": "Привет",
            "original_language": "RUSS",
            "translation_language": "CS",
        },
    )

    assert response.status_code == 405
