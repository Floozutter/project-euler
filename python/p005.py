"""
Project Euler - Problem 5
"What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"
"""

from math import gcd
from functools import reduce


def lcm(a: int, b: int) -> int:
    """
    Returns the least common multiple of two natural numbers.
    """
    return (a*b) // gcd(a, b)

def lcm_of_naturals(terms: int) -> int:
    """
    Returns the least common multiple of the first n natural numbers.
    """
    return reduce(lcm, range(1, terms+1), 1)
            

def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(lcm_of_naturals(20))


if __name__ == "__main__":
    print(answer())
