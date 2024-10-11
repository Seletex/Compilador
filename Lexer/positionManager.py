class PositionManager:
    def __init__(self, lexer):
        self.lexer = lexer
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = lexer.code[self.pos] if lexer.code else None

    def advance(self):
        """Avanza al siguiente carácter en el código fuente."""
        if self.current_char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        self.pos += 1
        if self.pos < len(self.lexer.code):
            self.current_char = self.lexer.code[self.pos]
        else:
            self.current_char = None  # EOF