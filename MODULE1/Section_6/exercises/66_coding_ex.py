files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    read_file = open(f"{file}", "r")
    print(read_file.read())
    read_file.close()

## solution
# filenames = ['a.txt', 'b.txt', 'c.txt']

# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)    