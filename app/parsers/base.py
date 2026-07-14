from abc import ABC
from abc import abstractmethod
from typing import ClassVar
from app.schemas.document_dto import DocumentDTO
# from bs4 import BeautifulSoup
from app.core.http_client import HttpClient
from app.services.rss_service import RSSService


class BaseParser(ABC):
    registry: ClassVar[dict[str, type["BaseParser"]]] = {}
    parser_name: ClassVar[str | None] = None
    base_url: ClassVar[str] = ""

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.parser_name:
            BaseParser.registry[cls.parser_name] = cls

    def __init__(self):
        self.client = HttpClient()

    async def run(self):
        try:
            return await self.execute()
        finally:
            await self.client.close()


    # def soup(self, html):
    #     return BeautifulSoup(
    #         html,
    #         "lxml",
    #     )

    async def execute(self) -> list[DocumentDTO]:
        """
        Виконує парсер та повертає список документів.
        """
        raise NotImplementedError

    @property
    def rss(self):
        return RSSService()
