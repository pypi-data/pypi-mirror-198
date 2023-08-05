import asyncio
import os
from typing import AsyncGenerator, Any

import pytest
import redis
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from redis import Redis

from jwtserver import create_app
from jwtserver.dependencies.init_redis import redis_conn
from jwtserver.dependencies.session_db import async_db_session
from jwtserver.tests.depends import override_async_db_session, override_redis_conn

os.environ["DEBUG"] = "False"


@pytest.fixture(scope="module")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="module", autouse=True)
async def flushall():
    r = redis.from_url("redis://:@localhost:6380/1", decode_responses=True)
    r.flushall()
    r.close()


@pytest.fixture(scope="module")
def app() -> FastAPI:
    # settings = ApplicationSettings()
    # director = Director(DevelopmentApplicationBuilder(settings=settings))
    _app = create_app(lvl_logging="CRITICAL")
    _app.dependency_overrides[async_db_session] = override_async_db_session
    _app.dependency_overrides[redis_conn] = override_redis_conn
    return _app


@pytest.fixture(scope="module")
async def initialized_app(app: FastAPI) -> AsyncGenerator[FastAPI, Any]:
    async with LifespanManager(app):
        yield app


@pytest.fixture(scope="module")
async def client(initialized_app: FastAPI) -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://test",
        headers={"Content-Type": "application/json", "accept": "application/json"},
    ) as client:  # type: AsyncClient
        yield client


@pytest.fixture(scope="module")
def authorized_client(client: AsyncClient) -> AsyncClient:
    return client


@pytest.fixture(scope="module")
def redis_client123():
    pass


@pytest.fixture(scope="module")
async def redis_client() -> Redis.client:
    r = redis.from_url("redis://:@localhost:6380/1", decode_responses=True)
    _client = r.client()
    try:
        return _client
    finally:
        _client.close()
