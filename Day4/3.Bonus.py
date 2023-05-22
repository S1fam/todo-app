filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

x = 0
for filename in filenames:
    new_filename = filename.replace('.', '-', 1)  # exchange . with - and only first instance of it
    filenames[x] = new_filename
    x += 1

print(filenames)


my_tuple = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
print(my_tuple)
