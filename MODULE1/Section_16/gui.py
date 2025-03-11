from modules import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add", tooltip="Add todo")


window = fsg.Window(title="My To-Do App",
                    layout=[[label], [input_box, add_button]]
                    )

window.read()
window.close()
