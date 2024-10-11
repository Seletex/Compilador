from Parser.parserBase import ParserBase
from type import TokenType

class BlockParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def block(self):
        """Analiza un bloque de código."""
        print(f"Analizando bloque: {self.current_token}")  # Para trazabilidad

        while self.current_token.type == TokenType.NEWLINE:  # Ignorar líneas vacías
            self.advance()

        while self.current_token.type != TokenType.EOF and self.current_token.type != TokenType.NEWLINE:
            # Mueve la importación aquí para evitar el ciclo
            from Parser.statementParser import StatementParser
            statement_parser = StatementParser(self.tokens, self.pos)
            statement_parser.statement()  # Procesa una declaración dentro del bloque
            self.pos = statement_parser.pos
            self.current_token = self.tokens[self.pos]
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
