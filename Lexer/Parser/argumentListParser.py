from Parser.parserBase import ParserBase
from type import TokenType

class ArgumentListParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def argument_list(self):
        """Analiza los argumentos de una función."""
        if self.current_token.type != TokenType.PARENTHESIS:
            while self.current_token.type in (TokenType.IDENTIFIER, TokenType.INTEGER, TokenType.STRING):
                
                # Mueve la importación aquí
                from Parser.expresionParser import ExpressionParser
                expression_parser = ExpressionParser(self.tokens, self.pos)
                
                expression_parser.expression()  # Analiza cada argumento
                self.pos = expression_parser.pos
                if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
                    self.eat(TokenType.PUNCTUATION, ',')  # Consume ',' entre argumentos
                else:
                    break
