from sqlalchemy.orm import Session

from .database import SessionLocal
from .config import settings


def get_db_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def check_token(token: str = "") -> bool:
    """Emulates admin authentication"""
    return token == settings.token
