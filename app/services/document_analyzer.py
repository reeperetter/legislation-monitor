import re
from datetime import datetime


class DocumentAnalyzer:

    NUMBER_PATTERN = re.compile(r"№\s*([A-Za-zА-Яа-яІЇЄҐ0-9\-\/]+)")

    DATE_PATTERN = re.compile(r"(\d{2}\.\d{2}\.\d{4})")

    TYPE_PATTERNS = {
        "Закон": r"\bЗакон України\b",
        "Постанова": r"\bПостанова\b",
        "Розпорядження": r"\bРозпорядження\b",
        "Наказ": r"\bНаказ\b",
        "Указ": r"\bУказ\b",
    }

    def analyze(self, text: str) -> dict:
        return {
            "document_number": self.find_number(text),
            "document_date": self.find_date(text),
            "document_type": self.find_type(text),
        }

    def find_number(self, text: str):
        match = self.NUMBER_PATTERN.search(text)
        if match:
            return match.group(1)

        return None


    def find_date(self, text: str):
        match = self.DATE_PATTERN.search(text)
        if not match:
            return None
        try:
            return datetime.strptime(match.group(1), "%d.%m.%Y").date()
        except ValueError:
            return None

    def find_type(self, text: str):
        for name, pattern in self.TYPE_PATTERNS.items():
            if re.search(pattern, text, re.IGNORECASE):
                return name

        return None
