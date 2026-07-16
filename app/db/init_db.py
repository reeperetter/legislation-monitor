from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.seed import seed_sources


def init_database() -> None:
    """
    Виконує початкове заповнення бази даних.
    Структура БД створюється Alembic.
    """

    db: Session = SessionLocal()

    try:
        seed_sources(db)

    finally:
        db.close()