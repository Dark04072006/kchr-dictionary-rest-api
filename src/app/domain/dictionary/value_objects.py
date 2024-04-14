from dataclasses import dataclass
from typing import Literal

from app.domain.common.exceptions import DomainValidationError
from app.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class DictionaryItemId(ValueObject[int]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise DomainValidationError(
                f"Item id must be an integer, not {type(self.to_raw())}"
            )
        if self.to_raw() < 0:
            raise DomainValidationError(
                f"Item id must be positive, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Original(ValueObject[str]):
    def validate(self) -> None:
        if not self.to_raw():
            raise DomainValidationError("Item original field cannot be empty")
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Item original field must be a string, not {type(self.to_raw())}"
            )


@dataclass(frozen=True)
class Translation(ValueObject[str]):
    def validate(self) -> None:
        if not self.to_raw():
            raise DomainValidationError("Item translation field cannot be empty")
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Item translation field must be a string, not {type(self.to_raw())}"
            )


LanguageT = Literal["KAR", "CS", "RUSS"]


@dataclass(frozen=True)
class Language(ValueObject[LanguageT]):
    def validate(self) -> None:
        if not self.to_raw():
            raise DomainValidationError("Item language field cannot be empty")

        if self.to_raw() not in ["KAR", "CS", "RUSS"]:
            raise DomainValidationError(
                f'Item language field must be "KAR" or "CS" or "RUSS", not {self.to_raw()}'
            )
