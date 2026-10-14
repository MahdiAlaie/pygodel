import math
import pytest
from pygodel.tensor import VectorizedGodel
from pygodel.primes import get_nth_prime


def test_to_token_ids_and_decode():
    vg = VectorizedGodel()
    expr = ["(", "¬", "→", ")"]

    token_ids = vg.to_token_ids(expr)
    assert token_ids == [1, 9, 15, 3]

    decoded = vg.decode_token_ids(token_ids)
    assert [s.name for s in decoded] == expr

def test_log_godel_calculation():
    vg = VectorizedGodel()
    expr = ["(", "¬"] # codes: 1, 9 ; primes: 2, 3
    # ln(G) = 1 * ln(2) + 9 * ln(3) = ln(2^1 * 3^9) = ln(39366)
    codes = [vg.alphabet.get_code(s) for s in expr] 
    expected_log = codes[0] * math.log(get_nth_prime(0)) + codes[1] * math.log(get_nth_prime(1))
    actual_log = vg.to_log_godel(expr)
    token_ids = vg.to_token_ids(expr)

    print("token_ids = ", token_ids)
    print("p0,p1 = ", get_nth_prime(0),get_nth_prime(1))
    assert pytest.approx(actual_log , rel= 1e-5) == expected_log

def test_one_hot_shape_and_values():
    vg = VectorizedGodel()
    expr = ["(", "¬"]
    matrix = vg.to_one_hot(expr)

    # Length of expr is 2, so 2 rows
    assert len(matrix) == 2
    # Each row must sum to 1 (one-hot property)
    assert sum(matrix[0]) == 1
    assert sum(matrix[1]) == 1

def test_invalid_inputs_raise():
    vg = VectorizedGodel()
    with pytest.raises(ValueError):
        vg.to_token_ids([])
    with pytest.raises(TypeError):
        vg.to_token_ids(123)    # type: ignore

