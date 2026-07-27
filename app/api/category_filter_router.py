from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.category_filter_service import (
    CategoryFilterService,
)

router = APIRouter(
    prefix="/category",
    tags=["Category"],
)


@router.get("/{name}")
def documents(
    name: str,
    db: Session = Depends(get_db),
):
    service = CategoryFilterService(db)

    return service.get_documents(name)
