countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for country in countries:
    file = open(f"{country}.txt", "w")
    file.write(f"{country}")
    file.close()
    