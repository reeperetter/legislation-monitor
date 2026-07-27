from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    model = Category

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(self.model)
            .order_by(self.model.name)
            .all()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(self.model)
            .filter(self.model.name == name)
            .first()
        )

    def create(self, name: str):
        category = self.model(name=name)

        self.db.add(category)
        self.db.flush()

        return category