from dishka import Provider, Scope, provide

from app.application.usecases.dictionary import (
    GetItemsByLanguage,
    GetListItems,
    SearchItems,
)


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    get_list_items = provide(GetListItems)
    search_items = provide(SearchItems)
    get_items_by_language = provide(GetItemsByLanguage)
