from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.category import Category

router = APIRouter(
    prefix="/category",
    tags=["Category"],
)


@router.get("/{name}")
def documents_by_category(
    name: str,
    db: Session = Depends(get_db),
):
    category = (
        db.query(Category)
        .filter(Category.name == name)
        .first()
    )

    if category is None:
        return []

    return category.documents
