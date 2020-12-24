from math import log10, log as logarithm

"""
This module calculates different logarithms
"""

def log():
    def check_b():
        try:
            b = float(input("Enter the number: "))
            if b > 0:
                return b
            else:
                raise ValueError
        except ValueError:
            print("Error, enter the data correctly.")
            return check_b()

    def check_a():
        try:
            a = float(input("Enter the base of the number: "))
            if a > 0 and a != 1:
                return a
            else:
                raise ValueError
        except ValueError:
            print("Error, enter the data correctly.")
            return check_a()

    a = check_a()
    b = check_b()
    print(f'Logarithm with base {a}, from the number {b} = {round(logarithm(b, a), 5)}')
    return round(logarithm(b, a), 5)


def ln():
    try:
        b = float(input("Enter the number: "))
        if b > 0:
            print(f'The logarithm is natural from {b} = {round(logarithm(b), 5)}')
            return round(logarithm(b), 5)
        else:
            raise ValueError
    except ValueError:
        print("Error, enter the data correctly.")
        return ln()


def lg():
    try:
        b = float(input("Enter the number: "))
        if b > 0:
            print(f'Logarithm with base ten from number {b} = {round(log10(b), 5)}')
            return round(log10(b), 5)
        else:
            raise ValueError
    except ValueError:
        print("Error, enter the data correctly.")
        return lg()
