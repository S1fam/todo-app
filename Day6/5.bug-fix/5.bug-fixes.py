
file = open("data.txt", 'w')

file.writelines("100.12\n")  # missing \n
file.writelines("111.23\n")  # missing \n
file.close()


file = open("data.txt", 'w')  # r instead of w
file.write("100.12")
file.close()
