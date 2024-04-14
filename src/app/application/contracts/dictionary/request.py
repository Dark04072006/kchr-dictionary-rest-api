from dataclasses import dataclass, field


@dataclass(frozen=True)
class LimitOffsetRequest:
    limit: int = field(default=20)
    offset: int = field(default=0)


@dataclass(frozen=True)
class SearchItemsRequest:
    original: str
    original_language: str
    translation_language: str
    limit: int = field(default=20)
    offset: int = field(default=0)


@dataclass(frozen=True)
class GetItemsByLanguageRequest:
    language: str
    limit: int = field(default=20)
    offset: int = field(default=0)
