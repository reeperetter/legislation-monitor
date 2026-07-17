from sqlalchemy.orm import Session
from app.models.category import Category


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_name(self, name: str):
        return (
            self.db.query(Category)
            .filter(Category.name == name)
            .first()
        )

    def create(self, name: str):
        category = Category(name=name)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category