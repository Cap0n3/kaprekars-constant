"""
Little script to find Kaprekar's constant for a 4-digit number.

See https://demian.ferrei.ro/blog/programmer-vs-mathematician
See https://en.wikipedia.org/wiki/6174_(number) for more information.
"""

from kaprekar.utils import is_valid_number
from kaprekar.kaprekar_routine import kaprekar_routine

if __name__ == "__main__":
    while True:
        input_nb = int(input("Please, enter a 4-digit number: "))
        if is_valid_number(input_nb):
            break
        print("Invalid input. Ensure you enter a 4-digit number with at least two different digits.")

    kaprekar_routine(input_nb)