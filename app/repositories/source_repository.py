from sqlalchemy.orm import Session
from app.models.source import Source
from app.repositories.base import BaseRepository
from datetime import datetime


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

    def get_by_parser(self, parser_name: str):
        return (
            self.db.query(Source)
            .filter(Source.parser_name == parser_name)
            .first()
        )

    def create(
        self,
        name: str,
        base_url: str,
        parser_name: str,
        enabled: bool = True,
        priority: int = 100,
        check_interval: int = 60,
        status: str = "idle",
    ):

        source = Source(
            name=name,
            base_url=base_url,
            parser_name=parser_name,
            enabled=enabled,
            priority=priority,
            check_interval=check_interval,
            status=status,
        )

        return self.add(source)

    def update_status(
        self,
        source_id: int,
        status: str,
    ):
        source = self.get(source_id)

        if source is None:
            return

        source.status = status
        source.last_check = datetime.utcnow()

        self.db.commit()


    def mark_success(
        self,
        source_id: int,
    ):
        source = self.get(source_id)

        if source is None:
            return

        now = datetime.utcnow()

        source.status = "ok"
        source.last_check = now
        source.last_success = now

        self.db.commit()
