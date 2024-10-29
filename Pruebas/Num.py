from astNode import ASTNode


class Num(ASTNode):
    """Nodo para números."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)