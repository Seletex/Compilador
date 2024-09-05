
from lexer import Lexer
from type import TokenType


code = """
def suma(a, b):
    return a + b

if suma(3, 5) > 5:
    print("Resultado:", True)
else:
    print("Resultado:", False)
"""

lexico = Lexer(code)

token = lexico.get_next_token()
while token.type != TokenType.EOF:
    print(token)
    token = lexico.get_next_token()
