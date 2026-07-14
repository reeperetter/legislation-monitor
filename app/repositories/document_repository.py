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
            .order_by(Document.document_date.desc())
            .all()
        )

    def create(self, document: Document):

        self.db.add(document)

        self.db.commit()

        self.db.refresh(document)

        return document
