"""
Project Euler - Problem 2
"By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms."
"""

from itertools import takewhile
from typing import Generator


def evenfibs() -> Generator[int, None, None]:
    """
    Yields even Fibonacci numbers, starting with 2.
    Avoids checking integer parity by leveraging the mathematical fact that
    every third Fibonacci number is even.
    This insight was taken from the user Begoner from the problem's discussion
    thread on the Project Euler website.
    """
    last, curr = 1, 2
    while True:
        yield curr
        last, curr = curr, last+curr  # curr will be odd
        last, curr = curr, last+curr  # curr will be odd, again
        last, curr = curr, last+curr  # curr will be even

def evenfibsum(upperbound: int) -> int:
    """
    Sums every even Fibonacci number that is below an upper bound.
    """
    return sum(takewhile(lambda z: z < upperbound, evenfibs()))


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(evenfibsum(4_000_000))


if __name__ == "__main__":
    print(answer())
