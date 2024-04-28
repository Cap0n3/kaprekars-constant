def is_three_digits(nb) -> bool:
    """ Check if the number is a valid three-digit number. """
    if 100 <= nb <= 999 and len(set(str(nb))) > 1:
        return True
    return False

def is_four_digits(nb) -> bool:
    """ Check if the number is a valid four-digit number with at least two different digits. """
    if 1000 <= nb <= 9999 and len(set(str(nb))) > 1:
        return True
    return False

def transform_four_digits(nb) -> tuple:
    """ Transform the number to a tuple of its digits sorted in ascending and descending order. """
    str_nb = f"{nb:04d}"  # Ensure the number has four digits
    asc_digits = ''.join(sorted(str_nb))
    desc_digits = ''.join(sorted(str_nb, reverse=True))
    return (int(asc_digits), int(desc_digits))

def transform_three_digits(nb) -> tuple:
    """ Transform the number to a tuple of its digits sorted in ascending and descending order. """
    str_nb = f"{nb:03d}"  # Ensure the number has three digits
    asc_digits = ''.join(sorted(str_nb))
    desc_digits = ''.join(sorted(str_nb, reverse=True))
    return (int(asc_digits), int(desc_digits))
