"""
Project Euler - Problem 2
"By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms."
"""

def evenfibsum(upperbound: int) -> int:
    """
    Sums every even Fibonacci number below an upper bound.
    This implementation avoids checking integer parity by leveraging the
    mathematical fact that every third Fibonacci number is even.
    This insight was taken from the user Begoner from the problem's discussion
    thread on the Project Euler website.
    """
    total = 0
    last, curr = 1, 2
    while curr < upperbound:
        total += curr
        last, curr = curr, last+curr  # curr will be odd
        last, curr = curr, last+curr  # curr will be odd, again
        last, curr = curr, last+curr  # curr will be even
    return total


def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(evenfibsum(4_000_000))


if __name__ == "__main__":
    print(answer())
