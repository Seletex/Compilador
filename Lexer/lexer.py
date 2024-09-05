from type import TokenType
from token import Token
from type import KEYWORDS, OPERATORS, PARENTHESIS

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.current_char = code[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.code):
            self.current_char = self.code[self.pos]
        else:
            self.current_char = None  # EOF

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return result

    def get_string(self):
        result = ''
        self.advance()  # Skip the opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # Skip the closing quote
        return result

    def get_next_token(self):
        while self.pos < len(self.code):
            self.current_char = self.code[self.pos]

            if self.current_char.isspace():
                if self.current_char == '\n':
                    self.pos += 1
                    return Token(TokenType.NEWLINE, '\\n')
                self.pos += 1
                continue

            if self.current_char.isdigit():
                return self._integer()

            if self.current_char.isalpha():
                return self._identifier()

            if self.current_char in OPERATORS:
                token = Token(TokenType.OPERATOR, self.current_char)
                self.pos += 1
                return token

            if self.current_char in PARENTHESIS:
                token = Token(TokenType.PARENTHESIS, self.current_char)
                self.pos += 1
                return token

            self.pos += 1

        return Token(TokenType.EOF, None)

    def _integer(self):
        start_pos = self.pos
        while self.pos < len(self.code) and self.code[self.pos].isdigit():
            self.pos += 1
        return Token(TokenType.INTEGER, self.code[start_pos:self.pos])

    def _identifier(self):
        start_pos = self.pos
        while self.pos < len(self.code) and self.code[self.pos].isalnum():
            self.pos += 1
        value = self.code[start_pos:self.pos]
        if value in KEYWORDS:
            return Token(TokenType.KEYWORD, value)
        return Token(TokenType.IDENTIFIER, value)
