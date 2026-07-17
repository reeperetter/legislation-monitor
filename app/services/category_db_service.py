from sqlalchemy.orm import Session
from app.repositories.category_repository import (
    CategoryRepository,
)


class CategoryDBService:

    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_or_create(self, name: str):
        category = self.repository.get_by_name(name)

        if category:
            return category

        return self.repository.create(name)