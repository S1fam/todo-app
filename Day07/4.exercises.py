# 1. names = ["john smith", "jay santi", "eva kuki"]
# Extend the code above so the code capitalizes all the names and surnames of the list and then prints the new list.

names = ["john smith", "jay santi", "eva kuki"]

new_names = [name.capitalize() for name in names]
print("List of new names: ", new_names, "\n")


# 2. usernames = ["john 1990", "alberta1970", "magnola2000"]
# Extend the code above so the code prints out a list containing the number of characters for each username.

usernames = ["john 1990", "alberta1970", "magnola2000"]

usernames_lenght = [len(username) for username in usernames]
print("Lenght of usernames: ", usernames_lenght, "\n")


# 3. user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out a list containing the same items as floats.

user_entries = ['10', '19.1', '20']
print("Entries in string: ", user_entries, "\n")

user_entries_in_floats = [float(entry) for entry in user_entries]
print("Entries in floats: ", user_entries_in_floats, "\n")

# voluntary
user_entries_in_ints = [int(entry) for entry in user_entries_in_floats]  # a) since in original list there is
print("Entries in ints: ", user_entries_in_ints, "\n")  # b) a string value "19.1" we must first convert to floats


# 4. user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out the sum of the numbers.

user_entries = ['10', '19.1', '20']
user_entries_in_floats = [float(entry) for entry in user_entries]
print("the sum of user entries: ", sum(user_entries_in_floats), "\n")
