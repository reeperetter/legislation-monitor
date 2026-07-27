from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.category_reader_service import CategoryReaderService


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("")
def get_categories(
    db: Session = Depends(get_db),
):
    service = CategoryReaderService(db)

    return service.get_all()
