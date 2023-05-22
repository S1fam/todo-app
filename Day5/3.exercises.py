# 1 - filenames = ['document', 'report', 'presentation']
# to output - 0-Document.txt..

filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    row = f"{index}-{item.capitalize()}.txt"
    print(row)

# ips = ['100.122.133.105', '100.122.133.111']
# Copy-paste the ips list in a .py file and extend the program so it:
# 1. Prompts the user to input an index (e.g, 0 or 1).
# 2. 2. Returns the IP address that has that index.

ips = ['100.122.133.105', '100.122.133.111']

index = int(input("Enter the index of the IP you want: "))

print(f"You chose {ips[index]}")
