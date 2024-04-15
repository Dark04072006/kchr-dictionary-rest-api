from dataclasses import dataclass

from app.domain.common.entities import Entity
from app.domain.common.exceptions import DomainValidationError
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

    def __post_init__(self) -> None:
        if self.original_language == self.translation_language:
            raise DomainValidationError(
                "Original and translation languages cannot be the same"
            )

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
