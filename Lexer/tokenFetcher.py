class TokenFetcher:
    def __init__(self, lexer):
        self.lexer = lexer

    def fetch(self):
        """Obtiene el siguiente token del código fuente."""
        return self.lexer.get_next_token()