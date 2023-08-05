import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from jwtserver import models

engine = create_engine(
    "postgresql+psycopg2://jwtserver:jwtserver-password@localhost:5433/jwtserver-tests"
)
# async_engine = create_async_engine(
#     "postgresql+asyncpg://jwtserver:jwtserver-password@localhost:5433/jwtserver-tests"
# )
# TestingSessionLocal = sessionmaker(
#     async_engine, expire_on_commit=False, class_=AsyncSession
# )
TestingSessionLocal = sessionmaker(engine)


def create_pool_redis():
    _pool = redis.ConnectionPool.from_url(
        "redis://:@localhost:6380/1",
        max_connections=10,
        decode_responses=True,
    )
    return redis.Redis(connection_pool=_pool)


models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
# models.Base.metadata.drop_all(bind=sync_engine)
# models.Base.metadata.create_all(bind=sync_engine)


def override_async_db_session():
    """Databases pool fabric connection, auto close connection"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_redis_conn():
    try:
        r = create_pool_redis().client()
        yield r
    finally:
        r.close()
