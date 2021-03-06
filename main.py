import sys


def fast_exponent(a, z, n):
    x = 1
    print("\n\n\nFastExponentAlgo\n")
    print(str(a) + "^" + str(z) + " mod " + str(n) + " = ")
    while z != 0:
        while z % 2 == 0:
            print(str(a) + "*" + str(a) + "^" + str(z) + " mod " + str(n))
            z = z / 2
            print(str(a) + "*" + str(a) + "^" + str(z) + " mod " + str(n))
            a = a * a % n
            print("Equals = \n" + str(x) + " * " + str(a) + "*" + str(a) + "^" + str(z) + " mod " + str(n))
        z = z - 1
        print("z equals: " + str(z))
        x = x * a % n
        print("x equals: " + str(x))
        print("\nRestart loops\n")
    return x


def get_numbers():
    print("Enter math problem with exponent and modular\n x = a^z mod n")
    a = int(input("Enter base 'a': "))
    z = int(input("Enter exponent 'z': "))
    n = int(input("Enter modulo 'n': "))

    print("The answer to: " + str(a) + "^" + str(z) + " mod " + str(n) + " is: " + str(fast_exponent(a, z, n)))


# Press the green button in the gutter to run the script.
def normal_mod():
    print("Enter base number a, and modular n,\n a mod n")
    a = int(input("Input base number 'a': "))
    n = int(input("Input modulo 'n': "))
    r = a % n
    print("a mod n = " + str(a) + " mod " + str(n) + "\nEquals: " + str(r))
    print("Returning to menu")
    menu()


def greatest_common_divisor(num1, num2):
    g = [num1, num2]
    i = 1
    while g[i] != 0:
        g.append(g[i - 1] % g[i])
        i = i + 1
    print(str(g[i - 1]))
    # a = num1
    # n = num2
    # r = 0
    # swap_val = 0
    # gcd_final = 0
    #
    # if a > n:
    #     r = a % n  # Remainder equals % of a/n.
    #     a = a / n  # A divided by n
    #     if r > 0:
    #         a = n
    #         n = r
    #         greatest_common_divisor(a, n)
    #     else:
    #         print("\nFinal value of b and greatest common divisor = " + str(n))
    #         return
    # else:
    #     swap_val = a
    #     a = n
    #     n = swap_val
    #     greatest_common_divisor(a, n)


def euclidid_gcd_algo():
    a = int(input("Enter value for a"))
    n = int(input("Enter value for n"))
    greatest_common_divisor(a, n)  # Get input and then calculate
    menu()


def menu():
    print("\n___Data Sec Calculator Tool___")
    print("1: Normal Modulo Calculator")
    print("2: Fast Modular with Exponent Calculator")
    print("3: Greatest Common Divisor calculator")
    print("0: Exit Program")
    menu_choice = input("Choose an option: \n")

    if menu_choice == "1":
        normal_mod()
    elif menu_choice == "2":
        get_numbers()
    elif menu_choice == "3":
        euclidid_gcd_algo()
    elif menu_choice == "0":
        sys.exit()
    else:
        print("You must select either 1, 2, or 3")
        print("Please try again")
        menu()


if __name__ == '__main__':
    menu()
