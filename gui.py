import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button("Add")

win = sg.Window('My todo App', layout=[[label], [input_box, add_button]])
win.read()
win.close()
