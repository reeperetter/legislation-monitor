from app.core.http_client import HttpClient
from app.services.content_extractor import ContentExtractor


class DocumentProcessor:
    def __init__(self):
        self.client = HttpClient()
        self.extractor = ContentExtractor()

    async def load_content(self, url: str) -> str:
        html = await self.client.get(url)
        return self.extractor.extract(html)

    async def close(self):
        await self.client.close()
