"""
Project Euler - Problem 5
"What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"
"""

from itertools import chain
from typing import Set, FrozenSet


def factors(n: int) -> FrozenSet[int]:
    """
    Returns a FrozenSet of a natural number's factors.
    """
    factors = chain(
        filter(lambda i: n%i == 0, range(1, n)),
        (n,)  # Iterable Tuple of only n (a number is its own factor)
    )
    return frozenset(factors)

def smallest_multiple(upper: int) -> int:
    """
    Returns the smallest multiple of the numbers in [1, upper].
    """
    smolmult = 1  # running product for the smallest multiple
    included_factors = set()
    for i in range(upper, 0, -1):
        if i not in included_factors:
            smolmult *= i
            included_factors.update(factors(i))
    return smolmult
            

def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(smallest_multiple(10))


if __name__ == "__main__":
    print(answer())
