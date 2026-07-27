from sqlalchemy.orm import Session
from app.models.document import Document
from app.models.category import Category


class DocumentCategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def add_category(self, document: Document, category: Category):
        if category not in document.categories:
            document.categories.append(category)

    def commit(self):
        self.db.commit()