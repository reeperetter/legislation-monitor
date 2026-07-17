from app.core.http_client import HttpClient
from app.services.content_extractor import ContentExtractor
from app.services.document_analyzer import DocumentAnalyzer


class DocumentProcessor:

    def __init__(self):
        self.client = HttpClient()
        self.extractor = ContentExtractor()
        self.analyzer = DocumentAnalyzer()

    async def load_content(self, url: str) -> str:
        """
        Завантажує HTML та повертає очищений текст.
        """

        html = await self.client.get(url)

        return self.extractor.extract(html)

    async def process(self, url: str) -> dict:
        """
        Повністю обробляє документ:
        - завантажує HTML;
        - витягує текст;
        - аналізує документ.
        """

        content = await self.load_content(url)

        analysis = self.analyzer.analyze(content)

        return {
            "content": content,
            "analysis": analysis,
        }

    async def close(self):
        await self.client.close()
