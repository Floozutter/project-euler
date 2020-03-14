"""
Project Euler - Problem 7
"What is the 10,001st prime number?"
"""

from itertools import islice, count
from typing import Generator, List


def is_prime(knownprimes: List[int], n: int) -> bool:
    """
    Checks if a number is prime using a List of known primes.
    """
    for p in knownprimes:
        if n % p == 0:
            return False
    return True

def primes() -> Generator[int, None, None]:
    """
    Yields prime numbers in ascending order, starting from 2.
    """
    found = []  # List of primes already found by this Generator.
    for i in count(start=2):
        if is_prime(found, i):
            yield i
            found.append(i)

def nth_prime(n: int) -> int:
    """
    Returns the nth prime number, with 2 being the first at n=1.
    """
    return next(islice(primes(), n-1, None))


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(nth_prime(10_001))


if __name__ == "__main__":
    print(answer())
