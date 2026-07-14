from app.parsers import load_parsers
from app.parsers.base import BaseParser


load_parsers()


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
