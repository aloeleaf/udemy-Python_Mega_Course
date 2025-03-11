import FreeSimpleGUI as fsg

feet_lable = fsg.Text("Enter feet:")
feet_input = fsg.Input()
inch_lable = fsg.Text("Enter inches:")
inch_input = fsg.Input()
button = fsg.Button("Convert")

window = fsg.Window("Convertor",
                    layout=[[feet_lable, feet_input],
                            [inch_lable, inch_input],
                            [button]])

window.read()
window.close()
