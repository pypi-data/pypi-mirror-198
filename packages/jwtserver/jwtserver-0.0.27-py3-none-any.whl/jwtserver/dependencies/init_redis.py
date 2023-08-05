import redis

from jwtserver import settings

settings = settings.get_settings()


def create_pool_redis():
    pool = redis.ConnectionPool.from_url(
        settings.redis.redis_dsn,
        max_connections=settings.redis.max_connections,
        decode_responses=True,
    )
    return redis.Redis(connection_pool=pool)


def redis_conn():
    r = create_pool_redis().client()
    try:
        yield r
    finally:
        r.close()
