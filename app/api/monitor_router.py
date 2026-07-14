from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.monitoring_service import MonitoringService


router = APIRouter()


@router.post("/monitor/{parser_name}")
async def monitor(
    parser_name: str,
    db: Session = Depends(get_db),
):

    service = MonitoringService(db)

    return await service.run_parser(parser_name)


@router.post("/monitor")
async def monitor_all(
    db: Session = Depends(get_db),
):

    service = MonitoringService(db)

    return await service.run_all()
