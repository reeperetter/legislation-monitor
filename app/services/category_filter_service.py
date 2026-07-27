from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryFilterService:

    def __init__(self, db: Session):
        self.db = db

    def get_documents(self, category_name: str):

        category = (
            self.db.query(Category)
            .filter(Category.name == category_name)
            .first()
        )

        if category is None:
            return []

        return category.documents
