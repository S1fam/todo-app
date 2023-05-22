password = input("Choose password: ")
print("you have chose your password, confirm it please:")

try_pasword = "null"
password_guessed = False
attempt_count = 0

while password != try_pasword:
    print("Enter password: (", (3-attempt_count), " attempts left)")
    try_pasword = input("password:")
    if try_pasword == password:
        password_guessed = True
        break
    print("password was incorrect")
    attempt_count += 1
    if attempt_count >= 3:
        break

if password_guessed is True:
    print("password was confirmed")
else:
    print("you did not confirm your password")

i = 1
while i <= 6:
    print(i)
    i += 1
