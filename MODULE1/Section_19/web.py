import streamlit as st
from modules import functions

todos = functions.get_todos()
st.set_page_config(layout='wide')


def add_todo():
    # st.session_state output is a dictionary data and "new_todo" is the key
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    # st.rerun(scope='app')


# create fix html elements in streamlit
st.title('My Todo App')
st.subheader('This is my todo app.')
st.write(
    "This app is to increase your <b>productivity</b>.",
    unsafe_allow_html=True)

st.text_input(
    label="New todo:",
    placeholder="Add new todo",
    on_change=add_todo,
    key='new_todo',
    label_visibility='hidden')

# create dynamic html elements in streamlit
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # print(index, "-", todo)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
