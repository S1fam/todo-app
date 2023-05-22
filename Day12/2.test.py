
def greet(message):
    new_message = message.capitalize()
    print("Hey hey")
    return new_message


user_entry = input("What greeting do you prefer: ")
greeting = greet(user_entry)

print(greeting)
