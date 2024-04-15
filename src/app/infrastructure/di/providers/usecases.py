from dishka import Provider, Scope, provide

from app.application.usecases.dictionary import GetItems, GetTranslations


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    get_items = provide(GetItems)
    get_translations = provide(GetTranslations)
