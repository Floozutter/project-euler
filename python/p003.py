"""
Project Euler - Problem 3
"What is the largest prime factor of the number 600851475143?"
"""

from math import sqrt


def largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of a natural number greater than 1.
    """
    lpf = n            # current candidate for the largest prime factor
    upper = sqrt(lpf)  # inclusive upper bound of possible factors
    i = 2              # factors to check
    while i <= upper:
        quotient, remainder = divmod(lpf, i)
        if remainder == 0:     # 2 factors found, i and the quotient
            lpf = quotient     # update candidate with the larger factor
            upper = sqrt(lpf)  # update upper bound using the new candidate
        else:
            i += 1
    return lpf


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(largest_prime_factor(600851475143))


if __name__ == "__main__":
    print(answer())
