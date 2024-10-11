class SyntaxError(Exception):
    def __init__(self, expected, found, line, column):
        super().__init__(f"Error sintáctico: se esperaba {expected}, pero se encontró {found} en línea {line}, columna {column}")
