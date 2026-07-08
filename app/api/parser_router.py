from fastapi import APIRouter

from app.parsers.kmu_parser import KMUParser

router = APIRouter()


@router.get("/parser/test")
async def parser_test():

    parser = KMUParser()

    soup = await parser.parse()

    return {
        "title": soup.title.text,
    }
