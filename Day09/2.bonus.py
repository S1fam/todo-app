# we are checking password strenght
# conditions for strenght: lenght 8, number, uppercase

# 1. my solution

password = input("Enter password: ")

number_amount = 0
for character in password:
    if "0" <= character <= "9":
        number_amount += 1

uppercase_amount = 0
for character in password:
    if "A" <= character <= "Z":
        uppercase_amount += 1

if len(password) >= 8:
    if number_amount > 0:
        if uppercase_amount > 0:
            print("Strong password")
else:
    print("Weak password")


# 2. instructors solution

password = input("Enter new password: ")  # getting an input

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)


digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)


upper = False
for i in password:
    if i.isupper():
        upper = True

result.append(upper)

if all(result):
    print("Strong password")
else:
    print("Weak password")


# 3. introduction to dictionaries!??

password = input("Enter new password: ")  # getting an input

result = {}  # creates empty dictionary

if len(password) >= 8:
    result["lenght"] = True  # appends dictionary by key of "lenght" with value True {"lenght": True}
else:
    result["lenght"] = False  # appends dictionary by key of "lenght" with value False {"lenght": False}


digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit  # appends dictionary by key of "digits" with value True/False {"lenght": True, "digits": True}


upper = False
for i in password:
    if i.isupper():
        upper = True

result["uppercase"] = upper  # {"lenght": True/False, "digits": True/False, "uppercase": True/False}

print(result)

if all(result.values()):  # .result() would check key, we want to check values
    print("Strong password")
else:
    print("Weak password")
