filepath = 'todos.txt'

def get_todos(file=filepath) -> list:
    try:
        with open(file, 'r') as f:
            local_todos = f.readlines()
        return local_todos
    except:
        print('Sorry file not found ...')
        return []


def save_todos(todo_list, file=filepath):
    with open(file, 'w') as f:
        f.writelines(todo_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

