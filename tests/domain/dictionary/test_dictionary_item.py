import pytest

from app.domain.common.exceptions import DomainValidationError
from app.domain.dictionary.entities import DictionaryItem
from app.domain.dictionary.value_objects import (
    DictionaryItemId,
    Language,
    Original,
    Translation,
)


def test_create_dictionary_item() -> None:
    item = DictionaryItem.create(
        id=1,
        original="Уи махуэ фlыуэ!",
        translation="Здравствуйте!",
        original_language="CS",
        translation_language="RUSS",
    )

    assert item.id == DictionaryItemId(1)
    assert item.original == Original("Уи махуэ фlыуэ!")
    assert item.translation == Translation("Здравствуйте!")
    assert item.original_language == Language("CS")
    assert item.translation_language == Language("RUSS")


def test_same_dictionary_item_languages() -> None:
    with pytest.raises(DomainValidationError):
        DictionaryItem.create(
            id=1,
            original="Уи махуэ фlыуэ!",
            translation="Уи махуэ фlыуэ!",
            original_language="CS",
            translation_language="CS",
        )


def test_invalid_dictionary_item_id() -> None:
    with pytest.raises(DomainValidationError):
        DictionaryItem.create(
            id="not_an_integer",
            original="Уи махуэ фlыуэ!",
            translation="Здравствуйте!",
            original_language="CS",
            translation_language="RUSS",
        )


def test_empty_original() -> None:
    with pytest.raises(DomainValidationError):
        DictionaryItem.create(
            id=1,
            original="",
            translation="Здравствуйте!",
            original_language="CS",
            translation_language="RUSS",
        )


def test_empty_translation() -> None:
    with pytest.raises(DomainValidationError):
        DictionaryItem.create(
            id=1,
            original="Уи махуэ фlыуэ!",
            translation="",
            original_language="CS",
            translation_language="RUSS",
        )


def test_invalid_original_language() -> None:
    with pytest.raises(DomainValidationError):
        DictionaryItem.create(
            id=1,
            original="INVALID",
            translation="Здравствуйте!",
            original_language="INVALID LANGUAGE",
            translation_language="RUSS",
        )


def test_invalid_translation_language() -> None:
    with pytest.raises(DomainValidationError):
        DictionaryItem.create(
            id=1,
            original="Уи махуэ фlыуэ!",
            translation="INVALID",
            original_language="CS",
            translation_language="INVALID LANGUAGE",
        )
