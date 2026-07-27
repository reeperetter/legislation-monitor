from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.document_reader_service import (
    DocumentReaderService,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.get("")
def get_documents(
    db: Session = Depends(get_db),
):
    service = DocumentReaderService(db)

    return service.get_all()


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    service = DocumentReaderService(db)

    document = service.get_by_id(
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document
