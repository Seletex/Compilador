class ErrorHandler:
    @staticmethod
    def handle_unknown_character(char, line, column):
        raise Exception(f"Error léxico en la línea {line}, columna {column}: "
                        f"Se esperaba un identificador, número, operador o palabra clave, pero se encontró '{char}'")

    @staticmethod
    def handle_unclosed_string(line, column):
        raise Exception(f"Error léxico: cadena sin cerrar en la línea {line}, columna {column}")