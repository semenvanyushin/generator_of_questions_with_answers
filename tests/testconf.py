from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from scr.db.base import Base
from scr.app.app import app, get_db

SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/postgres_test"
)

engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_test
)


Base.metadata.create_all(bind=engine_test)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
