def is_three_or_four_digits(nb) -> bool:
    """ Check if the number is three or four digits. """
    return 100 <= nb <= 9999 and len(set(str(nb))) > 1

def sort_digits(nb, digit_count) -> tuple:
    """ Transform the number to a tuple of its digits sorted in ascending and descending order. """
    str_nb = f"{nb:0{digit_count}d}"
    asc_digits = ''.join(sorted(str_nb))
    desc_digits = ''.join(sorted(str_nb, reverse=True))
    return (int(asc_digits), int(desc_digits))