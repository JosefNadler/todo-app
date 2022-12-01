import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(key='-todo-', tooltip='Enter todo')
add_button = sg.Button("Add")

win = sg.Window('My todo App', layout=[[label], [input_box, add_button]], font=('Helvetica', 20))

while True:
    event, values = win.read()
    print(event, values)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    else:
        match event:
            case 'Add':
                todos = functions.get_todos()
                new_todo = values['-todo-'] + '\n'
                todos.append(new_todo)
                functions.save_todos(todos)


win.close()
