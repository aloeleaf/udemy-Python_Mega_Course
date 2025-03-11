import FreeSimpleGUI as fsg

label1 = fsg.Text("Slect file to commpress: ")
input1 = fsg.Input()
choose_button1 = fsg.Button("Choose")



label2 = fsg.Text("Slect file to commpress: ")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose")

compress_button = fsg.Button("Compress")

window = fsg.Window("Compress File", 
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button]]
                    )


window.read()
window.close()