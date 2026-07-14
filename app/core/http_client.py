import httpx


class HttpClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=30,
            follow_redirects=True,
            headers={
                "User-Agent":
                "LegislationMonitor/1.0"
            }
        )

    async def get(self, url: str) -> str:
        response = await self.client.get(url)
        response.raise_for_status()

        return response.text

    async def close(self):
        await self.client.aclose()
