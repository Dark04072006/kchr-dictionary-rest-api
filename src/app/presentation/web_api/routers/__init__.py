from app.presentation.web_api.routers.dictionary import dictionary_router
from app.presentation.web_api.routers.health_check import health_check_router

__all__ = [
    "health_check_router",
    "dictionary_router",
]
