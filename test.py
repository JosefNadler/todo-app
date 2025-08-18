import functions
import FreeSimpleGUI as sg
import time


sg.theme('Black')  # Add a touch of color

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo ")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button(size=20, image_source='add.png', key='Add', mouseover_colors='LightBlue2', tooltip='Add todo')
list_box = sg.Listbox(values=functions.get_todos(), key='todo_list', enable_events=True, size = (45, 10))

edit_button = sg.Button("Edit", size=20, key='Edit')
delete_button = sg.Button(size=20, image_source='complete.png', key='Delete', mouseover_colors='LightBlue2', tooltip='Delete todo')
exit_button = sg.Button('Exit', key='Exit')

window = sg.Window('My todo App', 
                    layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, delete_button], [exit_button]], 
                    font=('Helvetica', 12))

while True:
    event, values = window.read(200)
    window['clock'].update(value=time.strftime('%b %d, %H:%M:%S'))

    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.save_todos(todos)
            window['todo_list'].update(values=todos)
        case 'Edit':
            try:
                selected_todo = values['todo_list'][0] if values['todo_list'] else None
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(selected_todo) if selected_todo else None
                todos[index] = new_todo
                functions.save_todos(todos)
                window['todo_list'].update(values=todos)
                print(selected_todo)
            except:
                sg.popup("Error: No todo item selected.", font=('Helvetica', 20))
        case 'Delete':
            try:
                selected_todo = values['todo_list'][0] if values['todo_list'] else None
                todos = functions.get_todos()
                if selected_todo in todos:
                    todos.remove(selected_todo)
                    functions.save_todos(todos)
                    window['todo_list'].update(values=todos)
                    window['todo'].update(value='')
            except:
                sg.popup("Error: No todo item selected.", font=('Helvetica', 20))
        case 'todo_list':
            selected_todo = values['todo_list'][0] if values['todo_list'] else None
            if selected_todo:
                window['todo'].update(value=selected_todo)  
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
#        case _:        case _:
#            print("Unknown event")   
#            print("Unknown event")        

print("Bye")
window.close()  


