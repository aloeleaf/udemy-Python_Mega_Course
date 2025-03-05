password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["lenght"] = True
else:
    result["lenght"] = False


digit = False
for char in password:
    if char.isdigit():
        digit = True


result["digit"] = digit

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True


result["uppercase"] = uppercase
print(result)
if all(result.values()):
    print("Password is strong")
else:
    print("Password is weak")
