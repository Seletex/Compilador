from Parser.blockParser import BlockParser
from Parser.expresionParser import ExpressionParser
from Parser.parserBase import ParserBase
from type import TokenType


class IfStatementParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def if_statement(self):
        """Analiza una declaración if."""
        print(f"Analizando declaración if: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.KEYWORD, "if")  # Consume 'if'
        expression_parser = ExpressionParser(self.tokens, self.pos)
        expression_parser.expression()  # Analiza la condición del if
        self.pos = expression_parser.pos
        self.eat(TokenType.PUNCTUATION, ':')  # Consume ':'
        block_parser = BlockParser(self.tokens, self.pos)
        block_parser.block()  # Analiza el bloque del if
        self.pos = block_parser.pos
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == "else":
            self.eat(TokenType.KEYWORD, "else")  # Consume 'else'
            self.eat(TokenType.PUNCTUATION, ':')  # Consume ':'
            block_parser.block()  # Analiza el bloque del else
