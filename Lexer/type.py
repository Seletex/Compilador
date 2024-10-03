import re
from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    INTEGER = auto()
    STRING = auto()
    OPERATOR = auto()
    PARENTHESIS = auto()
    PUNCTUATION = auto()
    KEYWORD = auto()
    NEWLINE = auto()
    EOF = auto()
    COMMENT = auto()
    BOOLEAN = auto()

KEYWORDS = {'def', 'if', 'else', 'return'}
OPERATORS = {'+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>='}
PUNCTUATION = {'(', ')', '[', ']', '{', '}', ',', ';','"',':'}
PARENTHESIS = {'(', ')'}
