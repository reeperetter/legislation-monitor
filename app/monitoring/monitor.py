from app.monitoring.parser_manager import ParserManager


class Monitor:

    async def run(self):

        result = {}

        for parser_name in ParserManager.available():

            parser = ParserManager.get(parser_name)

            try:

                documents = await parser.run()

                result[parser_name] = len(documents)

            except Exception as e:

                result[parser_name] = str(e)

        return result
