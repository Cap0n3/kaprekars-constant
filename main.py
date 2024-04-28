"""
Little script to find Kaprekar's constant for a 4-digit number and 3-digit number.

See https://demian.ferrei.ro/blog/programmer-vs-mathematician
See https://en.wikipedia.org/wiki/6174_(number) for more information.
"""

from kaprekar.utils import is_three_or_four_digits
from kaprekar.kaprekar_routine import kaprekar_routine

if __name__ == "__main__":
    while True:
        input_nb = input("Enter a 3-digit or 4-digit number: ")
        if is_three_or_four_digits(int(input_nb)):
            break
        print("\nPlease enter a valid 3-digit or 4-digit number with at least two different digits.\n")
    
    kaprekar_routine(int(input_nb), len(input_nb))