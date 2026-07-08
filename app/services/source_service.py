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
    ):

        exists = self.repository.get_by_name(name)

        if exists:

            raise ValueError(
                "Source already exists."
            )

        return self.repository.create(
            name=name,
            base_url=base_url,
        )