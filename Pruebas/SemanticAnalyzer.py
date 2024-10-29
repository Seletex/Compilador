import SymbolTable
import String
import Number

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def visit_var_declaration(self, node):
        # Verificar que la variable no esté ya definida
        self.symbol_table.define(node.name, node.var_type)

    def visit_assignment(self, node):
        # Verificar que la variable esté definida
        symbol = self.symbol_table.lookup(node.var.name)
        # Verificar que el tipo de la expresión coincida con el tipo de la variable
        if symbol.symbol_type != self.check_expression_type(node.expr):
            raise Exception(f"Error de tipo: no se puede asignar {node.expr} a {symbol.name}")

    def check_expression_type(self, expr):
        # Lógica para determinar el tipo de la expresión
        if isinstance(expr, Number):
            return 'int'
        elif isinstance(expr, String):
            return 'string'
        # Agregar más tipos según sea necesario