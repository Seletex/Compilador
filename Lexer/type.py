import re
from enum import Enum, auto

class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    OPERATOR = auto()
    INTEGER = auto()
    STRINGS = auto()
    PARENTHESIS = auto()
    WHITESPACE = auto()
    NEWLINE = auto()
    EOF = auto()
    PUNCTUATION = auto()

KEYWORDS = {'def', 'if', 'else', 'return'}
OPERATORS = {'+', '-', '*', '/', '=', '==', '!='}
PARENTHESIS = {'(', ')'}
PUNCTUATION = {',', '"', ':'}
