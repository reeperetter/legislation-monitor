from sqlalchemy.orm import Session

from app.repositories.document_repository import (
    DocumentRepository,
)


class DocumentReaderService:

    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(
        self,
        document_id: int,
    ):
        return self.repository.get_by_id(
            document_id,
        )
