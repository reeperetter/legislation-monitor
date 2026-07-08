from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class Source(Base):

    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    base_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    parser_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    priority: Mapped[int] = mapped_column(
        Integer,
        default=100,
        nullable=False,
    )

    check_interval: Mapped[int] = mapped_column(
        Integer,
        default=3600,
        nullable=False,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    last_check: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    last_success: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="idle",
        nullable=False,
    )

    documents = relationship(
        "Document",
        back_populates="source",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Source {self.name}>"
