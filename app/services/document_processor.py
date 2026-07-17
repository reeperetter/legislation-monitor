from app.core.http_client import HttpClient
from app.services.content_extractor import ContentExtractor
from app.services.document_analyzer import DocumentAnalyzer
from app.services.importance_service import ImportanceService
from app.services.category_service import CategoryService


class DocumentProcessor:

    def __init__(self):
        self.client = HttpClient()
        self.extractor = ContentExtractor()
        self.analyzer = DocumentAnalyzer()
        self.importance = ImportanceService()
        self.categories = CategoryService()

    async def load_content(self, url: str) -> str:
        """
        Завантажує HTML та повертає очищений текст.
        """

        html = await self.client.get(url)

        return self.extractor.extract(html)

    async def process(self, url: str, title: str, summary: str) -> dict:
        """
        Повністю обробляє документ
        """

        content = await self.load_content(url)
        analysis = self.analyzer.analyze(content)
        categories = self.categories.detect(title, summary, content)

        importance = self.importance.calculate(
            title=title,
            summary=summary,
            document_type=analysis.get("document_type"),
        )

        return {
            "content": content,
            "analysis": analysis,
            "categories": categories,
            "importance": importance,
        }

    async def close(self):
        await self.client.close()
