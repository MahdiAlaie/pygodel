import pytest
from pygodel.encoder import GodelEncoder

def test_encode_simple_expression():
    encoder = GodelEncoder()
     # "(" has code 1, "¬" has code 9
    # p_1 = 2, p_2 = 3
    # G = 2^1 * 3^9 = 2 * 19683 = 39366
    godel_num = encoder.encode(["(","¬"])
    assert godel_num == 39366

def test_roundtrip_encode_decode():
    encoder = GodelEncoder()
    expression = ["(", "¬", "→", ")"]

    godel_num = encoder.encode(expression)
    decoded_symbols = encoder.decode(godel_number=godel_num)
    decoded_string = encoder.decode_to_string(godel_num)

    assert [s.name for s in decoded_symbols] == expression
    assert decoded_string == "(¬→)"

def test_encode_empty_raises():
    encoder = GodelEncoder()
    with pytest.raises(ValueError):
        encoder.encode([])

def test_encode_invalid_number_raises():
    encoder = GodelEncoder()
    with pytest.raises(ValueError):
        encoder.encode(1)
    with pytest.raises(ValueError):
        encoder.decode(0)

def test_decode_non_contiguous_primes_raises():
    encoder = GodelEncoder()
    # 2^1 * 5^1 (missing 3, wich is the 2nd prime)
    invalid_godel = (2**1) * (5**1)
    with pytest.raises(ValueError, match="Missing contiguous prime factor"):
        encoder.decode(invalid_godel)