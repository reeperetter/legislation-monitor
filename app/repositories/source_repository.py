from sqlalchemy.orm import Session

from app.models.source import Source
from app.repositories.base import BaseRepository


class SourceRepository(BaseRepository):

    def __init__(self, db: Session):

        super().__init__(db)

    def get_all(self):

        return (
            self.db.query(Source)
            .order_by(Source.name)
            .all()
        )

    def get(self, source_id: int):

        return (
            self.db.query(Source)
            .filter(Source.id == source_id)
            .first()
        )

    def get_by_name(self, name: str):

        return (
            self.db.query(Source)
            .filter(Source.name == name)
            .first()
        )

    def create(
        self,
        name: str,
        base_url: str,
        enabled: bool = True,
    ):

        source = Source(
            name=name,
            base_url=base_url,
            enabled=enabled,
        )

        return self.add(source)
