from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.category_repository import CategoryRepository

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("")
def get_categories(
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)

    categories = (
        db.query(repository.model)
        .order_by(repository.model.name)
        .all()
    )

    return categories
