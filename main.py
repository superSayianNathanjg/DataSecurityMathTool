import sys


def fast_exponent(a, z, n):
    x = 1
    print("\n\n\nFastExponentAlgo\n")
    while z != 0:
        while z % 2 == 0:
            print("z currently equals: " + str(z))
            print("z % 2 == 0, so we divide z by 2")
            z = z / 2
            print("z now equals: " + str(z))
            print("a currently equals: " + str(a))
            a = a * a % n
            print("a*a % mod n => a equals: " + str(a))
        print("\nz != to z % 2 == 0, so we subtract 1 from z")
        z = z - 1
        print("z now equals: " + str(z))
        print("x = x*a mod n")
        x = x * a % n
        print("x now equals to: " + str(x))
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
    a = int(input("Input your base number 'a': "))
    n = int(input("Input your modulo 'n': "))
    r = a % n
    print("a mod n = " + str(a) + " mod " + str(n) + "\nEquals: " + str(r))
    print("Returning to menu")
    menu()


def menu():
    print("\n___Data Sec Calculator Tool___")
    print("1: Normal Modulo Calculator")
    print("2: Fast Modular with Exponent Calculator")
    print("0: Exit Program")
    menu_choice = input("Choose an option: \n")

    if menu_choice == "1":
        normal_mod()
    elif menu_choice == "2":
        get_numbers()
    elif menu_choice == "0":
        sys.exit()
    else:
        print("You must select either 1 or 2")
        print("Please try again")
        menu()


if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
