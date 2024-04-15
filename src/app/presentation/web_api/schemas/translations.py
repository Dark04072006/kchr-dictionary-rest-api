from typing import Annotated

from fastapi import Query

from app.domain.dictionary.value_objects import LanguageT
from app.presentation.web_api.schemas.limit_offset import LimitOffsetSchema


class GetTranslationsSchema(LimitOffsetSchema):
    original: Annotated[str, Query()]
    original_language: Annotated[LanguageT, Query()]
    translation_language: Annotated[LanguageT, Query()]
