# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program asks for a number, then checks if it is
# greater than 0 by continuously adding one to the 0


def main():
    # this function loops until it is less than the user integer
    # and creates an addition sequence

    # while loop variable
    sum = 0
    digit_one = 0

    # input
    user_number = input("Enter in a positive integer: ")
    print("")

    # process & output
    try:
        user_number_int = int(user_number)

        while digit_one < user_number_int:
            sum = sum + user_number_int
            user_number_int = user_number_int - 1

        print(
            "The sum of all positive integers from 1 to {0} is {1}".format(
                user_number, sum
            )
        )

    except Exception:
        print("That is an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
