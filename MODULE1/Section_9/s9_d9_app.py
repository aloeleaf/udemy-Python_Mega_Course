# use with context manager to open file
# example: with open("todos.txt", "r") as file

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if "add" in user_action:
        todo = user_action[4:]

        with open(r"todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    if "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            row = f"{index + 1}-{todo}"
            print(row)

    if "edit" in user_action:
        number = int(input("Enter the number of the todo to edit: "))
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    if "complete" in user_action:
        number = int(input("Enter the number of the todo to complete: "))
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo number {todo_to_remove} was removed from the list."
        print(message)

    if "exit" in user_action:
        break

print("Bye!")
