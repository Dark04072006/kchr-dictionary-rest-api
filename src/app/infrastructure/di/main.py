from dishka import AsyncContainer, make_async_container

from app.infrastructure.di.providers.adapters import SqlalchemyProvider
from app.infrastructure.di.providers.usecases import UseCasesProvider


def container_factory() -> AsyncContainer:
    return make_async_container(SqlalchemyProvider(), UseCasesProvider())
