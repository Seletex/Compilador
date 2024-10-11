from errorHandler import ErrorHandler
from positionManager import PositionManager
from tokenExtractor import TokenExtractor
from tokenFetcher import TokenFetcher
from whitheSpaceSkipper import WhitespaceSkipper
from Parser.lexicalError import LexicalError
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
        self.position = 0
        
        self.tokens = []
        self.current_indent_level = 0
        self.position_manager = PositionManager(self)
        self.token_extractor = TokenExtractor(self)
        self.whitespace_skipper = WhitespaceSkipper(self.position_manager)
        self.token_fetcher = TokenFetcher(self)

    def get_next_token(self):
        """Obtiene el siguiente token del código fuente."""
        while self.position_manager.current_char is not None:
            self.whitespace_skipper.skip_whitespace()

            if self.position_manager.current_char is None:
                break

            # Detectar números
            if self.position_manager.current_char.isdigit():
                return self.token_extractor.get_number()

            # Detectar identificadores o palabras clave
            if self.position_manager.current_char.isalpha():
                return self.token_extractor.get_identifier()

            # Detectar operadores
            if self.position_manager.current_char in {'>', '<', '=', '!'}:
                return self.token_extractor.get_operator()

            # Detectar otros operadores simples
            if self.position_manager.current_char in OPERATORS:
                token = Token(TokenType.OPERATOR, self.position_manager.current_char, self.position_manager.line, self.position_manager.column)
                self.position_manager.advance()
                return token

            # Detectar paréntesis
            if self.position_manager.current_char in PARENTHESIS:
                token = Token(TokenType.PARENTHESIS, self.position_manager.current_char, self.position_manager.line, self.position_manager.column)
                self.position_manager.advance()
                return token

            # Detectar puntuación
            if self.position_manager.current_char in PUNCTUATION:
                token = Token(TokenType.PUNCTUATION, self.position_manager.current_char, self.position_manager.line, self.position_manager.column)
                self.position_manager.advance()
                return token

            # Detectar cadenas de texto
            if self.position_manager.current_char == '"':
                return self.token_extractor.get_string()

            # Manejo de caracteres desconocidos
            else:
                ErrorHandler.handle_unknown_character(self.position_manager.current_char, self.position_manager.line, self.position_manager.column)

        return Token(TokenType.EOF, None, self.position_manager.line, self.position_manager.column)
    def get_tokens(self):
        # Lógica para analizar el código y generar tokens
        lines = self.code.split('\n')
        for line in lines:
            stripped_line = line.lstrip()
            indent_level = len(line) - len(stripped_line)

            if indent_level > self.current_indent_level:
                self.tokens.append(Token(TokenType.INDENT, None, self.current_indent_level))
                self.current_indent_level = indent_level
            elif indent_level < self.current_indent_level:
                while self.current_indent_level > indent_level:
                    self.tokens.append(Token(TokenType.DEDENT, None, self.current_indent_level))
                    self.current_indent_level -= 4  # Ajusta según tu lógica de indentación

            # Continuar con la generación de otros tokens
            # Aquí iría tu lógica para otros tokens como IDENTIFIER, KEYWORD, etc.

            # Ejemplo para NEWLINE
            if line.strip() == '':
                self.tokens.append(Token(TokenType.NEWLINE, None, self.current_indent_level))

        self.tokens.append(Token(TokenType.EOF, None, ...))  # Añadir token EOF al final
        return self.tokens

