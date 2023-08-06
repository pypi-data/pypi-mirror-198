from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from jwtserver.core.config import settings

engine = create_engine(settings.postgres.dsn, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
