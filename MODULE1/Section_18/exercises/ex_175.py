import FreeSimpleGUI as fsg
import converts

fsg.theme('DarkAmber')

label_feet = fsg.Text('Enter feet:')
input_feet = fsg.InputText(tooltip='Enter feet', key='feet')
label_inches = fsg.Text('Enter inches:')
input_inches = fsg.InputText(tooltip='Enter inches', key='inches') 

convert_button = fsg.Button('Convert', tooltip='Convert to inches', key='convert')
exit_button = fsg.Button('Exit', tooltip='Exit the program', key='exit')
info_text = fsg.Text('')


window = fsg.Window('Feet to Inches Converter',
                    [[label_feet, input_feet],
                     [label_inches, input_inches],
                     [convert_button, exit_button, info_text]])

while True:
    key, value = window.read()
    print(key, value)
    match key:
        case 'exit':
            break
        case fsg.WIN_CLOSED:
            break
        case 'convert':
            try:
                feet = float(value['feet'])
                inches = float(value['inches'])
                result = converts.convert(feet, inches)
                info_text.update(f'{result} m')
            except ValueError:
                fsg.popup_error('Please enter a valid number')                


window.close()  

                    