# 1. The code below tries to write the items of temperatures each in one line in the 6.bug-fix.txt list.
# However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

# file.writelines(temperatures) --> original - we cannot write integers into file
file.writelines(f"{temperature}\n" for temperature in temperatures)


# 2. The code below tries to convert all the numbers to integers. However, the code has an error. Try to fix the error.

numbers = [10.1, 12.3, 14.7]

# numbers = [int(number) for item in numbers] - for item (item is not defined)
numbers = [int(number) for number in numbers]
print(numbers)
