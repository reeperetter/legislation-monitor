from app.parsers.base import BaseParser

# Імпорт потрібен лише для автоматичної реєстрації
import app.parsers.kmu
import app.parsers.rada
import app.parsers.president
import app.parsers.minregion
import app.parsers.diam


class ParserManager:

    @staticmethod
    def get(name: str):

        parser = BaseParser.registry.get(name)

        if parser is None:
            raise ValueError(f"Parser '{name}' not found.")

        return parser()

    @staticmethod
    def available():

        return sorted(BaseParser.registry.keys())
