from modules import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add", tooltip="Add todo")
list_box = fsg.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 10])
edit_button = fsg.Button("Edit", tooltip="Edit todo")

complete_button = fsg.Button("Complete", tooltip="Complete todo")


window = fsg.Window(title="My To-Do App",
                    layout=[[label],[input_box, add_button], [list_box, edit_button, complete_button]],
                    font=('Helvetica', 16)
                    )


while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)  
            window["todos"].update(values=todos)
        case 'todos':
            window["todo"].update(value=values['todos'][0])         
        case fsg.WIN_CLOSED:
            #exit() stop all program
            break

window.close()
