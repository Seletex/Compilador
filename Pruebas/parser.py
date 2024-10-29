from lexer import Lexer
from Print import Print
from TokenType import TokenType
from Assign import Assign
from binOp import BinOp
from Num import Num


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
        self.functions = []  # Asegúrate de inicializar la lista de funciones

    def error(self):
        raise Exception("Error de análisis")

    def eat(self, token_type):
        """Consume el token actual si es del tipo esperado."""
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            self.error()

    def parse(self):
        try:
            """Método principal para iniciar el análisis."""
            nodes = []
            while self.current_token.token_type != TokenType.EOF:
                if self.current_token.token_type == TokenType.FUNCTION:
                    self.eat(TokenType.FUNCTION)
                    func_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    self.eat(TokenType.LPAREN)
                    self.eat(TokenType.RPAREN)
                    self.eat(TokenType.NEWLINE)
                    self.functions.append(func_name)
                elif self.current_token.token_type == TokenType.KEYWORD and self.current_token.value == 'print':
                    nodes.append(self.print_statement())
                else:
                    self.error()
                
            
            if 'main' not in self.functions:
                raise Exception("Error: La función main es necesaria para ejecutar el programa.")
            print(f"Nodos encontrados: {len(nodes)}")
            print("Devolviendo nodos...")
            return nodes
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return []

    def print_statement(self):
        """Analiza una declaración de impresión."""
        self.eat(TokenType.KEYWORD)  # Se espera 'print'
        self.eat(TokenType.LPAREN)
        expr = self.expr()
        self.eat(TokenType.RPAREN)
        return Print(expr)

    def factor(self):
        """Analiza un factor (número o paréntesis)."""
        token = self.current_token
        if token.token_type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Num(token.value)
        elif token.token_type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        else:
            self.error()

    def term(self):
        """Analiza un término (factor seguido de operadores)."""
        node = self.factor()

        while self.current_token.token_type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.token_type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            elif token.token_type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)
            node = BinOp(left=node, op=token.value, right=self.factor())

        return node

    def expr(self):
        """Analiza una expresión (término seguido de operadores)."""
        node = self.term()
        while self.current_token.token_type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.token_type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.token_type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            node = BinOp(left=node, op=token.value, right=self.term())

        return node

# Ejemplo de uso
source_code = """
print(123 + 456)
"""
lexer = Lexer(source_code)
parser = Parser(lexer)
ast = parser.parse()

# Imprimir el AST
for node in ast:
    print(node)