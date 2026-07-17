from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class ProcessedDocumentDTO:
    content: str
    document_number: str | None
    document_date: date | None
    document_type: str | None
    importance: int
    categories: list[str]
