
from tokenize import Token
from type import TokenType


class ParserBase:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        """Avanza al siguiente token."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(TokenType.EOF, None, self.current_token.line, self.current_token.column)

    def eat(self, token_type, expected_value=None):
        """Consume el token actual si es del tipo esperado."""
        if self.current_token.type == token_type and (expected_value is None or self.current_token.value == expected_value):
            print(f"Consumiendo token: {self.current_token}")  # Para trazabilidad
            self.advance()
        else:
            raise SyntaxError(
                expected_value if expected_value else token_type,
                self.current_token.type,
                self.current_token.line,
                self.current_token.column
            )
