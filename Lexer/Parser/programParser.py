
from Parser.statementParser import StatementParser
from Parser.parserBase import ParserBase
from type import TokenType


class ProgramParser(ParserBase):
    def __init__(self, tokens):
        super().__init__(tokens)

    def parse(self):
        """Método principal para iniciar el análisis sintáctico."""
        self.program()

    def program(self):
        """Analiza un programa que puede contener múltiples declaraciones."""
        while self.current_token.type != TokenType.EOF:
            statement_parser = StatementParser(self.tokens, self.pos)
            statement_parser.statement()
            self.pos = statement_parser.pos
            self.current_token = self.tokens[self.pos]
