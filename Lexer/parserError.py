from type import TokenType
from token import Token

class ParserError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} en línea {line}, columna {column}")

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
            self.current_token = Token(TokenType.EOF, None, self.current_token.line, self.current_token.column)

    def eat(self, token_type):
        """Consume el token actual si es del tipo esperado"""
        if self.current_token.type == token_type:
            print(f"Consumiendo token: {self.current_token}")  # Para trazabilidad
            self.advance()
        else:
            raise ParserError(
                f"Error sintáctico: se esperaba {token_type}, pero se encontró {self.current_token.type}",
                self.current_token.line,
                self.current_token.column
            )

    def parse(self):
        """Método principal para iniciar el análisis sintáctico"""
        self.program()

    def program(self):
        """Analiza un programa, que puede contener múltiples declaraciones"""
        while self.current_token.type != TokenType.EOF:
            self.statement()

    def statement(self):
        """Analiza una declaración, como una definición de función o una expresión"""
        print(f"Analizando declaración: {self.current_token}")  # Para trazabilidad

        if self.current_token.type == TokenType.KEYWORD:
            if self.current_token.value == "def":
                self.function_definition()
            elif self.current_token.value == "if":
                self.if_statement()
            elif self.current_token.value == "return":
                self.return_statement()
            else:
                raise ParserError(
                    f"Error sintáctico: palabra clave inesperada {self.current_token.value}",
                    self.current_token.line,
                    self.current_token.column
                )
        elif self.current_token.type == TokenType.IDENTIFIER:
            self.expression()
        elif self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        else:
            raise ParserError(
                f"Error sintáctico: declaración inesperada {self.current_token.type}",
                self.current_token.line,
                self.current_token.column
            )

    def expression(self):
        """Analiza una expresión básica que puede contener paréntesis"""
        print(f"Analizando expresión: {self.current_token}")  # Para trazabilidad

        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.PARENTHESIS and self.current_token.value == '(':
                self.eat(TokenType.PARENTHESIS)  # Consume '('
                self.argument_list()
                self.eat(TokenType.PARENTHESIS)  # Consume ')'
        elif self.current_token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
        else:
            raise ParserError(
                f"Error sintáctico: se esperaba un identificador o cadena, pero se encontró {self.current_token.type}",
                self.current_token.line,
                self.current_token.column
            )

    def function_definition(self):
        """Analiza una definición de función"""
        print(f"Analizando definición de función: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.KEYWORD)  # consume 'def'
        self.eat(TokenType.IDENTIFIER)  # consume el nombre de la función
        self.eat(TokenType.PARENTHESIS)  # consume '('
        self.parameter_list()
        self.eat(TokenType.PARENTHESIS)  # consume ')'
        print(f"Esperando ':' después de la definición de la función: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.PUNCTUATION)  # consume ':'
        self.block()

    def parameter_list(self):
        """Analiza la lista de parámetros de una función"""
        while self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
                self.eat(TokenType.PUNCTUATION)  # consume ','
            else:
                break

    def argument_list(self):
        """Analiza los argumentos de una función"""
        while self.current_token.type in (TokenType.IDENTIFIER, TokenType.INTEGER, TokenType.STRING):
            self.expression()  # Analiza cada argumento
            if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
                self.eat(TokenType.PUNCTUATION)  # Consume la coma entre argumentos
            else:
                break

    def if_statement(self):
        """Analiza una declaración if"""
        print(f"Analizando declaración if: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.KEYWORD)  # consume 'if'
        self.expression()  # analiza la condición del if
        print(f"Esperando ':' después de la condición del if: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.PUNCTUATION)  # consume ':'
        self.block()  # analiza el bloque del if
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == "else":
            self.eat(TokenType.KEYWORD)  # consume 'else'
            print(f"Esperando ':' después del else: {self.current_token}")  # Para trazabilidad
            self.eat(TokenType.PUNCTUATION)  # consume ':'
            self.block()  # analiza el bloque del else

    def return_statement(self):
        """Analiza una declaración return"""
        print(f"Analizando declaración return: {self.current_token}")  # Para trazabilidad
        self.eat(TokenType.KEYWORD)  # consume 'return'
        self.expression()  # analiza el valor de retorno
        self.eat(TokenType.NEWLINE)  # consume el salto de línea después del return

    def block(self):
        """Analiza un bloque de código"""
        print(f"Analizando bloque: {self.current_token}")  # Para trazabilidad

        while self.current_token.type == TokenType.NEWLINE:  # Ignorar líneas vacías
            self.advance()

        while self.current_token.type != TokenType.EOF and self.current_token.type != TokenType.NEWLINE:
            self.statement()  # Procesa una declaración dentro del bloque
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
