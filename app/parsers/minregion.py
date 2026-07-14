from app.parsers.base import BaseParser


class MinRegionParser(BaseParser):
    parser_name = "minregion"

    async def fetch(self):
        return []

    async def parse(self, data):
        return []
