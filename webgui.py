import streamlit as st
import todofunctions

todos = todofunctions.get_todos()

def add_todo():
    todo_n = st.session_state["new_todo"] + "\n"
    todos.append(todo_n)
    todofunctions.write_todos(todos)
## a webgui func add to-do to the file

st.title("My To-do List")
st.subheader("Add and edit daily to-dos.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todofunctions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new to-do.",
              on_change=add_todo, key="new_todo")
st.write("This web app is to keep track of the every-day housework.")

##window['clock'].update(value=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))