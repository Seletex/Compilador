class LexicalError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"Error léxico: {message} en línea {line}, columna {column}")
