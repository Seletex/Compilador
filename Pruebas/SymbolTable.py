import Symbol

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, symbol_type):
        if name in self.symbols:
            raise Exception(f"Error: '{name}' ya está definido.")
        self.symbols[name] = Symbol(name, symbol_type)

    def lookup(self, name):
        if name not in self.symbols:
            raise Exception(f"Error: '{name}' no está definido.")
        return self.symbols[name]