from typing import Any
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session):
        self.db = db
    def add(self, obj: Any):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: Any):
        self.db.delete(obj)
        self.db.commit()

    def save(self):
        self.db.commit()

    def refresh(self, obj: Any):
        self.db.refresh(obj)