"""Prime number generator and factorization engine for Godel numbering."""

from typing import Iterator

def prime_generator() ->Iterator[int]:
    """Generate an infinte sequence of prime numbers lazily using a sieve/trial division approch."""
    yield 2
    primes = [2]
    candidate = 3
    while True:
        is_prime = True
        limit = int(candidate ** 0.5)
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0 :
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2

def get_nth_prime(n:int) -> int:
    """Return the n-th prime number (0-indexed: 0th prime is 2, 1st is 3, etc)."""
    if n < 0 :
        raise ValueError("Prime index must be non-negative.")
    gen = prime_generator()
    for _ in range(n):
        next(gen)
    return next(gen)

def prime_factorization (n:int) -> list[tuple[int,int]]:
    """Decompose a positive integer into its prime factors.
    
    Return a list of tuples : (prime, exponent).
    Example: prime_factorization(12) -> [(2,2), (3,1)] (since 12 = 2^2 * 3^1)
    """

    if n <= 1 : 
        raise ValueError("Factorization is only defined for integers greater than 1.")

    factors = []
    d = 2
    temp = n
    while d * d <= temp :
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1 
                temp //= d
            factors.append((d,count))
        d += 1
    if temp > 1 :
        factors.append((temp,1))
    return factors

