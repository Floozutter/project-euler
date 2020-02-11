"""
Project Euler - Problem 0
Template file for my Project Euler problem solutions.
"""

def foo(bar: int) -> int:
    """
    Performs a computation related to the problem at hand.
    """
    return 142857 * bar


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(foo(7))


if __name__ == "__main__":
    print(answer())
