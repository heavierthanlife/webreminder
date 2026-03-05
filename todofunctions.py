FILEPATH = "app.reminder.txt"
import streamlit as st

def get_todos(filepath=FILEPATH):
    with open(FILEPATH, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
## a global read from the file
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as write_file:
        write_file.writelines(todos_arg)
## a global write function to the file