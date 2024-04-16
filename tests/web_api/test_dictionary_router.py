import httpx
import pytest


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
