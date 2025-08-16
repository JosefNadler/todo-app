import functions as f
import time
import PySimpleGUI as sg


todos = f.get_todos()


print(f"It is : {time.strftime('%b %d, %Y %H:%M:%S')}")

while True:
    user_action = input("Type add show,delete, edit  or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos.append(todo)
    elif user_action.startswith('show'):
        for i, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{i + 1} : {todo}")
    elif user_action.startswith('edit'):
        try:
            n = int(user_action[5:])
            new_todo = input('Enter new todo : ') + '\n'
            todos[n - 1] = new_todo
        except:
            print('Command for editing is: edit <row> <todo>')
    elif user_action.startswith('delete'):
        try:
            n = int(user_action[6:])
            removed_todo = todos.pop((n - 1)).strip('\n')
            print(f"Todo {removed_todo} is removed from the list.")
        except:
            print('Command for delete is: delete <number>')
    elif user_action.startswith('save'):
        f.save_todos(todos)
    elif user_action.startswith('exit'):
        break
    else:
        print('Not a valid command')

print('Bye!')
