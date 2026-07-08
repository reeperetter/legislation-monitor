from app.parsers.base import BaseParser


class KMUParser(BaseParser):

    parser_name = "kmu"

    async def fetch(self):
        return []

    async def parse(self, data):
        return []
