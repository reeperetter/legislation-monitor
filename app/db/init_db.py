from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.seed import seed_sources
from app.services.category_initializer import CategoryInitializer

from app.models.role import Role
from app.models.user import User
from app.models.source import Source
from app.models.keyword import Keyword
from app.models.category import Category
from app.models.document import Document
from app.models.document_category import DocumentCategory


def init_database() -> None:
    """
    Виконує початкове заповнення бази даних.
    Структура БД створюється Alembic.
    """

    db: Session = SessionLocal()

    try:
        seed_sources(db)

        CategoryInitializer(db).initialize()

    finally:
        db.close()
