from app.parsers.base import BaseParser


class DIAMParser(BaseParser):
    parser_name = "diam"

    async def fetch(self):
        return []

    async def parse(self, data):
        return []
