from sqlalchemy.orm import Session

from app.monitoring.parser_manager import ParserManager

from app.services.document_service import DocumentService
from app.services.source_service import SourceService


class MonitoringService:

    def __init__(self, db: Session):

        self.db = db

        self.source_service = SourceService(db)
        self.document_service = DocumentService(db)

    async def run_parser(
        self,
        parser_name: str,
    ):

        source = self.source_service.get_by_parser(parser_name)

        if source is None:
            raise ValueError(
                f"Source '{parser_name}' not found."
            )

        parser = ParserManager.get(parser_name)

        documents = await parser.run()

        saved = self.document_service.save_documents(
            documents,
            source.id,
        )

        return {
            "source": source.name,
            "saved": saved,
        }

    async def run_all(self):

        result = []

        sources = self.source_service.get_all_sources()

        for source in sources:

            if not source.enabled:
                continue

            result.append(
                await self.run_parser(source.parser_name)
            )

        return result
