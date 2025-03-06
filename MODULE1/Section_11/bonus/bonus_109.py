
def get_average():
    with open("data.txt", 'r') as file:
        data = file.readlines()
    
    values = data[1:] 
    values = [float(value) for value in values]
    average = sum(values) / len(values)
    return average

avarage = get_average()
print(avarage)