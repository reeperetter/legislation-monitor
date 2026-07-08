from sqlalchemy import Boolean
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

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

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # documents = relationship(
    #     "Document",
    #     back_populates="source",
    #     cascade="all, delete-orphan",
    # )

    def __repr__(self):
        return f"<Source {self.name}>"
