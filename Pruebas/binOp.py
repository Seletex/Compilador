from astNode import ASTNode


class BinOp(ASTNode):
    """Nodo para operaciones binarias."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"