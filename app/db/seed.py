from sqlalchemy.orm import Session

from app.models.source import Source


SOURCES = [
    {
        "name": "Верховна Рада України",
        "base_url": "https://zakon.rada.gov.ua",
        "parser_name": "rada",
    },
    {
        "name": "Кабінет Міністрів України",
        "base_url": "https://www.kmu.gov.ua",
        "parser_name": "kmu",
    },
    {
        "name": "Президент України",
        "base_url": "https://www.president.gov.ua",
        "parser_name": "president",
    },
    {
        "name": "Міністерство розвитку громад та територій України",
        "base_url": "https://mtu.gov.ua",
        "parser_name": "minregion",
    },
    {
        "name": "ДІАМ",
        "base_url": "https://diam.gov.ua",
        "parser_name": "diam",
    },
]


def seed_sources(db: Session):

    for data in SOURCES:

        exists = (
            db.query(Source)
            .filter(
                Source.parser_name == data["parser_name"]
            )
            .first()
        )

        if exists:
            continue

        db.add(
            Source(
                **data,
                enabled=True,
                priority=100,
                check_interval=60,
                status="idle",
            )
        )

    db.commit()
