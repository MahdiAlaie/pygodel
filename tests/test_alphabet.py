import pytest
from pygodel.alphabet import Alphabet, Symbol, SymbolType


def test_standard_symbol_mapping():
    alphabet = Alphabet()
    assert alphabet.get_code("(") == 1
    assert alphabet.get_code("¬") == 9
    assert alphabet.get_code("→") == 15
    assert alphabet.get_symbol(1).name == "("
    assert alphabet.get_symbol(9).symbol_type == SymbolType.CONNECTIVE


def test_duplicate_registration_raises():
    alphabet = Alphabet()
    duplicate_name = Symbol(name="(", code=99, symbol_type=SymbolType.PUNCTUATION)
    with pytest.raises(ValueError):
        alphabet.register_symbol(duplicate_name)

    duplicate_code = Symbol(name="NEW", code=1 , symbol_type=SymbolType.PUNCTUATION)
    with pytest.raises(ValueError):
        alphabet.register_symbol(duplicate_code)


def test_membership_and_missing_keys():
    alphabet = Alphabet()
    assert "(" in alphabet
    assert 9 in alphabet
    assert "?" not in alphabet
    assert 100 not in alphabet


    with pytest.raises(KeyError):
        alphabet.get_code("UNKNOWN")

    with pytest.raises(KeyError):
        alphabet.get_symbol(999)
