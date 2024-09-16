from type import TokenType
from token import Token

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        """Avanza al siguiente token"""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(TokenType.EOF, None)

    def eat(self, token_type):
        """Consume el token actual si es del tipo esperado"""
        if self.current_token.type == token_type:
            self.advance()
        else:
            raise ParserError(f"Error sintáctico: se esperaba {token_type}, pero se encontró {self.current_token.type}")

    def parse(self):
        """Método principal para iniciar el análisis sintáctico"""
        self.program()

    def program(self):
        """Analiza un programa, que puede contener múltiples declaraciones"""
        while self.current_token.type != TokenType.EOF:
            self.statement()

    def statement(self):
        """Analiza una declaración, como una definición de función o una expresión"""
        if self.current_token.type == TokenType.KEYWORD:
            if self.current_token.value == "def":
                self.function_definition()
            elif self.current_token.value == "if":
                self.if_statement()
            elif self.current_token.value == "return":
                self.return_statement()
            else:
                raise ParserError(f"Error sintáctico: palabra clave inesperada {self.current_token.value}")
        elif self.current_token.type == TokenType.IDENTIFIER:
            self.expression()
        elif self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        else:
            raise ParserError(f"Error sintáctico: declaración inesperada {self.current_token.type}")

    def expression(self):
        """Analiza una expresión que puede contener paréntesis y puntuación"""
        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.PARENTHESIS and self.current_token.value == '(':
                self.eat(TokenType.PARENTHESIS)  # Consume '('
                self.parameter_list()
                self.eat(TokenType.PARENTHESIS)  # Consume ')'
            elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value in {',', ';', ':'}:
                # Opcional: Maneja puntuación dentro de expresiones si es necesario
                self.eat(TokenType.PUNCTUATION)
        else:
            raise ParserError(f"Error sintáctico: se esperaba un identificador, pero se encontró {self.current_token.type}")

    def function_definition(self):
        """Analiza una definición de función"""
        self.eat(TokenType.KEYWORD)  # consume 'def'
        self.eat(TokenType.IDENTIFIER)  # consume el nombre de la función
        self.eat(TokenType.PARENTHESIS)  # consume '('
        self.parameter_list()
        self.eat(TokenType.PARENTHESIS)  # consume ')'
        self.eat(TokenType.COLON)  # consume ':'
        self.block()

    def parameter_list(self):
        """Analiza la lista de parámetros de una función"""
        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            while self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
                self.eat(TokenType.PUNCTUATION)  # consume ','
                if self.current_token.type == TokenType.IDENTIFIER:
                    self.eat(TokenType.IDENTIFIER)
                else:
                    raise ParserError(f"Error sintáctico: se esperaba un identificador, pero se encontró {self.current_token.type}")

    def if_statement(self):
        """Analiza una declaración if"""
        self.eat(TokenType.KEYWORD)  # consume 'if'
        self.expression()  # analiza la condición del if
        self.block()  # analiza el bloque del if
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == "else":
            self.eat(TokenType.KEYWORD)  # consume 'else'
            self.block()  # analiza el bloque del else

    def return_statement(self):
        """Analiza una declaración return"""
        self.eat(TokenType.KEYWORD)  # consume 'return'
        self.expression()  # analiza el valor de retorno
        self.eat(TokenType.NEWLINE)  # consume el salto de línea después del return

    def block(self):
        """Analiza un bloque de código que puede contener múltiples declaraciones"""
        while self.current_token.type == TokenType.NEWLINE:  # Ignorar líneas vacías
            self.advance()

        while self.current_token.type != TokenType.EOF and self.current_token.type != TokenType.NEWLINE:
            self.statement()  # Procesa una declaración dentro del bloque
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
