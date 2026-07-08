from app.parsers.base import BaseParser


class RadaParser(BaseParser):

    parser_name = "rada"

    async def fetch(self):
        return []

    async def parse(self, data):
        return []
