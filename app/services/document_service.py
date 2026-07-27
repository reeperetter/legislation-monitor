from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.category_repository import CategoryRepository
from app.repositories.document_repository import DocumentRepository
from app.schemas.document_dto import DocumentDTO
from app.services.document_processor import DocumentProcessor


class DocumentService:

    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)
        self.category_repository = CategoryRepository(db)
        self.processor = DocumentProcessor()

    def get_all_documents(self):
        return self.repository.get_all()

    def save_documents(
        self,
        documents: list[DocumentDTO],
        source_id: int,
    ):
        added = 0
        skipped = 0

        try:
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

            self.repository.commit()

        except Exception:
            self.repository.rollback()
            raise

        return {
            "added": added,
            "skipped": skipped,
        }

    async def process_documents(
        self,
        limit: int = 20,
    ):
        documents = self.repository.get_unprocessed(limit)
        processed = 0

        try:
            for document in documents:

                try:
                    result = await self.processor.process(
                        url=document.url,
                        title=document.title,
                        summary=document.summary or "",
                    )

                    document.content = result.content
                    document.document_number = result.document_number
                    document.document_date = result.document_date
                    document.document_type = result.document_type
                    document.importance = result.importance
                    document.processed = True

                    for category_name in result.categories:

                        category = self.category_repository.get_by_name(
                            category_name,
                        )

                        if category is None:
                            category = self.category_repository.create(
                                category_name,
                            )

                        if category not in document.categories:
                            document.categories.append(category)

                    processed += 1

                except Exception as e:
                    print(f"Error processing {document.url}: {e}")

            self.repository.commit()

        except Exception:
            self.repository.rollback()
            raise

        finally:
            await self.processor.close()

        return {
            "processed": processed,
            "total": len(documents),
        }
