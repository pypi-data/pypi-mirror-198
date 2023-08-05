from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from jwtserver.core.config import settings

engine = create_engine(settings.postgres.pg_dsn, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
