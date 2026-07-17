from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.document_service import DocumentService

router = APIRouter(prefix="/process", tags=["Processing"])


@router.post("")
async def process_documents(db: Session = Depends(get_db)):
    service = DocumentService(db)
    return await service.process_documents()
