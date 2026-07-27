from sqlalchemy.orm import Session

from app.repositories.category_repository import CategoryRepository


class CategoryReaderService:

    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all(self):
        return self.repository.get_all()
