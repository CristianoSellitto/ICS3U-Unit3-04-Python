#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if the user's integer is positive, negative, or zero


def main():
    # Finds if the user's integer is positive, negative, or zero

    integer = int(input("Enter an integer: "))
    if integer > 0:
        print("\n{} is a positive integer.".format(integer))
    elif integer < 0:
        print("\n{} is a negative integer.".format(integer))
    else:
        print("\n{} is zero.".format(integer))

    print("\nDone.")


if __name__ == "__main__":
    main()
