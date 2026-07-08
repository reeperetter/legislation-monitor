from abc import ABC
from abc import abstractmethod


class BaseParser(ABC):

    registry = {}

    parser_name = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.parser_name:
            BaseParser.registry[cls.parser_name] = cls

    async def run(self):

        raw = await self.fetch()

        return await self.parse(raw)

    @abstractmethod
    async def fetch(self):
        pass

    @abstractmethod
    async def parse(self, data):
        pass
