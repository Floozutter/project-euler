"""
Project Euler - Problem 4
"Find the largest palindrome made from the product of two 3-digit numbers."
"""

from heapq import merge
from typing import Iterable


def palindromic(s: str) -> bool:
    """
    Checks whether a string is a palindrome.
    """
    size = len(s)
    for i in range(size // 2):
        if s[i] != s[size - 1 - i]:
            return False
    return True

def descending_products(incl_upper: int, excl_lower: int) -> Iterable[int]:
    """
    Returns every product of two ranged factors, in descending order.
    The upper bound is inclusive, the lower bound is exclusive.
    Works by generating sorted rows of multiples for each ranged factor, then
    merging the sorted rows together with heapq.
    """
    def multiples(factor: int) -> Iterable[int]:
        """
        Returns multiples of the factor, in descending order.
        The multiples are within the bounds [factor*factor, factor*excl_lower).
        """
        return [factor*n for n in range(factor, excl_lower, -1)]
    rows = (multiples(factor) for factor in range(incl_upper, excl_lower, -1))
    return merge(*rows, reverse=True)

def largest_palindrome_product(digits: int) -> int:
    """
    Returns the largest palindrome product of two n-digit numbers.
    """
    upper = 10**digits - 1      # inclusive upper bound for n-digit factors
    lower = 10**(digits-1) - 1  # exclusive lower bound for n-digit factors
    products = descending_products(upper, lower)
    return next(filter(lambda z: palindromic(str(z)), products))


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(largest_palindrome_product(3))


if __name__ == "__main__":
    print(answer())
