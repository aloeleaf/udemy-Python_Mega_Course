
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            # r in front of "" stands for raw string, which means that the string should be treated as is
            read_file = open(r"file/todos.txt", "r")
            todos = read_file.readlines() # read all lines from the file and output them as a list
            read_file.close()
            todos.append(todo)
            write_file = open("file/todos.txt", "a")
            write_file.writelines(todos)
            write_file.close()
        case "show":
            read_file = open("file/todos.txt", "r")
            todos = read_file.readlines() # read all lines from the file and output them as a list
            read_file.close()
            for index, todo in enumerate(todos):
                row = f"{index + 1}-{todo}"
                print(row, end="")
        case "edit":
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case 'complete':
            # # remove by task
            # task = input("Enter the todo to complete: ")
            # todos.remove(task)
            # remove by index
            number = int(input("Enter the number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break

print("Bye!")