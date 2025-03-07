def strength(password):
    pwd_strength = {}
    if len(password) >= 8 :
        pwd_strength["lenght"] = True
    else:
        pwd_strength["lenght"] = False
    
    for char in password:        
        if char.isupper():
            pwd_strength["uppercase"] = True
            break
        else:
            pwd_strength["uppercase"] = False
    
    for char in password:
        if char.isdigit():
            pwd_strength["digit"] = True
            break
        else:
            pwd_strength["digit"] = False
            

    print(pwd_strength)

    if all(pwd_strength.values()):
        return "Strong Password"
    else:
        return "Weak Password"


my_password = "9wlVKwq1"
print(strength(my_password))

