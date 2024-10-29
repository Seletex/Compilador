# lexer.py
import re
from TokenType import TokenType
from Token import Token

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_char = self.source_code[self.position] if self.source_code else None
        self.keywords = {'if', 'else', 'for', 'while', 'def', 'class', 'return', 'print'}

    def error(self):
        
        raise Exception(f"Error de análisis: carácter inesperado '{self.current_char}' en la posición {self.position}")

    def advance(self):
        """Avanza a la siguiente posición en el código fuente."""
        self.position += 1
        if self.position < len(self.source_code):
            self.current_char = self.source_code[self.position]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Salta los espacios en blanco."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def identifier(self):
        """Devuelve un identificador o una palabra clave."""
        result = ''
        start_position = self.position
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result in self.keywords:
            return Token(TokenType.KEYWORD, result, start_position)  # Pasar la posición
        else:
            return Token(TokenType.IDENTIFIER, result, start_position)
    def string(self):
        """Devuelve un token de cadena."""
        result = ''
        self.advance()  # Avanzar para pasar la comilla de apertura

        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()

        if self.current_char == '"':
            self.advance()  # Avanzar para pasar la comilla de cierre
            return Token(TokenType.STRING, result, self.position)

    # Si llegamos aquí, significa que no encontramos la comilla de cierre
        self.error()
    def number(self):
        """Devuelve un número entero."""
        result = ''
        start_position = self.position
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result), start_position)

    def next_token(self):
        """Devuelve el siguiente token del código fuente."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+', self.position)

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-', self.position)

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, '*', self.position)

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/', self.position)

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(', self.position)  # Asegúrate de pasar la posición

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')', self.position)  # Asegúrate de pasar la posición
            if self.current_char == ':':  # Agregar esta línea
                self.advance()
                return Token(TokenType.COLON, ':', self.position)
            
            if self.current_char == '>':  # Agregar esta línea para manejar '>'
                self.advance()
                return Token(TokenType.GREATER_THAN, '>', self.position)  # Asegúrate de definir TokenType.GREATER_THAN

            if self.current_char == '<':  # Si también necesitas manejar '<'
                self.advance()
                return Token(TokenType.LESS_THAN, '<', self.position)
            if self.current_char == '\n':
                self.advance()
                return Token(TokenType.NEWLINE, '\n', self.position)  # Asegúrate de pasar la posición
            if self.current_char == ';':
                self.advance()
                return Token(TokenType.SEMICOLON, ';', self.position)
            
            if self.current_char == '"':  # Agregar esta línea para manejar cadenas
                return self.string()
            
            self.error()
              # Asegúrate de pasar la posición
            

        return Token(TokenType.EOF, None, self.position)

# Ejemplo de uso
source_code = """
def my_function():
    print("Hola, mundo")
    if x > 10:
        return x
print(123 + 456)
"""
 # Asegúrate de pasar la posición


lexer = Lexer(source_code)

token = lexer.next_token()
while token.token_type != TokenType.EOF:
    print(token)
    token = lexer.next_token()