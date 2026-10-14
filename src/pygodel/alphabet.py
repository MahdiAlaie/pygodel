"""Formal syntax alphabet and symbol mappings for Godel numbering."""

from dataclasses import dataclass
from enum import Enum

class SymbolType(Enum):
    PUNCTUATION = "punctuation"
    CONNECTIVE = "connective"
    QUANTIFIER = "quantifier"
    RELATION = "relation"
    VARIABLE = "variable"


@dataclass(frozen=True)
class Symbol:
    name : str
    code : int
    symbol_type : SymbolType

    def __str__(self):
        return self.name


class Alphabet:
    """Manage the bi-directional mapping between formal logic symbols and theil Godel codes."""

    def __init__(self):
        self._name_to_symbol : dict[str, Symbol] = {}
        self._code_to_symbol: dict[int, Symbol] = {}
        self._setup_standard_symbols()

    def _setup_standard_symbols(self):
        # Standard logical and syntactic symbols mapped to odd integers
        standard_mapping = [
            ("(", 1, SymbolType.PUNCTUATION),
            (")", 3, SymbolType.PUNCTUATION),
            (",", 5, SymbolType.PUNCTUATION),
            ("=", 7, SymbolType.RELATION),
            ("¬", 9, SymbolType.CONNECTIVE),   #NOT
            ("∧", 11,SymbolType.CONNECTIVE),   #AND
            ("∨", 13,SymbolType.CONNECTIVE),   #OR
            ("→", 15,SymbolType.CONNECTIVE),   #IMPLIES
            ("∀", 17,SymbolType.QUANTIFIER),   #FOR ALL
            ("∃", 19,SymbolType.QUANTIFIER),   #EXISTS
        ]

        for name, code, sym_type in standard_mapping:
            sym = Symbol(name=name, code=code, symbol_type=sym_type)
            self.register_symbol(sym)

    def register_symbol(self, symbol:Symbol):
        """Register a new symbol in the alphabet ensuring unique names and codes."""
        if symbol.name in self._name_to_symbol:
            raise ValueError(f"Symbol name '{symbol.name}' is already registered.")
        if symbol.code in self._code_to_symbol:
            raise ValueError(f"Symbol code {symbol.code} is already registered.")
        self._name_to_symbol[symbol.name] = symbol
        self._code_to_symbol[symbol.code] = symbol

    def register_variable(self, name: str) -> Symbol:
        """Register a new variable with the next avilable odd integer code."""
        if name in self._name_to_symbol:
            return self._name_to_symbol[name]

        max_code = max(self._code_to_symbol.keys()) if self._code_to_symbol else -1
        next_code = max_code + 2 if max_code % 2 ==1 else max_code + 1

        sym = Symbol(name= name, code= next_code, symbol_type= SymbolType.VARIABLE)
        self.register_variable(sym)
        return sym

    def get_code(self,name:str) -> int:
        """Get the numeric Godel code for a given symbol name."""
        if name not in self._name_to_symbol:
            raise KeyError(f"Symbol '{name}; not found in alphabet.")
        return self._name_to_symbol[name].code


    def get_symbol(self, code:int) -> Symbol:
        """Get the symbol object for a given numeric Godel code."""
        if code not in self._code_to_symbol:
            raise KeyError(f"Code {code} not found in alphabet.")
        return self._code_to_symbol[code]

    def __contains__(self, item: str | int) -> bool:
        if isinstance(item, str):
            return item in self._name_to_symbol
        if isinstance(item, int):
            return item in self._code_to_symbol
        return False
