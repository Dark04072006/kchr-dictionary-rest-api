import httpx
import pytest


@pytest.mark.asyncio
async def test_health_status_success_endpoint(client: httpx.AsyncClient) -> None:
    response = await client.get("/health-check/")

    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}
    assert response.headers["Content-Type"] == "application/json"


@pytest.mark.asyncio
async def test_health_status_fail_endpoint(client: httpx.AsyncClient) -> None:
    response = await client.post("/health-check/")

    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
    assert response.headers["Content-Type"] == "application/json"
