#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 13th Oct 2026
# This program uses a random number generator to choose a
# random number and then asks the user to try guessing it
import random


def main():
    # set up the random number generator
    number = int(random.randint(0, 9))

    # get the user guess number
    user_number = int(input("Enter your guess number : "))

    # check if the user guess is correct
    if user_number == number:
        print("you guessed correctly!!")
    else:
        print("you guessed wrong!!")
        print("The correct answer was : {}".format(number))


if __name__ == "__main__":
    main()
