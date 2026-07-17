from bs4 import BeautifulSoup


class ContentExtractor:

    def extract(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n")

        lines = [line.strip() for line in text.splitlines()]
        lines = [line for line in lines if line]

        return "\n".join(lines)
