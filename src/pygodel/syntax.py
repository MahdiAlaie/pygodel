"""Syntax validation and structer checking for formal logic expressions."""

from typing import Sequence
from pygodel.alphabet import Alphabet , SymbolType

class FormalValidator:
    """Validates structural and grammatical correctness of formal formulas."""

    def __init__(self, alphabet: Alphabet | None = None) -> None:

        self.alphabet = alphabet or Alphabet()

    def check_balanced_parentheses(self, symbols: Sequence[str]) -> bool:
        """Check wether parentheses in the symbol sequence are strictly balanced.
        
        Arg:
            symbols: A sequence of symbol representetions.
        
        Returns:
            True if parentheses are balanced, False otherwise.
        """

        stack_depth = 0

        for sym in symbols:
            if sym == "(":
                stack_depth += 1
            elif sym == ")":
                stack_depth -= 1
                if stack_depth < 0:
                    return False
        return stack_depth == 0

    def is_valid_token_squence(self, symbols: Sequence[str]) -> bool:
        """Check if all symbols belong to registered alphabet.
        
        Args:
            symbols: sequence of token strings.
        
        Returns:
            True if all tokens are in alphabet, False otherwise.
        """

        if not symbols:
            return False
        return all(sym in self.alphabet for sym in symbols)