from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends, HTTPException

from app.application.contracts.dictionary.request import (
    GetItemsByLanguageRequest,
    LimitOffsetRequest,
    SearchItemsRequest,
)
from app.application.contracts.dictionary.response import ListItemsResponse
from app.application.usecases.dictionary import (
    GetItemsByLanguage,
    GetListItems,
    SearchItems,
)

dictionary_router = APIRouter(
    prefix="/dictionary", tags=["dictionary"], route_class=DishkaRoute
)


@dictionary_router.get("/", response_model=ListItemsResponse)
async def get_list_items(
    request: Annotated[LimitOffsetRequest, Depends()],
    interactor: FromDishka[GetListItems],
) -> ListItemsResponse:
    if request.limit >= 100:
        raise HTTPException(
            status_code=400,
            detail="Limit cannot be greater than 100",
        )

    return await interactor(request)


@dictionary_router.get("/search", response_model=ListItemsResponse)
async def search_items(
    request: Annotated[SearchItemsRequest, Depends()],
    interactor: FromDishka[SearchItems],
) -> ListItemsResponse:
    if request.limit >= 100:
        raise HTTPException(
            status_code=400,
            detail="Limit cannot be greater than 100",
        )

    return await interactor(request)


@dictionary_router.get("/{language}", response_model=ListItemsResponse)
async def get_items_by_language(
    language: str,
    request: Annotated[LimitOffsetRequest, Depends()],
    interactor: FromDishka[GetItemsByLanguage],
) -> ListItemsResponse:
    if request.limit >= 100:
        raise HTTPException(
            status_code=400,
            detail="Limit cannot be greater than 100",
        )

    return await interactor(
        GetItemsByLanguageRequest(
            language=language,
            limit=request.limit,
            offset=request.offset,
        )
    )
