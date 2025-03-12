import FreeSimpleGUI as fsg
import converters

label_feet = fsg.Text("Enter feet")
input_feet_box = fsg.InputText(tooltip="Enter feet", key="feet")

label_inches = fsg.Text("Enter inches")
input_inches_box = fsg.InputText(tooltip="Enter inches", key="inches") 

convert_button = fsg.Button("Convert", tooltip="Convert to cm")
output_label = fsg.Text(key="output")

window = fsg.Window(title="Convertor", 
                    layout=[[label_feet, input_feet_box],
                    [label_inches, input_inches_box],
                    [convert_button, output_label]],  
                    font=('Helvetica', 18)
                    )

while True:
    event, values = window.read()
    if event == fsg.WIN_CLOSED:
        break
    feet = float(values['feet'])
    inches = float(values['inches'])

    result = converters.convert(feet, inches)
    output_label.update(value=f"{result:.2f} m", text_color="white")

  


window.close()