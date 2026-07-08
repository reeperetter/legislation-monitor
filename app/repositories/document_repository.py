from sqlalchemy.orm import Session

from app.models.document import Document

from app.repositories.base import BaseRepository


class DocumentRepository(BaseRepository):

    def __init__(self, db: Session):

        super().__init__(db)

    def get_all(self):

        return (
            self.db.query(Document)
            .order_by(
                Document.document_date.desc(),
                Document.id.desc(),
            )
            .all()
        )

    def get(self, document_id: int):

        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_by_url(self, url: str):

        return (
            self.db.query(Document)
            .filter(Document.url == url)
            .first()
        )

    def create(self, **kwargs):

        document = Document(**kwargs)

        return self.add(document)
