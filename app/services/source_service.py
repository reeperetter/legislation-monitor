from sqlalchemy.orm import Session
from app.repositories.source_repository import SourceRepository


class SourceService:
    def __init__(self, db: Session):
        self.repository = SourceRepository(db)

    def get_all_sources(self):
        return self.repository.get_all()

    def create_source(
        self,
        name: str,
        base_url: str,
        parser_name: str,
    ):
        exists = self.repository.get_by_name(name)

        if exists:
            raise ValueError(
                "Source already exists."
            )

        return self.repository.create(
            name=name,
            base_url=base_url,
            parser_name=parser_name,
        )

    def get_by_parser(self, parser_name: str):
        return self.repository.get_by_parser(parser_name)

    def update_status(
        self,
        source_id: int,
        status: str,
    ):
        self.repository.update_status(
            source_id,
            status,
        )

    def mark_success(
        self,
        source_id: int,
    ):
        self.repository.mark_success(source_id)
