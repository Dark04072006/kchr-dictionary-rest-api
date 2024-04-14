from app.application.contracts.dictionary.request import (
    GetItemsByLanguageRequest,
    LimitOffsetRequest,
    SearchItemsRequest,
)
from app.application.contracts.dictionary.response import ListItemsResponse
from app.application.protocols.interactor import Interactor
from app.domain.dictionary.repositories import DictionaryItemRepository
from app.domain.dictionary.value_objects import Language, Original


class GetListItems(Interactor[LimitOffsetRequest, ListItemsResponse]):
    def __init__(self, item_repository: DictionaryItemRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: LimitOffsetRequest) -> ListItemsResponse:
        items = await self.item_repository.get_all_items(request.limit, request.offset)

        return ListItemsResponse.from_entity_list(items)


class SearchItems(Interactor[SearchItemsRequest, ListItemsResponse]):
    def __init__(self, item_repository: DictionaryItemRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: SearchItemsRequest) -> ListItemsResponse:
        items = await self.item_repository.search_translation(
            Original(request.original),
            Language(request.original_language),
            Language(request.translation_language),
            request.limit,
            request.offset,
        )

        return ListItemsResponse.from_entity_list(items)


class GetItemsByLanguage(Interactor[GetItemsByLanguageRequest, ListItemsResponse]):
    def __init__(self, item_repository: DictionaryItemRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: GetItemsByLanguageRequest) -> ListItemsResponse:
        items = await self.item_repository.get_all_by_language(
            Language(request.language), request.limit, request.offset
        )

        return ListItemsResponse.from_entity_list(items)
