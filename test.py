import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo ")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todo_list', enable_events=True, size = (45, 10))

edit_button = sg.Button('Edit')


window = sg.Window('My todo App', 
                    layout=[[label], [input_box, add_button], [list_box, edit_button]], 
                    font=('Helvetica', 12))

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break

    print("Hello from the GUI ", event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.save_todos(todos)
            window['todo_list'].update(values=todos)
        case 'Edit':
            selected_todo = values['todo_list'][0] if values['todo_list'] else None
            new_todo = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(selected_todo) if selected_todo else None
            todos[index] = new_todo
            functions.save_todos(todos)
            window['todo_list'].update(values=todos)
            print(selected_todo)
        case 'todo_list':
            selected_todo = values['todo_list'][0] if values['todo_list'] else None
            if selected_todo:
                window['todo'].update(value=selected_todo)  
        case _:
            print("Unknown event")

window.close()


