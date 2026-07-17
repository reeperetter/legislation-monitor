from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(Document)
            .order_by(Document.document_date.desc())
            .all()
        )

    def get_by_url(self, url: str):
        return (
            self.db.query(Document)
            .filter(Document.url == url)
            .first()
        )

    def create(self, document: Document):
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_unprocessed(self, limit: int = 20):
        return (
            self.db.query(Document)
            .filter(Document.processed.is_(False))
            .order_by(Document.id)
            .limit(limit)
            .all()
        )

    def save_content(
        self,
        document: Document,
        content: str,
    ):
        document.content = content
        document.processed = True

        self.db.commit()

    def update_analysis(
        self,
        document: Document,
        analysis: dict,
    ):
        document.document_number = analysis.get("document_number")
        document.document_date = analysis.get("document_date")
        document.document_type = analysis.get("document_type")

        self.db.commit()

    def commit(self):
        self.db.commit()
