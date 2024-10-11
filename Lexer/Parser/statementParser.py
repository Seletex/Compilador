from Parser.expresionParser import ExpressionParser
from Parser.functionDefinitionParser import FunctionDefinitionParser
from Parser.ifStatementParser import IfStatementParser
from Parser.lexicalError import LexicalError
from Parser.parserBase import ParserBase
from Parser.returnStatementParser import ReturnStatementParser
from type import TokenType

class StatementParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def statement(self):
        """Analiza una declaración, como una definición de función o una expresión."""
        print(f"Analizando declaración: {self.current_token}")  # Para trazabilidad

        if self.current_token.type == TokenType.KEYWORD:
            if self.current_token.value == "def":
                function_parser = FunctionDefinitionParser(self.tokens, self.pos)
                function_parser.function_definition()
                self.pos = function_parser.pos  # Actualiza la posición
            elif self.current_token.value == "if":
                if_parser = IfStatementParser(self.tokens, self.pos)
                if_parser.if_statement()
                self.pos = if_parser.pos
            elif self.current_token.value == "return":
                return_parser = ReturnStatementParser(self.tokens, self.pos)
                return_parser.return_statement()
                self.pos = return_parser.pos
            else:
                raise LexicalError(
                    f"Palabra clave inesperada '{self.current_token.value}'",
                    self.current_token.line,
                    self.current_token.column
                )
        elif self.current_token.type == TokenType.IDENTIFIER:
            expression_parser = ExpressionParser(self.tokens, self.pos)
            expression_parser.expression()
            self.pos = expression_parser.pos
        elif self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        else:
            raise SyntaxError(
                "declaración válida",
                self.current_token.type,
                self.current_token.line,
                self.current_token.column
            )
