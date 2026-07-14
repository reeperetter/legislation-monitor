from app.parsers.base import BaseParser


class PresidentParser(BaseParser):
    parser_name = "president"

    async def fetch(self):
        return []

    async def parse(self, data):
        return []
