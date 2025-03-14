from modules import functions
import FreeSimpleGUI as fsg
import time

fsg.theme('Black')

clock  = fsg.Text('', key='clock', font=('Helvetica', 18))
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add", tooltip="Add todo")
list_box = fsg.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 10])
edit_button = fsg.Button("Edit", tooltip="Edit todo")

complete_button = fsg.Button("Complete", tooltip="Complete todo")
exit_button = fsg.Button("Exit", tooltip="Exit todo")


window = fsg.Window(title="My To-Do App",
                    layout=[[clock],
                            [label], 
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 18)
                    )


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime('%H:%M:%S'))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            if not new_todo.isspace():
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            else:
                fsg.popup("Please enter a todo", font=('Helvetica', 18))
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first", font=('Helvetica', 18))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                fsg.popup("Please select an item first", font=('Helvetica', 18))
        case "Exit":
            break
        case 'todos':
            window["todo"].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            # exit() stop all program
            break

window.close()
