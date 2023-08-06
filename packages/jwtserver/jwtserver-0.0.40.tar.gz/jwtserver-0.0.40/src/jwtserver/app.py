from fastapi import FastAPI, Depends
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

from jwtserver.api.api_v1.api import api_router
from jwtserver.api.deps import recaptcha_google_v3_action
from jwtserver.core.config import settings

__all__ = ["app", "create_app"]

from jwtserver.middlewares.stock import middleware_stock

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:5000",
    "http://localhost:3000",
]
description = """[Full JWT Server docs](https://jwtserver.markgoltsev.net)"""
tags_metadata = [
    {
        "name": "login",
        "externalDocs": {
            "description": "Login external docs",
            "url": "https://jwtserver.markgoltsev.net/en/api_v1/login",
        },
    },
    {
        "name": "users",
        "externalDocs": {
            "description": "users external docs",
            "url": "https://jwtserver.markgoltsev.net/en/api_v1/users",
        },
    },
    {
        "name": "utils",
        "externalDocs": {
            "description": "utils external docs",
            "url": "https://jwtserver.markgoltsev.net/en/api_v1/users",
        },
    },
    {
        "name": "items",
        "externalDocs": {
            "description": "items external docs",
            "url": "https://jwtserver.markgoltsev.net/en/api_v1/users",
        },
    },
]


def create_app(_title=settings.project_name, lvl_logging="INFO") -> FastAPI:
    dependencies = []

    if settings.recaptcha:
        dependencies.append(Depends(recaptcha_google_v3_action))

    _app = FastAPI(
        title=_title,
        description=description,
        version="0.0.40",
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        openapi_tags=tags_metadata,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if settings.recaptcha:
        _app.add_middleware(BaseHTTPMiddleware, dispatch=middleware_stock)

    _app.include_router(
        api_router,
        prefix=settings.API_V1_STR,
        dependencies=dependencies,
    )

    # _app.dependency_overrides = {
    #     get_settings: lambda: _config,
    # }
    _app.debug = True

    # def enable_logger(sink=sys.stderr, level="DEBUG"):
    #     logging.basicConfig(level=logging.DEBUG)
    #     logger.configure(handlers=[{"sink": sink, "level": level}])
    #     logger.enable("aria2p")
    #
    # enable_logger(level=lvl_logging)
    return _app


app = create_app()
