from fastapi import APIRouter
from fastapi import Depends
from fastapi import Form
from fastapi import Request

from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.source_service import SourceService

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/sources")
def sources(
    request: Request,
    db: Session = Depends(get_db),
):

    service = SourceService(db)

    return templates.TemplateResponse(
        request=request,
        name="sources.html",
        context={
            "request": request,
            "sources": service.get_all_sources(),
            "title": "Sources",
        },
    )


@router.post("/sources")
def create_source(
    name: str = Form(...),
    base_url: str = Form(...),
    db: Session = Depends(get_db),
):

    service = SourceService(db)

    service.create_source(
        name,
        base_url,
    )

    return RedirectResponse(
        "/sources",
        status_code=303,
    )
