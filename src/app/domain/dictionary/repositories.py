from typing import Protocol

from app.domain.dictionary.entities import DictionaryItem
from app.domain.dictionary.value_objects import Language, Original


class DictionaryItemRepository(Protocol):
    async def get_all_items(
        self, limit: int = 20, offset: int = 0
    ) -> list[DictionaryItem]:
        raise NotImplementedError

    async def search_translation(
        self,
        original: Original,
        original_language: Language,
        translation_language: Language,
        limit: int = 20,
        offset: int = 0,
    ) -> list[DictionaryItem]:
        raise NotImplementedError

    async def get_all_by_language(
        self, language: Language, limit: int = 20, offset: int = 0
    ) -> list[DictionaryItem]:
        raise NotImplementedError
