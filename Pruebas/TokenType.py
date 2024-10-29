from enum import Enum

class TokenType(Enum):
    # Tipos de tokens para palabras clave
    FUNCTION = 'FUNCTION'
    PRINT = "PRINT"
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FOR = "FOR"
    DEF = "DEF"  # Agregar este tipo
    CLASS = "CLASS"  # Agregar este tipo
    RETURN = "RETURN"  # Agregar este tipo

    # Tipos de tokens para operadores
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    GREATER_THAN = 'GREATER_THAN'
    LESS_THAN = 'LESS_THAN'

    # Tipos de tokens para literales
    NUMBER = "NUMBER"
    STRING = 'STRING'

    # Tipos de tokens para identificadores
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"  # Agregar este tipo

    # Otros tipos de tokens
    LPAREN = "LPAREN"  # (
    RPAREN = "RPAREN"  # )
    LBRACE = "LBRACE"  # {
    RBRACE = "RBRACE"  # }
    SEMICOLON = "SEMICOLON"  # ;
    EOF = "EOF"  # Fin de archivo
    COLON = ':'
    NEWLINE = '\n'
    INDENT = 'INDENT'
    DEDENT = 'DEDENT'
    