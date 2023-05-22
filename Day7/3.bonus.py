
filenames = ["1.doc", "2.report", "1.presentation"]  # change into 1-doc.txt ...

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)
