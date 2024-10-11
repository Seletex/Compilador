import sys
import os
from Parser.programParser import ProgramParser
from lexer import Lexer
from type import TokenType


# Código a analizar
code = """
def suma(a,b):
    return a + b

if suma(3, 5) > 5:
    print("Resultado: ", True)
else:
    print("Resultado: ", False)
"""

# Instancia el lexer y genera los tokens
lexico = Lexer(code)
tokens = lexico.get_tokens()

# Imprime los tokens (opcional, para depuración)
print("Tokens generados por el lexer:")
for token in tokens:
    print(token)

# Instancia el parser con los tokens generados
program_parser = ProgramParser(tokens)

# Intentamos hacer el análisis sintáctico
try:
    program_parser.parse()  # Llama al método parse de ProgramParser
    print("El código es sintácticamente correcto.")
except Exception as e:  # Captura cualquier error lanzado por las clases de parser
    print(f"Ocurrió un error durante el análisis: {e}")
