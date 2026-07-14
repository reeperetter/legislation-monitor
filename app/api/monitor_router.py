from fastapi import APIRouter

from app.monitoring.monitor import Monitor


router = APIRouter(
    prefix="/monitor",
    tags=["Monitor"],
)


@router.get("/run")
async def run_monitor():

    monitor = Monitor()

    return await monitor.run()
