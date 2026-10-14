"""Vectoraized and tensor representations of Godel numbering for Neuro-Symbolic AI."""
import math
from typing import Sequence

from pygodel.alphabet import Alphabet , Symbol
from pygodel.primes import get_nth_prime

class VectorizedGodel:
    """Vectorized and Matrix/Tensor encoder for formal logic sequence."""

    def __init__(self, alphabet: Alphabet | None = None) -> None:
        self.alphabet = alphabet if alphabet is not None else Alphabet()


    def to_token_ids(self, symbols: Sequence[str]) -> list[int]:
        """Convert a sequence of symbol strings into a 1D vector of Godel symbol codes.
        Args:
            symbols: List of formal logic symbols, e.g. ["(", "¬", "P", ")"]
        Returns:
            A list of integers representing the token/symbol IDs.
        """

        if not isinstance(symbols, (list, tuple)):
            raise TypeError("Input symbols must be a list or tuple of strings.")
        if not symbols:
            raise ValueError("Can not encode an empty sequence of symbols.")

        return [self.alphabet.get_code(sym) for sym in symbols]

    def decode_token_ids(self, token_ids: Sequence[int]) -> list[Symbol]:
        """Decode a sequence of Godel symbol codes back into Symbol objects in O(L).
        
        Args:
            token_ids: List of integers representing Godel symbol codes.

        Returns:
            List of decoded Symbol objects.
        """

        if not isinstance(token_ids, (list, tuple)):
            raise TypeError("Token IDs mubst be a list or tuple of integers.")
        if not token_ids:
            raise ValueError("Can not decode an empty sequence of token IDs")

        return [self.alphabet.get_symbol(code) for code in token_ids]

    def to_log_godel(self, symbols: Sequence[str]) -> float:
        """Compute the natural logarithm of the Godel number: ln(G) = sum(c_i * ln(p_i)).
        
        This computes the exact log-magnitude in O(L) without integer overflow.

        Args:
            symbols: Sequence of formal logic symbols.

        Returns:
            The float value of ln(G).
        """

        token_ids = self.to_token_ids(symbols=symbols)
        log_godel_sum = 0.0
        for i, code in enumerate(token_ids):
           prime= get_nth_prime(i)
           log_godel_sum += code * math.log(prime) 
        return log_godel_sum

    def to_one_hot(self, symbols: Sequence[str])-> list[list[int]]:
        """Encode the sequence into a 2D One-Hot matrix (Length x Vocabulary_Size).
        
        Returns:
            A 2D matrix (list of lists) suitable for neural network embeddings.
        """
        token_ids = self.to_token_ids(symbols=symbols)
        all_codes = sorted(self.alphabet._code_to_symbol.keys())
        code_to_col = {code: idx for idx , code in enumerate(all_codes)}
        vocab_size = len(all_codes)

        matrix: list[list[int]] = []
        for code in token_ids:
            row = [0] * vocab_size
            col_idx = code_to_col[code]
            row[col_idx] = 1
            matrix.append(row)

        return matrix