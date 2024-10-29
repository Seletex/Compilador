from binOp import BinOp
import Num
import Print
from lexer import Lexer
from parser import Parser
import Assign

class Translator:
    def __init__(self, ast):
        self.ast = ast
        self.output = []
        self.parser = parser

    def visit(self, node):
        """Visita un nodo del AST y genera el código correspondiente."""
        if isinstance(node, Print):
            self.visit_print(node)
        elif isinstance(node, BinOp):
            self.visit_binop(node)
        elif isinstance(node, Num):
            self.visit_num(node)
        elif isinstance(node, Assign):
            self.visit_assign(node)
        else:
            raise Exception("Nodo desconocido")

    def visit_print(self, node):
        """Genera el código para una declaración de impresión."""
        self.output.append("println(")
        self.visit(node.expr)
        self.output.append(")")

    def visit_binop(self, node):
        """Genera el código para una operación binaria."""
        self.output.append("(")
        self.visit(node.left)
        self.output.append(f" {node.op} ")
        self.visit(node.right)
        self.output.append(")")

    def visit_num(self, node):
        """Genera el código para un número."""
        self.output.append(str(node.value))

    def translate(self):
        """Genera el código Kotlin a partir del AST."""
        for node in self.ast:
            self.visit(node)
            self.output.append("\n")  # Nueva línea después de cada declaración
        return ''.join(self.output)
    def translate(self):
        kotlin_code = ""
        for func in self.parser.functions:
            kotlin_code += f"fun {func}() {{\n"
            kotlin_code += "    // Aquí va el código de la función\n"
            kotlin_code += "}\n"
        return kotlin_code
# Ejemplo de uso
source_code = """
print(123 + 456)
"""
lexer = Lexer(source_code)
parser = Parser(lexer)
ast = parser.parse()

translator = Translator(ast)
kotlin_code = translator.translate()

print("Código Kotlin generado:")
print(kotlin_code)