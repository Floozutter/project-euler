"""
Project Euler - Problem 4
"Find the largest palindrome made from the product of two 3-digit numbers."
"""

from itertools import combinations_with_replacement


def palindromic(s: str) -> bool:
    """
    Checks whether a string is a palindrome.
    """
    size = len(s)
    for i in range(size // 2):
        if s[i] != s[size - 1 - i]:
            return False
    return True
        
def largest_palindrome_product(digits: int) -> int:
    """
    Returns the largest palindrome product of two n-digit numbers.
    """
    factors = range(10**(digits-1), 10**digits)
    pairs = combinations_with_replacement(factors, 2)
    products = (p[0]*p[1] for p in pairs)
    sortedproducts = sorted(products, reverse=True)
    return next(filter(lambda z: palindromic(str(z)), sortedproducts))


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(largest_palindrome_product(3))


if __name__ == "__main__":
    print(answer())
