from app.parsers.base import BaseParser
from app.schemas.document_dto import DocumentDTO


class RadaParser(BaseParser):

    parser_name = "rada"

    rss_url = "https://zakon.rada.gov.ua/laws/main/rss"

    async def execute(self) -> list[DocumentDTO]:

        feed = await self.rss.load(self.rss_url)

        documents = []

        for entry in feed.entries:

            title = str(entry.get("title", "")).strip()
            url = str(entry.get("link", "")).strip()
            summary = str(entry.get("summary", "")).strip()

            if not title or not url:
                continue

            documents.append(
                DocumentDTO(
                    title=title,
                    url=url,
                    summary=summary,
                    source="rada",
                )
            )

        return documents
