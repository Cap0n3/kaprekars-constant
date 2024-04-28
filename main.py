"""
Little script to find Kaprekar's constant for a 4-digit number and 3-digit number.

See https://demian.ferrei.ro/blog/programmer-vs-mathematician
See https://en.wikipedia.org/wiki/6174_(number) for more information.
"""

from kaprekar.utils import is_four_digits, is_three_digits
from kaprekar.kaprekar_routine import kaprekar_routine

if __name__ == "__main__":
    while True:
        choice = input("Do you want to find Kaprekar's constant for a 4-digit number or 3-digit number? (4/3): ")
        if choice == "4":
            # Ask for a 4-digit number
            while True:
                input_nb = input("Enter a 4-digit number: ")
                if input_nb.isdigit() and is_four_digits(int(input_nb)):
                    break
                print("Invalid number. Please enter a 4-digit number with at least two different digits.\n")
        elif choice == "3":
            # Ask for a 3-digit number
            while True:
                input_nb = input("Enter a 3-digit number: ")
                if input_nb.isdigit() and is_three_digits(int(input_nb)):
                    break
                print("Invalid number. Please enter a 3-digit number with at least two different digits.\n")
        else:
            print("Invalid choice. Please enter 4 or 3.\n")
            continue
    
        kaprekar_routine(int(input_nb), int(choice))