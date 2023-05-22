# Supposedly, the following program should: 1. Prompt the user to input an index (e.g., 0, 1, or 2).
# 2. Print out the item with that index. However, there is a bug with the program which you should try to fix.

menu = ["pasta", "pizza", "salad"]

user_choice = input("Enter the index of the item: ")

message = f"You chose {menu[int(user_choice)]}."  # missing int()
print(message)


# 2.

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):  # wrong brackets were used [] instead of ()
    print(f"{i}.{j}")


# 3.

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")  # f was inside the parantheses like "f..."
