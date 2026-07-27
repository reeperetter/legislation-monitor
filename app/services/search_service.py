from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository


class SearchService:

    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)

    def search(self, query: str):
        return self.repository.search(query)
