filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"{filename}", "w")
    file.write("Hello")
    file.close()
