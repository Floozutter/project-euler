"""
Project Euler - Problem 1
"Find the sum of all the multiples of 3 or 5 below 1000."
"""

def sum_multiples(divisor: int, terms: int) -> int:
    """
    Sums the first N multiples of a divisor.
    Uses the arithmetic series formula.
    """
    return divisor * (terms * (terms + 1)) // 2

def fizzbuzzsum(upperbound: int) -> int:
    """
    Sums every multiple of 3 or 5 below an upper bound.
    This is achieved by summing the 3-multiples with the 5-multiples, then
    subtracting the 15-multiples from that to remove duplicated terms.
    """
    fizzsum      = sum_multiples( 3, (upperbound-1) //  3)
    buzzsum      = sum_multiples( 5, (upperbound-1) //  5)
    intersectsum = sum_multiples(15, (upperbound-1) // 15)
    return fizzsum + buzzsum - intersectsum


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(fizzbuzzsum(1000))


if __name__ == "__main__":
    print(answer())
