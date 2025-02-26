todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, todo in enumerate(todos):
                # f-string to format the output
                # index + 1 to start the numbering from 1
                row = f"{index + 1}-{todo}"
                print(row)
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