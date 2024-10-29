from lexer import Lexer
from parser import Parser
from translator import Translator

"""def main():
    source_code = """
    # Aquí va el código Python que deseas traducir
"""
    print("Hola, mundo")
    """
"""
    lexer = Lexer(source_code)
    parser = Parser(lexer)
    ast = parser.parse()
    translator = Translator(ast)
    kotlin_code = translator.translate()
    
    print("Código Kotlin generado:")
    print(kotlin_code)
    """
def main():
    try:
        # Leer el archivo de entrada
        with open('input.py', 'r') as file:
            code = file.read()
            print("Código leído del archivo:")
            print(code)
        # Crear el lexer
        lexer = Lexer(code)

        # Crear el parser
        parser = Parser(lexer)
        parser.parse()

        # Crear el traductor
        translator = Translator(parser)
        kotlin_code = translator.translate()

        # Imprimir el código traducido
        print(kotlin_code)

    except FileNotFoundError:
        print("Error: El archivo 'input.py' no se encontró. Asegúrate de que el archivo exista en el directorio correcto.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()