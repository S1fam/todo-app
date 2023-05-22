import glob

myfiles = glob.glob("files/*.txt")  # what files to filter out (all text files in specified folder)
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())
