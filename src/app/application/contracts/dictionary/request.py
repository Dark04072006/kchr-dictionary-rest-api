from dataclasses import dataclass, field

from app.domain.dictionary.value_objects import LanguageT


@dataclass(frozen=True)
class GetItemsRequest:
    limit: int = field(default=20)
    offset: int = field(default=0)
    language: LanguageT | None = field(default=None)


@dataclass(frozen=True)
class GetTranlationsRequest:
    original: str
    original_language: LanguageT
    translation_language: LanguageT
    limit: int = field(default=20)
    offset: int = field(default=0)
