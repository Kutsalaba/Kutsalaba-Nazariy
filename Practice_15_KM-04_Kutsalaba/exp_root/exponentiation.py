"""
This module is designed to square numbers or to a cube
"""


def exp2():

    try:
        n = float(input("Enter the number: "))
        print(f'{n} squared = {round(n ** 2, 5)}')
        return round(n ** 2, 5)

    except ValueError:
        print("Error, enter the data correctly.")
        return exp2()


def exp3():

    try:
        n = float(input("Enter the number: "))
        print(f'{n} squared = {round(n ** 3, 5)}')
        return round(n ** 3, 5)

    except ValueError:
        print("Error, enter the data correctly.")
        return exp3()

