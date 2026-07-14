from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.monitoring.parser_manager import ParserManager

from app.services.document_service import DocumentService
from app.services.source_service import SourceService


router = APIRouter()


@router.post("/monitor/{parser_name}")
async def monitor(
    parser_name: str,
    db: Session = Depends(get_db),
):

    parser = ParserManager.get(parser_name)

    documents = await parser.run()

    source = SourceService(db).get_by_parser(parser_name)

    if source is None:
        raise ValueError(f"Source '{parser_name}' not found.")

    result = DocumentService(db).save_documents(
        documents,
        source.id,
    )

    return result
