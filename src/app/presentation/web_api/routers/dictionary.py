from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends

from app.application.contracts.dictionary.request import (
    GetItemsRequest,
    GetTranlationsRequest,
)
from app.application.contracts.dictionary.response import ListItemsResponse
from app.application.usecases.dictionary import GetItems, GetTranslations
from app.presentation.web_api.schemas.items import GetItemsSchema
from app.presentation.web_api.schemas.translations import GetTranslationsSchema

dictionary_router = APIRouter(tags=["dictionary"], route_class=DishkaRoute)


@dictionary_router.get(
    "/items",
    response_model=ListItemsResponse,
    description="Retrieves a list of dictionary items.",
)
async def get_list_items(
    schema: Annotated[GetItemsSchema, Depends()],
    interactor: FromDishka[GetItems],
) -> ListItemsResponse:
    return await interactor(
        GetItemsRequest(
            limit=schema.limit,
            offset=schema.offset,
            language=schema.language,
        )
    )


@dictionary_router.get(
    "/translations",
    response_model=ListItemsResponse,
    description="Searches for translations of a given word/phrase.",
)
async def get_translations(
    schema: Annotated[GetTranslationsSchema, Depends()],
    interactor: FromDishka[GetTranslations],
) -> ListItemsResponse:
    return await interactor(
        GetTranlationsRequest(
            original=1,
            original_language=schema.original_language,
            translation_language=schema.translation_language,
            limit=schema.limit,
            offset=schema.offset,
        )
    )
