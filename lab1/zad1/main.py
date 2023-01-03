from fractions import Fraction
from multiprocessing.sharedctypes import Value
from sys import argv


def sanitize_number(arg):
    # can be replaced with simple regex
    if isinstance(arg, str):
        no_digit_arg = arg
        for i in range(10):
            no_digit_arg = no_digit_arg.replace(f'{i}', '')
        if no_digit_arg == '.':
            return float(arg)
        elif len(no_digit_arg) == 0:
            return int(arg)
        else:
            # return 0
            return None
    elif isinstance(arg, int) or isinstance(arg, float) or isinstance(arg, Fraction) or isinstance(arg, complex):
        return arg
    else:
        return None

def sum(arg1, arg2):
    arg1 = sanitize_number(arg1)
    arg2 = sanitize_number(arg2)
    if arg1 is not None and arg2 is not None:
        return arg1 + arg2
    else:
        raise TypeError("Invalid value")

if __name__ == "__main__":
    if len(argv) > 2:
        try:
            print(f"suma = {sum(argv[1], argv[2])}")
        except TypeError:
            print("Invalid argument")

    print(f"__name__ = {__name__}")