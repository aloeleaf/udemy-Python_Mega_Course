todos = []

# while loop
while True:
    user_action = input("Type add or show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            break


print("Goodbye!")