# 1. Bug-Fixing Exercise 1: The program below intends to find out how many items have at least one underscore ("_")
# character in them.  However, there is an error with the code. Try to find and fix it.

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for i in ids:  # there was id instead of i. that is built in function so we cant use it as a name to iterate over
    if '_' in i:  # here aj did swap id for i aswell, also this part was not indented which pycharm fixed for me
        x = x + 1
print(x)


# 2. Bug-Fixing Exercise 2: This program also intends to find out how many items have an underscore in them.
# However, the program has a bug. It doesn't return an error message, but it returns: 1\n 1\n 2\n  (\n makes newline)
# Instead, the expected output is: 2
# Try to fix the program, so it returns the expected output. Here is the buggy program:

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for i in ids:  # swap id for i, which was not again the crucial issue, but pycharm is suggesting i dont use id
    if '_' in i:
        x = x + 1
print(x)  # had to lower the indent


# 3. Bug-Fixing Exercise 3: Fix the program below so that it prints out "OK"
# when the perimeter is less than 14 and the area is less than 8.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:  # was area > 10
    print("OK")
else:
    print("NOT OK")
