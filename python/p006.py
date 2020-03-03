"""
Project Euler - Problem 6
"Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."
"""

def sum_square_difference(n: int) -> int:
    """
    Returns the "sum square difference" of the first n natural numbers.
    """
    square_of_sum = (n*(n+1) // 2)**2
    sum_of_squares = n*(n+1)*(2*n+1) // 6
    return square_of_sum - sum_of_squares
            

def answer() -> str:
    """
    Returns the answer to the problem as a string.
    """
    return str(sum_square_difference(100))


if __name__ == "__main__":
    print(answer())
