from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.source import Source
from app.models.category import Category


class DashboardService:

    def __init__(self, db: Session):
        self.db = db

    def statistics(self):
        return {
            "documents": self.db.query(Document).count(),
            "processed": (
                self.db.query(Document)
                .filter(Document.processed.is_(True))
                .count()
            ),
            "sources": self.db.query(Source).count(),
            "categories": self.db.query(Category).count(),
        }