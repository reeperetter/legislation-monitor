from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.config import settings
from app.core.logger import logger
from app.db.init_db import init_database
from app.api.source_router import router as source_router
from app.api.document_router import router as document_router
from app.api.parser_router import router as parser_router
from app.api.monitor_router import router as monitor_router
from app.api.process_router import router as process_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Legislation Monitor...")
    init_database()
    logger.info("Database initialized.")
    yield
    logger.info("Stopping Legislation Monitor...")


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.include_router(source_router)
app.include_router(document_router)
app.include_router(parser_router)
app.include_router(monitor_router)
app.include_router(process_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "request": request,
            "title": settings.APP_NAME,
        },
    )
