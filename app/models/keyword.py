from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.db.base import Base


class Keyword(Base):
    __tablename__ = "keywords"

    id: Mapped[int] = mapped_column(primary_key=True)

    word: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    weight: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    def __repr__(self):
        return f"<Keyword {self.word}>"
