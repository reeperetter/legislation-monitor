from abc import ABC
from abc import abstractmethod

from bs4 import BeautifulSoup

from app.core.http_client import HttpClient


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

        html = await self.fetch()

        documents = await self.parse(html)

        await self.client.close()

        return documents

    async def fetch(self):

        return await self.client.get(self.base_url)

    def soup(self, html):

        return BeautifulSoup(
            html,
            "lxml",
        )

    @abstractmethod
    async def parse(self, html) -> list:
        pass
