from Parser.expresionParser import ExpressionParser
from Parser.parserBase import ParserBase
from type import TokenType
class ReturnStatementParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def return_statement(self):
        """Analiza una declaración return."""
        print(f"Analizando declaración return: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.KEYWORD, "return")  # Consume 'return'
        expression_parser = ExpressionParser(self.tokens, self.pos)
        expression_parser.expression()  # Analiza el valor de retorno
        self.pos = expression_parser.pos
        if self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)  # Consume el salto de línea después del return
