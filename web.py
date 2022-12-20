import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['-new_todo-'] + '\n'
    todos.append(todo)
    functions.save_todos(todo_list=todos)

st.title('My todo App')
st.subheader('This is my todo app.')
st.write('this app will increase your productivity.')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a new todo', placeholder="Add new todo .....", on_change=add_todo, key='-new_todo-')

st.session_state
print('Hello again ..')