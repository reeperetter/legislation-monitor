from app.config.importance_rules import (KEYWORDS, DOCUMENT_TYPES)


class ImportanceService:

    def calculate(self, title: str, summary: str, document_type: str | None) -> int:
        score = 0
        text = f"{title} {summary}".lower()

        for keyword, value in KEYWORDS.items():
            if keyword in text:
                score += value

        if document_type:
            score += DOCUMENT_TYPES.get(document_type, 0)

        return min(score, 100)
