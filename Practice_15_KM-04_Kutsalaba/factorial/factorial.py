
"""This module calculates the factorial of a number"""

def fact(factorial = 1):

    try:
        n = int(input("Enter a natural number: "))
        if n >= 0:
            while n > 1:
                factorial *= n
                n -= 1
            print(f'Factorial of the entered number = {factorial}')
            return factorial
        else:
            raise ValueError

    except ValueError:
        print("Error, enter the data correctly.")
        return fact()

