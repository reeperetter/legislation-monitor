from app.db.base import Base
from app.db.session import engine
from app.models.document import Document

# Імпорт моделей ОБОВ'ЯЗКОВИЙ,
# щоб SQLAlchemy "побачила" таблиці.

from app.models.user import User
from app.models.role import Role

from app.models.source import Source
from app.models.keyword import Keyword
from app.models.category import Category


def init_database() -> None:
    """
    База даних тепер керується Alembic.

    Тут поки нічого не потрібно.
    """
    return
