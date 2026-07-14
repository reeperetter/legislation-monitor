from fastapi import APIRouter
from fastapi import HTTPException
from app.monitoring.parser_manager import ParserManager

router = APIRouter(prefix="/parser", tags=["Parser"])


@router.get("/available")
async def available_parsers():
    return {
        "parsers": ParserManager.available()
    }


@router.get("/run/{parser_name}")
async def run_parser(parser_name: str):
    try:
        parser = ParserManager.get(parser_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    result = await parser.run()

    return {
        "parser": parser_name,
        "result": result,
    }
