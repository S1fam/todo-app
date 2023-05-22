
contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# a = [1, 2, 3]
# b = [10, 20, 30]
# x = zip(a, b)  --> zip grabs content as first item of created tuple
# print(list(x)) - vypise [(1, 10), (2, 20), (3, 30)] enumarate would use numbers 1,2...

for content, filename in zip(contents, filenames):
    file = open(f"files/bonus/{filename}", 'w')  # ../ goes up one level, then write the path
    file.write(content)  # (up) we open a path and varying filename, inside we write varying content

file.close()

# a = "I am a string " \
#     "on my " \
#     "own"
# print(a) --> prints out:  I am a string on my own
