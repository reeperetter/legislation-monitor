from app.parsers.base import BaseParser


class KMUParser(BaseParser):
    parser_name = "kmu"

    base_url = "https://www.kmu.gov.ua"

    async def parse(self, html):

        return []
