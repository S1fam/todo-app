# we also don't want to accept squares (same width and lenght)

try:
    width = float(input("Enter rectangle width: "))
    lenght = float(input("Enter rectangle lenght: "))
    if width == lenght:
        exit(print("you entered a square"))  # we can also enter eit("message"), the message will then be displayed red

    area = width * lenght
    print(area)
except ValueError:
    print("Please enter a number.")
