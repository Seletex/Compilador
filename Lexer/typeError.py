class TypeError(Exception):
    def __init__(self, expected, found, line, column):
        super().__init__(f"Error de tipo: se esperaba {expected}, pero se encontró {found} en línea {line}, columna {column}")
