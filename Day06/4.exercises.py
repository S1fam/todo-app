# 1. open essays.txt, create program that prints out its text and capitalizes it

file = open(f"files/exercises/essay.txt", 'r')
contents = file.read()
print(contents.capitalize())
file.close()


# 2. read essays.txt and return number of characters

print("Lenght of essays.txt is: ", len(contents))


# 3. enter a new member into members.txt

file = open(f"files/exercises/members.txt", 'r')
members = file.readlines()
file.close()

new_member = input("Add a new member: ")
members.append(f"{new_member}\n")

file = open(f"files/exercises/members.txt", 'w')
file.writelines(members)
file.close()

print(members)


# 4. Create a program that generates multiple text files by iterating over the filenames list.
# The text Hello should be written inside each generated text file.

filenames = ["Hello1.txt", "Hello2.txt", "Hello3.txt"]
text = "Hello"

for index, files in enumerate(filenames):
    file = open(f"files/exercises/iterate/Hello{index + 1}.txt", 'w')
    file.write(text)
    file.close()


# 5. from files a.txt, b.txt, c.txt create program that reads each text file and prints out
# content of each in the command line

filenames = ["a", "b", "c"]

for index, filename in enumerate(filenames):
    file = open(f"files/exercises/{filename}.txt", 'r')
    vypis = file.read()
    print(vypis)
    file.close()
