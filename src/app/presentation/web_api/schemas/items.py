from typing import Annotated

from fastapi import Query

from app.domain.dictionary.value_objects import LanguageT
from app.presentation.web_api.schemas.limit_offset import LimitOffsetSchema


class GetItemsSchema(LimitOffsetSchema):
    language: Annotated[LanguageT | None, Query(default=None)]
