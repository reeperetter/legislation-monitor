from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.get("")
def search(
    q: str = "",
    db: Session = Depends(get_db),
):
    service = SearchService(db)

    return service.search(q)
