def main():
    """This is the main function in which all the auxiliary functions are located. It also displays the result

    """

    def check_input():
        """This function checks the correctness of user input.

        :return: positive integer
        """

        while True:
            number_input = input('Enter a positive integer: ')

            if number_input.isdigit():
                if int(number_input) > 0:
                    break
            print(f'Please, enter a positive integer.')
        return int(number_input)

    numerator = check_input()
    denominator = check_input()


    def reduced_share(numer, denom):
        """This function divides the numerator and denominator by the same number

        :param numer: int, this is the numerator of the fraction
        :param denom: int, this is the denominator of the fraction
        :return: number, denom
        """

        while numer != 0 and denom != 0:
            if numer > denom:
                numer = numer % denom
            else:
                denom = denom % numer
        largest_divisor = numer + denom

        return numerator // largest_divisor, denominator // largest_divisor


    up_numerator, up_denominator = reduced_share(numerator, denominator)
    print(f'The initial fraction: {numerator}/{denominator}')

    if up_denominator == 1:
        print(f'After reductions the fraction is equal: {up_numerator}')
    else:
        print(f'After reduction, our fraction looks like this: {up_numerator}/{up_denominator}')

    goaway = input("Щоб вийти з програми клацніть \"Enter\""
                   "\nЩоб почати програму знову введіть \"так\" та клацніть \"Enter\" : ")
    if goaway == "так":
        main()


if __name__ == '__main__':
    main()