# 1. Your task is to create a program that generates a random whole number.
# As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number,
# the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers.

import random

try:
    minimal = int(input("Enter the lower bound: "))
    maximal = int(input("Enter the upper bound: "))
except ValueError:
    exit("Enter number")

try:
    random_number = random.randint(minimal, maximal)
    print(random_number)
except ValueError:
    exit("first number input must be lower than the second one")
    