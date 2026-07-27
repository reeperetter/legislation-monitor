from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.document import Document
from app.models.source import Source

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db),
):
    return {
        "documents": db.query(Document).count(),
        "processed": db.query(Document)
        .filter(Document.processed.is_(True))
        .count(),
        "sources": db.query(Source).count(),
    }
