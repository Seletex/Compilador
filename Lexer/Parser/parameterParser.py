from Parser.parserBase import ParserBase
from type import TokenType

class ParametersParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def parameters(self):
        """Analiza la lista de parámetros de una función."""
        self.eat(TokenType.IDENTIFIER)  # Esperamos el primer parámetro

        while self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
            self.eat(TokenType.PUNCTUATION, ",")
            self.eat(TokenType.IDENTIFIER)  # Esperamos el siguiente parámetro
