"""
Project Euler - Problem 9
"There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c."
"""

from typing import NamedTuple


class GaussianInt(NamedTuple):
    real: int
    imag: int


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print(answer())
