from .utils import sort_digits

def kaprekar_routine(input_nb, digits) -> None:
    """ Routine to find Kaprekar's constant for a given 4-digit number. """
    res_set = set()
    print("\n🔍 Searching for Kaprekar's constant ...\n")
    while True:
        asc, desc = sort_digits(input_nb, digits)
        result = desc - asc
        print(f"{input_nb} -> {desc} - {asc} = {result}")
        if result in res_set:
            print(f"\n✨ Found Kaprekar's constant: {result}\n")
            return result
        res_set.add(result)
        input_nb = result