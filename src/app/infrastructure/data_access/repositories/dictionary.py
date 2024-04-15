from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.dictionary.entities import DictionaryItem
from app.domain.dictionary.repositories import DictionaryItemRepository
from app.domain.dictionary.value_objects import Language, Original
from app.infrastructure.data_access.models import DictionaryItemDb


class SqlalchemyDictionaryItemRepository(DictionaryItemRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_list_items(
        self, limit: int = 20, offset: int = 0, language: Language | None = None
    ) -> list[DictionaryItem]:
        query = select(DictionaryItemDb).limit(limit).offset(offset)

        if language:
            query = query.where(DictionaryItemDb.original_language == language.to_raw())

        items_result = await self.session.execute(query)

        return [item.to_entity() for item in items_result.scalars()]

    async def get_translations(
        self,
        original: Original,
        original_language: Language,
        translation_language: Language,
        limit: int = 20,
        offset: int = 0,
    ) -> list[DictionaryItem]:
        query = (
            select(DictionaryItemDb)
            .where(
                DictionaryItemDb.original.like(f"%{original.to_raw().lower()}%"),
                DictionaryItemDb.original_language == original_language.to_raw(),
                DictionaryItemDb.translation_language == translation_language.to_raw(),
            )
            .limit(limit)
            .offset(offset)
        )
        items_result = await self.session.execute(query)

        return [item.to_entity() for item in items_result.scalars()]
