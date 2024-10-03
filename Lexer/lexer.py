from parserError import ParserError,Parser
from type import TokenType
from token import Token
from type import KEYWORDS, OPERATORS, PARENTHESIS, PUNCTUATION

# Agregar un conjunto de palabras clave en español
SPANISH_KEYWORDS = {'función', 'si', 'entonces', 'mientras', 'para', 'resultado', 'main'}

# Agregar operadores válidos al conjunto de operadores
OPERATORS = {'+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', '='}

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = code[self.pos] if code else None
        self.keywords = KEYWORDS

    def advance(self):
        """Avanza al siguiente carácter en el código fuente."""
        if self.current_char == '\n':
            self.line += 1
            self.column = 1  # Reiniciar la columna al comienzo de una nueva línea
        else:
            self.column += 1

        self.pos += 1
        if self.pos < len(self.code):
            self.current_char = self.code[self.pos]
        else:
            self.current_char = None  # EOF

    def skip_whitespace(self):
        """Ignora los espacios en blanco."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_identifier(self):
        """Obtiene un identificador o una palabra clave."""
        result = ''
        start_column = self.column
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()

        # Verifica si es una palabra clave
        if result in SPANISH_KEYWORDS:
            return Token(TokenType.KEYWORD, result, self.line, start_column)
        return Token(TokenType.IDENTIFIER, result, self.line, start_column)

    def get_number(self):
        """Obtiene un número entero."""
        result = ''
        start_column = self.column
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.INTEGER, result, self.line, start_column)

    def get_string(self):
        """Obtiene una cadena de texto, manejando comillas."""
        result = ''
        start_column = self.column
        self.advance()  # Saltar la comilla de apertura
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()

        if self.current_char == '"':
            self.advance()  # Saltar la comilla de cierre
            return Token(TokenType.STRING, result, self.line, start_column)
        else:
            raise ParserError(f"Error léxico: cadena sin cerrar", self.line, self.column)

    def get_operator(self):
        """Obtiene un operador simple o compuesto como '>', '>=', etc."""
        result = self.current_char
        start_column = self.column
        self.advance()

        # Manejo de operadores compuestos como '>=', '<=', '==', '!='
        if self.current_char == '=' and result in {'>', '<', '=', '!'}:
            result += self.current_char
            self.advance()

        return Token(TokenType.OPERATOR, result, self.line, start_column)

    def get_next_token(self):
        """Obtiene el siguiente token del código fuente."""
        while self.current_char is not None:
            # Ignorar espacios en blanco
            self.skip_whitespace()

            if self.current_char is None:
                break

            # Detectar números
            if self.current_char.isdigit():
                return self.get_number()

            # Detectar identificadores o palabras clave
            if self.current_char.isalpha():
                return self.get_identifier()

            # Detectar operadores
            if self.current_char in {'>', '<', '=', '!'}:
                return self.get_operator()

            # Detectar otros operadores simples
            if self.current_char in OPERATORS:
                token = Token(TokenType.OPERATOR, self.current_char, self.line, self.column)
                self.advance()
                return token

            # Detectar paréntesis
            if self.current_char in PARENTHESIS:
                token = Token(TokenType.PARENTHESIS, self.current_char, self.line, self.column)
                self.advance()
                return token

            # Detectar puntuación
            if self.current_char in PUNCTUATION:
                token = Token(TokenType.PUNCTUATION, self.current_char, self.line, self.column)
                self.advance()
                return token

            # Detectar cadenas de texto
            if self.current_char == '"':
                return self.get_string()

            # Manejo de caracteres desconocidos o no reconocidos
            else:
                char = self.current_char
                self.advance()
                raise ParserError(f"Error léxico en la línea {self.line}, columna {self.column}: "
                          f"Se esperaba un identificador, número, operador o palabra clave, pero se encontró '{char}'",
                          self.line, self.column)

        return Token(TokenType.EOF, None, self.line, self.column)

    def get_tokens(self):
        """Obtiene todos los tokens del código fuente."""
        tokens = []
        while True:
            token = self.get_next_token()
            if token.type == TokenType.EOF:
                break
            tokens.append(token)
        return tokens
