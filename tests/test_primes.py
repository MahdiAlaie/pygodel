import pytest
from pygodel.primes import get_nth_prime,prime_factorization,prime_generator

def test_prime_generator_sequence():
    gen = prime_generator()
    expected = [2,3,5,7,11,13,17,19,23,29]
    result = [next(gen) for _ in range(10)]
    assert result == expected


def test_get_nth_prime():
    assert get_nth_prime(0) == 2
    assert get_nth_prime(2) == 5
    assert get_nth_prime(4) == 11
    with pytest.raises(ValueError):
        get_nth_prime(-1)

def test_prime_factorization():
    assert prime_factorization(12) == [(2,2),(3,1)]
    assert prime_factorization(13) == [(13,1)]
    assert prime_factorization(360) == [(2,3),(3,2),(5,1)]
    with pytest.raises(ValueError):
        prime_factorization(1)