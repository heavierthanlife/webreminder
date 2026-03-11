import os

import streamlit
from flask import Flask

app = Flask(__name__)


@app.route('Home.py')
def home():
    return streamlit.html("Home page")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
