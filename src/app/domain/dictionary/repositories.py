from typing import Protocol

from app.domain.dictionary.entities import DictionaryItem
from app.domain.dictionary.value_objects import Language, Original


class DictionaryItemRepository(Protocol):
    async def get_list_items(
        self,
        limit: int = 20,
        offset: int = 0,
        language: Language | None = None,
    ) -> list[DictionaryItem]:
        raise NotImplementedError

    async def get_translations(
        self,
        original: Original,
        original_language: Language,
        translation_language: Language,
        limit: int = 20,
        offset: int = 0,
    ) -> list[DictionaryItem]:
        raise NotImplementedError
