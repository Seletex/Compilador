class WhitespaceSkipper:
    def __init__(self, position_manager):
        self.position_manager = position_manager

    def skip_whitespace(self):
        """Ignora los espacios en blanco."""
        while self.position_manager.current_char is not None and self.position_manager.current_char.isspace():
            self.position_manager.advance()