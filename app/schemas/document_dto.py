from dataclasses import dataclass
from datetime import date


@dataclass
class DocumentDTO:
    title: str
    url: str
    document_number: str | None = None
    document_date: date | None = None
    summary: str | None = None
    source: str | None = None
