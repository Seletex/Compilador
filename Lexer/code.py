from lexer import Lexer
from type import TokenType
from parserError import Parser, ParserError 


code = """
def suma(a, b)
    return a + b

if suma(3, 5) > 5:
    print("Resultado: ", True)
else:
    print("Resultado: , False)
"""

# Instancia el lexer y genera los tokens
lexico = Lexer(code)
tokens = lexico.get_tokens()

# Imprime los tokens (opcional, para depuración)
print("Tokens generados por el lexer:")
for token in tokens:
    print(token)

# Instancia el parser con los tokens generados
parser = Parser(tokens)

# Intentamos hacer el análisis sintáctico
try:
    parser.parse()
    print("El código es sintácticamente correcto.")
except ParserError as excepcion:
    print(f"Error sintáctico: {excepcion}")