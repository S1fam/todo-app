with open("files/doc.txt", "r") as file:  # context manager goes to mode=r (read) automatically, no need to specify
    print("hello")
    content = file.read()

print(content)  # this way we can print more times, if we did print(file.read()) we could only print out content once
print(content)  # this is because of position of cursor in file that moves to the end of file
