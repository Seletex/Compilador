from Parser.argumentListParser import ArgumentListParser
from Parser.parserBase import ParserBase
from type import TokenType


class ExpressionParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def expression(self):
        """Analiza una expresión básica que puede contener paréntesis."""
        print(f"Analizando expresión: {self.current_token}")  # Para trazabilidad

        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.PARENTHESIS and self.current_token.value == '(':
                self.eat(TokenType.PARENTHESIS, '(')  # Consume '('
                argument_list_parser = ArgumentListParser(self.tokens, self.pos)
                argument_list_parser.argument_list()
                self.pos = argument_list_parser.pos  # Actualiza la posición
                self.eat(TokenType.PARENTHESIS, ')')  # Espera el cierre de ')'
            elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ':':
                self.eat(TokenType.PUNCTUATION, ':')  # Consume ':'
            else:
                raise TypeError(
                    "identificador o paréntesis",
                    self.current_token.type,
                    self.current_token.line,
                    self.current_token.column
                )
