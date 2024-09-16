from type import TokenType
from token import Token
from type import KEYWORDS, OPERATORS, PARENTHESIS, PUNCTUATION

# Agregar un conjunto de palabras clave en español
spanish_keywords = {'función', 'si', 'entonces', 'mientras', 'para'}

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
        self.advance()  # Saltar la comilla de apertura
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # Saltar la comilla de cierre
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

            if self.current_char in PUNCTUATION:
                token = Token(TokenType.PUNCTUATION, self.current_char)
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
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
            self.pos += 1
        value = self.code[start_pos:self.pos]

        # Verificar si el identificador es una palabra clave en español
        if value in spanish_keywords:
            return Token(TokenType.KEYWORD, value)

        # Verificar si el identificador es una cadena de texto
        if value.startswith('"') and value.endswith('"'):
            return Token(TokenType.STRING, value)

        return Token(TokenType.IDENTIFIER, value)

    def get_tokens(self):
        tokens = []
        token = self.get_next_token()
        while token.type != TokenType.EOF:
            tokens.append(token)
            token = self.get_next_token()
        tokens.append(token)  # Añadir el token EOF
        return tokens