
# with open("6.bug-fix.txt", 'r') as file:
#     print(file.read())
#     print(len(file.read()))

# The Python script above is in the same directory with a file named 6.bug-fix.txt whose content is: Hello You

# The Python script should print out the content of the file and the number of characters of the text inside
# 6.bug-fix.txt. So, the expected output would be:

# Hello You
# 9
# However, the script prints out this:
#
# Hello You
# 0
# Can you fix the program so that it prints out the expected output?

with open("6.bug-fix.txt", 'r') as file:
    contents = file.read()
    print(contents)
    print(len(contents))
