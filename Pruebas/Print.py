from astNode import ASTNode


class Print(ASTNode):
    """Nodo para la declaración de impresión."""
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Print({self.expr})"
    