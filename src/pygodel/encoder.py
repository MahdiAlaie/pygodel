"""Godel encoding and decoding engine for formal logical expressions."""

from pygodel.alphabet import Alphabet, Symbol
from pygodel.primes import get_nth_prime , prime_factorization

class GodelEncoder:
    """Encode formar syntax sequences into Godel numbers and decodes them back."""

    def __init__(self, alphabet : Alphabet | None = None) -> None:
        self.alphabet = alphabet if alphabet is not None else Alphabet()

    def encode(self, symbols: list[str]) -> int:
        """Encode a sequence of symbol names into a single Godel number.
        
        Args:
            symbols : List of symbol string, e.g. ["(" , "¬" , ")"]

        Returns:
        The unique Godel number representig the sequence.
        """
        if not symbols:
            raise ValueError("Can not encode an empty sequence of symbols.")
        if not isinstance(symbols, list):
            raise ValueError("Input symbolls must be a list of strings.")

        godel_number = 1
        for index, sym_name in enumerate(symbols , start=0):
            prime = get_nth_prime(index)
            code = self.alphabet.get_code(sym_name)
            godel_number *= prime**code

        return godel_number

    def decode(self , godel_number: int) -> list[Symbol]:
        """Decode a Godel number back into its sequence of formal symbols.
        
        Args:
            Godel_number: An integer greater than 1.

        Returns:
            List of Symbol objects in their original sequential order.
        """
        if godel_number <= 1:
            raise ValueError("Godel number must be an integer greater than 1.")

        factors = dict(prime_factorization(godel_number))

        # Ensure the ptimes from a strictly contiguous initial sequence: p_1, p_2, ... .
        decoded_symbols: list[Symbol] = []
        for index in range(0, len(factors)):
            expected_prime = get_nth_prime(index)
            if expected_prime not in factors:
                raise ValueError(
                    f"Invalid Godel number: Missing contiguous prime factor p_{index} ({expected_prime})."
                )
            code = factors[expected_prime]
            symbol = self.alphabet.get_symbol(code)
            decoded_symbols.append(symbol)

        return decoded_symbols

    def decode_to_string(self, godel_number: int)-> str:
        """Decode a Godel number directly into a string representation."""
        symbols = self.decode(godel_number=godel_number)
        return "".join(sym.name for sym in symbols)
    