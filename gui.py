import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(key='-todo-', tooltip='Enter todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='-todos-', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete", key='-delete-')
exit_button = sg.Button('Exit', key = '-exit-')
frame = [[label], [input_box, add_button], [list_box, edit_button, delete_button], [exit_button]]

win = sg.Window('My todo App', layout=frame, font=('Helvetica', 20))

while True:
    event, values = win.read()
    print(event, values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['-todo-'] + '\n'
            todos.append(new_todo)
            functions.save_todos(todos)
            win['-todos-'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['-todos-'][0]
            new_todo = values['-todo-']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.save_todos(todos)
            win['-todos-'].update(values=todos)
        case '-todos-':
            win['-todo-'].update(value=values['-todos-'][0])
        case '-delete-':
            todo_to_delete = values['-todos-'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_delete)
            functions.save_todos(todo_list=todos)
            win['-todos-'].update(values=todos)
            win['-todo-'].update(value='')
            print(f"The element has been deleted !!")
        case '-exit-':
            print('First Exit')
            break
        case sg.WIN_CLOSED:
            print('Second Exit')
            break

print('Bye')
win.close()
