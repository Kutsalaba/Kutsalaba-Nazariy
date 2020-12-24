"""
This module finds cubic or square roots
"""

def root2():

    try:
        n = float(input("Enter a positive number: "))
        if n > 0:
            print(f'The square root of a {n} = {round(n ** (1/2), 5)}')
            return round(n ** (1/2), 5)
        else:
            raise ValueError
    except ValueError:
        print("Error, enter the data correctly.")
        return root2()


def root3():

    try:
        n = float(input("Enter a positive number: "))
        if n > 0:
            print(f'The square root of a {n} = {round(n ** (1/3), 5)}')
            return round(n ** (1/3), 5)
        else:
            raise ValueError
    except ValueError:
        print("Error, enter the data correctly.")
        return root3()


