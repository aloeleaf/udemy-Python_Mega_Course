new_member = input("Add a new member: ")
file = open("members.txt", "a")
file.write(new_member + "\n")
file.close()


## Solution
# member = input("Add a new member: ")

# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()

# existing_members.append(member + "\n")

# file = open("members.txt", 'w')
# file.writelines(existing_members)
# file.close()