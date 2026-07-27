from sqlalchemy.orm import Session

from app.config.categories import CATEGORIES
from app.repositories.category_repository import CategoryRepository


class CategoryInitializer:

    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def initialize(self):

        for category_name in CATEGORIES:

            category = self.repository.get_by_name(
                category_name,
            )

            if category is None:
                self.repository.create(
                    category_name,
                )

        self.repository.db.commit()
