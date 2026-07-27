from datetime import date
from sqlalchemy import Boolean, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.source import Source
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.category import Category


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    document_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    document_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    document_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        unique=True,
        nullable=False,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    content: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    importance: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    source_id: Mapped[int] = mapped_column(
        ForeignKey("sources.id"),
        nullable=False,
    )

    source: Mapped["Source"] = relationship(
        "Source",
        back_populates="documents",
    )

    categories: Mapped[list["Category"]] = relationship(
        "Category",
        secondary="document_categories",
        back_populates="documents",
    )

    def __repr__(self):
        return f"<Document {self.title}>"
