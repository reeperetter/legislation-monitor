import feedparser


class RSSService:
    async def load(self, url: str):
        return feedparser.parse(url)
