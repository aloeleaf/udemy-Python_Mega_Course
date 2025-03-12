import FreeSimpleGUI as fsg

label1 = fsg.Text("Slect file to commpress: ")
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse("Choose", key="files")



label2 = fsg.Text("Slect destination folder: ")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Compress")

window = fsg.Window("Compress File", 
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button]]
                    )


while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]


window.close()