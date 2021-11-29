from contextlib import contextmanager

import faker
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import SQLBase
from app.dependencies import get_db_session
from app.main import app
from app.models import User, Location
from app.config import settings


if settings.test_database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

engine = create_engine(settings.test_database_url, connect_args=connect_args)
SessionLocal = sessionmaker(engine, expire_on_commit=False)

SQLBase.metadata.drop_all(bind=engine)
SQLBase.metadata.create_all(bind=engine)

fake = faker.Faker()


def override_get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db_session] = override_get_db_session


@pytest.fixture
def db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_client() -> TestClient:
    with TestClient(app) as test_app:
        yield test_app


@pytest.fixture(scope="session")
def admin_token() -> str:
    return settings.token


@pytest.fixture
def db_users(db_session):
    users = []
    for _ in range(10):
        user = User(
            full_name=fake.name(),
            location=Location(
                lat=str(fake.latitude()),
                lon=str(fake.longitude()),
            )
        )
        users.append(user)

    db_session.add_all(users)
    db_session.commit()

    for user in users:
        db_session.refresh(user)

    yield users
