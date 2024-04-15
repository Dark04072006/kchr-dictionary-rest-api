from app.application.contracts.dictionary.request import (
    GetItemsRequest,
    GetTranlationsRequest,
)
from app.application.contracts.dictionary.response import ListItemsResponse
from app.application.protocols.interactor import Interactor
from app.domain.common.exceptions import DomainValidationError
from app.domain.dictionary.repositories import DictionaryItemRepository
from app.domain.dictionary.value_objects import Language, Original


class GetItems(Interactor[GetItemsRequest, ListItemsResponse]):
    def __init__(self, item_repository: DictionaryItemRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: GetItemsRequest) -> ListItemsResponse:
        language = Language(request.language) if request.language else None

        items = await self.item_repository.get_list_items(
            request.limit,
            request.offset,
            language,
        )

        return ListItemsResponse.from_entity_list(items)


class GetTranslations(Interactor[GetTranlationsRequest, ListItemsResponse]):
    def __init__(self, item_repository: DictionaryItemRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: GetTranlationsRequest) -> ListItemsResponse:
        if request.original_language == request.translation_language:
            raise DomainValidationError(
                "Original and translation languages cannot be the same."
            )

        items = await self.item_repository.get_translations(
            Original(request.original),
            Language(request.original_language),
            Language(request.translation_language),
            request.limit,
            request.offset,
        )

        return ListItemsResponse.from_entity_list(items)
