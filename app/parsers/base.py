from abc import ABC
from abc import abstractmethod
# from bs4 import BeautifulSoup
from app.core.http_client import HttpClient
from app.services.rss_service import RSSService


class BaseParser(ABC):
    registry = {}
    parser_name = None
    base_url = ""

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

    @abstractmethod
    async def execute(self):
        pass

    @property
    def rss(self):
        return RSSService()
