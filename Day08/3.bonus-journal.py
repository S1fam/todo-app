date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"files/journal/{date}.txt", "w") as file:  # having /files/journal.. did not work
    file.write(mood + 2 * "\n")
    file.write(thoughts)
