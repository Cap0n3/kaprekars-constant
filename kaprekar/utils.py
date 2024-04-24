def transform_number(nb) -> tuple:
    """ Transform the number to a tuple of its digits sorted in ascending and descending order. """
    str_nb = f"{nb:04d}"  # Ensure the number has four digits
    asc_digits = ''.join(sorted(str_nb))
    desc_digits = ''.join(sorted(str_nb, reverse=True))
    return (int(asc_digits), int(desc_digits))

def is_valid_number(nb) -> bool:
    """ Check if the number is a valid four-digit number with at least two different digits. """
    if 1000 <= nb <= 9999 and len(set(str(nb))) > 1:
        return True
    return False