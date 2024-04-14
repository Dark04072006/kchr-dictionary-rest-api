from dataclasses import dataclass, field

from app.domain.dictionary.entities import DictionaryItem


@dataclass(frozen=True)
class ItemResponse:
    id: int
    original: str
    translation: str
    original_language: str
    translation_language: str

    @staticmethod
    def from_entity(entity: DictionaryItem) -> "ItemResponse":
        return ItemResponse(
            id=entity.id.to_raw(),
            original=entity.original.to_raw(),
            translation=entity.translation.to_raw(),
            original_language=entity.original_language.to_raw(),
            translation_language=entity.translation_language.to_raw(),
        )


@dataclass(frozen=True)
class ListItemsResponse:
    data: list[ItemResponse] = field(default_factory=list)

    @staticmethod
    def from_entity_list(entity_list: list[DictionaryItem]) -> "ListItemsResponse":
        data = map(ItemResponse.from_entity, entity_list)

        return ListItemsResponse(list(data))
