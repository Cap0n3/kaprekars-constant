"""
Little script to find Kaprekar's constant for a 4-digit number.

See https://demian.ferrei.ro/blog/programmer-vs-mathematician
See https://en.wikipedia.org/wiki/6174_(number) for more information.
"""

def transform_asc_desc(nb):
    """
    Transform a number into a tuple of two numbers, the first one is the number
    with its digits sorted in ascending order, the second one is the number with
    its digits sorted in descending order.
    """
    def check_three_digit(nb_lst):
        if len(nb_lst) < 4:
            nb_lst.insert(0, 0)
        return nb_lst
    to_int_lst = lambda num: [int(x) for x in str(num)]
    to_num = lambda int_lst: int("".join([str(x) for x in int_lst]))
    asc_lst = check_three_digit(to_int_lst(nb))
    desc_lst = check_three_digit(to_int_lst(nb))
    asc_lst.sort()
    desc_lst.sort(reverse=True)
    return (to_num(asc_lst), to_num(desc_lst))


if __name__ == "__main__":
    input_nb = int(input("Please, enter a 4-digit number : "))
    # Check if number is a 4-digit number
    if input_nb < 1000 or input_nb > 9999:
        print("Please enter a 4-digit number.")
        exit()
    # Check if number has at least two different digits
    if len(set([int(x) for x in str(input_nb)])) == 1:
        print("Please enter a number with at least two different digits.")
        exit()
    # Search the constant
    found_rec = False
    res_lst = []
    print("\n🔍 Searching constant ...\n")
    while not found_rec:
        asc, desc = transform_asc_desc(input_nb)
        res = desc - asc
        print(f"{input_nb} -> {desc} - {asc} = {res}")
        input_nb = res
        if res in res_lst:
            found_rec = True
            print(f"\n✨ Found Kaprekar's constant : {res_lst[-1]}")
        else:
            res_lst.append(res)
