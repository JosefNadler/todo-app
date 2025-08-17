import FreeSimpleGUI as sg
import converters

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key='-feet-')
label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='-inches-')

convert_button = sg.Button('Convert', key='-convert-')

window = sg.Window('Converter', layout=[[label1, input1], [label2, input2], [convert_button, sg.Text("", key='-result-')]])   

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == '-convert-':
        feet = float(values['-feet-'])
        inches = float(values['-inches-'])
        meters = converters.convert(feet, inches)
        window['-result-'].update(f"{meters} meters")

window.close()
