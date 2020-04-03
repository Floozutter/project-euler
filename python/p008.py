"""
Project Euler - Problem 8
"Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?"
"""

from functools import reduce
from operator import mul
from typing import Sequence, Generator, TypeVar


def prod(digits: str) -> int:
    """
    Returns the product of a string of digits.
    """
    return reduce(mul, map(int, digits))

T = TypeVar("T")
def sliding_window(
    seq: Sequence[T],
    slicesize: int
) -> Generator[Sequence[T], None, None]:
    """
    Yields same-sized slices of the argument Sequence.
    """
    for i in range(len(seq) - slicesize + 1):
        yield seq[i : i+slicesize]

def lpoad(digits: str, slicesize: int) -> int:
    """
    Returns the largest product of adjacent digits from a string of digits.
    """
    # Group the string of digits into overlapping slices.
    digslcs = sliding_window(digits, slicesize)
    # Begin by accumulating the product of the first slice.
    product = prod(next(digslcs))  # Product of the current slice.
    largest = product    # Largest product encountered.
    lastdig = digits[0]  # Oldest digit of the previous slice.
    # Get each next product by first dividing out the oldest digit of the
    # previous slice, then multiplying in the newest digit of the next slice.
    for ds in digslcs:
        if lastdig == "0":      # A zero results in information loss.
            product = prod(ds)  # Accumulate again.
        else:
            product //= int(lastdig)  # Divide out oldest digit.
            product  *= int(ds[-1])   # Multiply in newest digit.
        lastdig = ds[0]  # Update oldest digit.
        # Update largest when applicable.
        if product > largest:
            largest = product
    return largest
    

def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(lpoad(
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450",
        13
    ))


if __name__ == "__main__":
    print(answer())
