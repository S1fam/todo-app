# 1. Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.


def convert(liters_local):
    cubic_meters = liters_local / 1000
    return cubic_meters


liters = float(input("enter amount of liters: "))
print(f"{liters} liters is: {convert(liters)} cubic meters")


# Create a script that asks the user to enter a password. Then create a function that checks the strength
# of the user password. The function should return Strong Password if all the following conditions are true:
#
# Eight or more characters
#
# At least one uppercase letter.
#
# At least one digit.
#
# Here is what happens when the user provides a password that satisfies all three conditions:
#
#
# And if the user enters a password that breaks one of the three conditions, the program returns Weak Password:
#
#
# Note:  You can use the code we developed in the xBonus Example on Day 9.  For your convenience,
# you can find the code we developed in that video attached to the lecture resources of this article.

# my solution:

def password_check(lenght_local, password_local):

    result = {"lenght": False, "number": False, "uppercase": False}

    if lenght_local > 7:
        result["lenght"] = True

    for character_local in password_local:
        if "0" <= character_local <= "9":
            result["number"] = True

    for character_local in password_local:
        if "A" <= character_local <= "Z":
            result["uppercase"] = True

    if all(result.values()):
        return "Strong password"
    return "Weak password"


password = input("Enter password: ")

password_strenght = password_check(len(password), password)

print(password_strenght)


# lectors solution

user_password = input("Enter new password: ")


def strength(password_local):

    result = {}

    if len(password_local) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password_local:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(user_password))
