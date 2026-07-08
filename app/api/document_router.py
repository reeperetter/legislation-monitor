from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request

from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.document_service import DocumentService

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/documents")
def documents(
    request: Request,
    db: Session = Depends(get_db),
):

    service = DocumentService(db)

    return templates.TemplateResponse(
        request=request,
        name="documents.html",
        context={
            "request": request,
            "documents": service.get_all_documents(),
            "title": "Documents",
        },
    )
