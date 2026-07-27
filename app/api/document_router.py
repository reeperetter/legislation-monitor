from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.document_repository import DocumentRepository
from app.models.document import Document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.get("")
def get_documents(
    db: Session = Depends(get_db),
):
    repository = DocumentRepository(db)
    return repository.get_all()


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document
