def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_local):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        # if "add" == user_action[:3]:

        todo = user_action[4:] + '\n'

        todos = get_todos("todos.txt")
        todos.append(todo)

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            row = f"{index + 1}-{todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos("todos.txt", todos)

            message = f"Todo number {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no todo with that number.")
            continue
        except SyntaxError:
            print("There is a syntax error.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")


print("Bye!")
