from tokenize import Token
from errorHandler import ErrorHandler
from lexer import SPANISH_KEYWORDS
from type import TokenType


class TokenExtractor:
    def __init__(self, lexer):
        self.lexer = lexer

    def get_identifier(self):
        """Obtiene un identificador o una palabra clave."""
        result = ''
        start_column = self.lexer.position_manager.column
        while self.lexer.position_manager.current_char is not None and (self.lexer.position_manager.current_char.isalnum() or self.lexer.position_manager.current_char == '_'):
            result += self.lexer.position_manager.current_char
            self.lexer.position_manager.advance()

        # Verifica si es una palabra clave
        if result in SPANISH_KEYWORDS:
            return Token(TokenType.KEYWORD, result, self.lexer.position_manager.line, start_column)
        return Token(TokenType.IDENTIFIER, result, self.lexer.position_manager.line, start_column)

    def get_number(self):
        """Obtiene un número entero."""
        result = ''
        start_column = self.lexer.position_manager.column
        while self.lexer.position_manager.current_char is not None and self.lexer.position_manager.current_char.isdigit():
            result += self.lexer.position_manager.current_char
            self.lexer.position_manager.advance()
        return Token(TokenType.INTEGER, result, self.lexer.position_manager.line, start_column)

    def get_string(self):
        """Obtiene una cadena de texto, manejando comillas."""
        result = ''
        start_column = self.lexer.position_manager.column
        self.lexer.position_manager.advance()  # Saltar la comilla de apertura
        while self.lexer.position_manager.current_char is not None and self.lexer.position_manager.current_char != '"':
            result += self.lexer.position_manager.current_char
            self.lexer.position_manager.advance()

        if self.lexer.position_manager.current_char == '"':
            self.lexer.position_manager.advance()  # Saltar la comilla de cierre
            return Token(TokenType.STRING, result, self.lexer.position_manager.line, start_column)
        else:
            ErrorHandler.handle_unclosed_string(self.lexer.position_manager.line, self.lexer.position_manager.column)