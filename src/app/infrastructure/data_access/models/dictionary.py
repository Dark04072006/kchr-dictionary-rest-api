from sqlalchemy import Column, Integer, Text

from app.domain.dictionary.entities import DictionaryItem
from app.infrastructure.data_access.models.base import Base


class DictionaryItemDb(Base):
    __tablename__ = "dictionary"

    id = Column("id", Integer, primary_key=True)
    original = Column("original", Text(), nullable=False)
    translation = Column("translation", Text(), nullable=False)
    original_language = Column("originalLanguage", Text(), nullable=False)
    translation_language = Column("translationLanguage", Text(), nullable=False)

    def to_entity(self) -> DictionaryItem:
        return DictionaryItem.create(
            id=self.id,
            original=self.original,
            translation=self.translation,
            original_language=self.original_language,
            translation_language=self.translation_language,
        )
