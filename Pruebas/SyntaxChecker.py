from parser import Parser
from Lexer import Lexer

class SyntaxChecker:
    def __init__(self, filename):
        self.filename = filename

    def check_syntax(self):
        with open(self.filename, 'r') as file:
            text = file.read()
        
        lexer = Lexer(text)
        parser = Parser(lexer)

        try:
            parser.parse()
            print("El código es sintácticamente correcto.")
        except Exception as e:
            print(f"Error: {e}")

# Uso de la clase SyntaxChecker
if __name__ == "__main__":
    checker = SyntaxChecker('codigo.txt')
    checker.check_syntax()