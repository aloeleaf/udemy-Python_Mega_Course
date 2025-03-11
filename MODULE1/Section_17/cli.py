from modules import functions
import time

text = """
Principles of productivity:
Managing your inflow.
Systemizing everything that repeats.
""" 

now = time.strftime("%Y-%m-%d %H:%M:%S")
print(f'It is : {now}')



while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        # if "add" == user_action[:3]:

        todo = user_action[4:] + '\n'

        todos = functions.get_todos("files/todos.txt")
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos("files/todos.txt")

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            row = f"{index + 1}-{todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos("files/todos.txt")

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos("files/todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

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
