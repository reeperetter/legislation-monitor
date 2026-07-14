from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.schemas.document_dto import DocumentDTO


class DocumentService:

    def __init__(self, db: Session):

        self.repository = DocumentRepository(db)

    def save_documents(
        self,
        documents: list[DocumentDTO],
        source_id: int,
    ):

        added = 0

        skipped = 0

        for dto in documents:

            if self.repository.get_by_url(dto.url):

                skipped += 1

                continue

            document = Document(
                title=dto.title,
                document_number=dto.document_number,
                document_date=dto.document_date,
                url=dto.url,
                summary=dto.summary,
                content=None,
                importance=0,
                processed=False,
                source_id=source_id,
            )

            self.repository.create(document)

            added += 1

        return {
            "added": added,
            "skipped": skipped,
        }
