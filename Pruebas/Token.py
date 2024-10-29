class Token:
    def __init__(self, token_type, value, position):
        self.token_type = token_type  
        self.value = value              # Valor del token (ej. 'x', 42, 'hello')
        self.position = position        # Posición en el código fuente (ej. número de línea y columna)

    def __repr__(self):
        return f"Token({self.token_type}, {repr(self.value)}, {self.position})"