from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class DatabaseConfig:
    db_uri: str

    @staticmethod
    def from_env() -> "DatabaseConfig":
        uri = getenv(
            "DATABASE_URI",
            "sqlite+aiosqlite:///assets/dictionary.db",
        )

        return DatabaseConfig(uri)
