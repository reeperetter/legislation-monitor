from sqlalchemy.orm import Session
from app.repositories.document_repository import DocumentRepository


class DocumentService:

    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)

    def get_all_documents(self):
        return self.repository.get_all()

    def create_document(self, **kwargs):
        exists = self.repository.get_by_url(
            kwargs["url"]
        )

        if exists:
            return exists

        return self.repository.create(**kwargs)
