from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_url(self, url: str):
        return (
            self.db.query(Document)
            .filter(Document.url == url)
            .first()
        )

    def get_all(self):
        return (
            self.db.query(Document)
            .order_by(
                Document.importance.desc(),
                Document.document_date.desc(),
            )
            .all()
        )

    def get_unprocessed(self, limit: int = 20):
        return (
            self.db.query(Document)
            .filter(Document.processed.is_(False))
            .order_by(Document.id)
            .limit(limit)
            .all()
        )

    def search(self, query: str):

        if not query:
            return self.get_all()

        return (
            self.db.query(Document)
            .filter(
                or_(
                    Document.title.ilike(f"%{query}%"),
                    Document.summary.ilike(f"%{query}%"),
                    Document.content.ilike(f"%{query}%"),
                )
            )
            .order_by(
                Document.importance.desc(),
                Document.document_date.desc(),
            )
            .all()
        )

    def create(self, document: Document):
        self.db.add(document)
        self.db.flush()
        return document

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def refresh(self, document: Document):
        self.db.refresh(document)
