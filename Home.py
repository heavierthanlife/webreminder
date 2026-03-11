import os
import requests
from dotenv import load_dotenv

load_dotenv()

class CloudBaseClient:
    def __init__(self):
        self.env_id = os.getenv("CLOUDBASE_ENV_ID")
        self.access_token = os.getenv("CLOUDBASE_ACCESS_TOKEN")
        self.base_url = f"https://{self.env_id}.api.tcloudbasegateway.com"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

    def request(self, method, path, **kwargs):
        """
        统一的HTTP请求方法

        Args:
            method: 请求方法 (GET, POST, PUT, PATCH, DELETE)
            path: API路径 (如 /v1/rdb/rest/table_name)
            **kwargs: 其他请求参数 (json, params, headers等)

        Returns:
            响应数据或None
        """
        url = f"{self.base_url}{path}"
        headers = self.headers.copy()

        # 允许自定义headers
        if "headers" in kwargs:
            headers.update(kwargs.pop("headers"))

        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()

            # 如果响应为空，返回True表示成功
            if not response.content:
                return True

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return None

cloudbase = CloudBaseClient()


import streamlit as st
import todofunctions

todos = todofunctions.get_todos()

st.set_page_config(page_title="My To-do List", layout="wide")

def add_todo():
    todo_n = st.session_state["new_todo"] + "\n"
    todos.append(todo_n)
    todofunctions.write_todos(todos)
## a webgui func add to-do to the file

st.title("My To-do List")
##st.subheader("Add and edit daily to-dos.")
st.text_input(label="", placeholder="Add a new to-do.",
              on_change=add_todo, key="new_todo")
st.write("This web app is to keep track of the every-day <b>housework</b>:",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todofunctions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()