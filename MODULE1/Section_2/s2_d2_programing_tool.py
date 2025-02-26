# dir(str)  # list all the methods of the string class
# dir("string")  # list all the methods of the string class
# help(str)  # get help on the string class
# help("string".capitalize)  # get help on the string class
# dir(builtins)  # list all the built-in functions

datatype = input("Enter the data type: ")
function_lists = dir(datatype)
print(function_lists)

for function in function_lists:
     if not function.startswith("__"):
        print(function)
      #  print(help(datatype + "." + function))  