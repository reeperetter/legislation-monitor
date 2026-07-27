from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.document_repository import DocumentRepository

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.get("")
def search_documents(
    q: str = "",
    db: Session = Depends(get_db),
):
    repository = DocumentRepository(db)

    return repository.search(q)
