from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from app.db.base import Base


class DocumentCategory(Base):
    __tablename__ = "document_categories"

    document_id = Column(Integer, ForeignKey("documents.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
