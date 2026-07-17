from app.config.categories import CATEGORIES


class CategoryService:

    def detect(self, title: str, summary: str, content: str) -> list[str]:
        text = (f"{title}\n{summary}\n{content}").lower()
        found = []

        for category, keywords in CATEGORIES.items():
            for keyword in keywords:
                if keyword in text:
                    found.append(category)
                    break

        return found
