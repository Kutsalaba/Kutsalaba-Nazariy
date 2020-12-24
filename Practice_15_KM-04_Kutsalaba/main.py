from exp_root import root, exponentiation
from factorial import factorial
from logarithm import logarithm


menu = {
    1 : factorial.fact,
    2 : root.root2,
    3 : root.root3,
    4 : exponentiation.exp2,
    5 : exponentiation.exp3,
    6 : logarithm.log,
    7 : logarithm.ln,
    8 : logarithm.lg
}

def main():
    print("             Menu\n\n"
          "Calculate the factorial of the number  - 1\n"
          "Calculate the square root of a number  - 2\n"
          "Calculate the cubic root  - 3\n"
          "Bring to a square  - 4\n"
          "Bring to a cube  - 5\n"
          "Calculate the logarithm  - 6\n"
          "Calculate the natural logarithm  - 7\n"
          "Calculate the logarithm to the base ten - 8\n\n")

    def check():
        try:
            choice = int(input("Enter a number from the menu to start the program: "))
            if 1 <= choice <= 8:
                return menu[choice]()

            else:
                raise ValueError

        except ValueError:
            print("Error, select a number from the menu.")
            return check()

    check()
    goaway = input("If you want to view the menu and use the program, "
                   "enter \"yes\" again and click \"Enter\", if you do not want to click \"Enter\": ")

    if goaway == 'yes':
        return main()

if __name__ == '__main__':
    main()




