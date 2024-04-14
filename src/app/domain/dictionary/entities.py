from dataclasses import dataclass

from app.domain.common.entities import Entity
from app.domain.dictionary.value_objects import (
    DictionaryItemId,
    Language,
    LanguageT,
    Original,
    Translation,
)


@dataclass
class DictionaryItem(Entity[DictionaryItemId]):
    original: Original
    translation: Translation
    original_language: Language
    translation_language: Language

    @staticmethod
    def create(
        id: int,
        original: str,
        translation: str,
        original_language: LanguageT,
        translation_language: LanguageT,
    ) -> "DictionaryItem":
        return DictionaryItem(
            id=DictionaryItemId(id),
            original=Original(original),
            translation=Translation(translation),
            original_language=Language(original_language),
            translation_language=Language(translation_language),
        )
