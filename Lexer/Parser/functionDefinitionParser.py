from Parser.blockParser import BlockParser
from Parser.parameterParser import ParametersParser
from Parser.parserBase import ParserBase
from type import TokenType

class FunctionDefinitionParser(ParserBase):
    def __init__(self, tokens, pos):
        super().__init__(tokens)
        self.pos = pos
        self.current_token = self.tokens[self.pos]

    def function_definition(self):
        """Analiza la definición de una función."""
        self.eat(TokenType.KEYWORD, "def")  # Asegúrate de consumir la palabra clave "def"
        self.eat(TokenType.IDENTIFIER)  # Esperamos un identificador para la función
        self.eat(TokenType.PARENTHESIS, "(")  # Esperamos un paréntesis de apertura

        # Analizar los parámetros de la función (si los hay)
        if self.current_token.type != TokenType.PARENTHESIS:
            parameters_parser = ParametersParser(self.tokens, self.pos)
            parameters_parser.parameters()
            self.pos = parameters_parser.pos  # Actualiza la posición

        self.eat(TokenType.PARENTHESIS, ")")  # Esperamos un paréntesis de cierre
        self.eat(TokenType.NEWLINE)  # Consumimos el salto de línea

        # Analizar el cuerpo de la función
        self.eat(TokenType.INDENT)  # Consumimos la indentación
        block_parser = BlockParser(self.tokens, self.pos)
        block_parser.block()  # Llama al bloque para analizar el cuerpo
        self.pos = block_parser.pos  # Actualiza la posición
        self.eat(TokenType.DEDENT)  # Consumimos la desindentación
