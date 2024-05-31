import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import traceback
import code_editor
from snowflake.snowpark import Session

connection_parameters = {
    "account": "cxa94702",
    "user": "francis",
    "password": st.secrets["password"],
    "role": "sigma_se",
    "warehouse": "PAPERCRANE",
    "database": "SE_DEMO_DB",
    "schema": "SNOWPARK_UDF",
}

session = Session.builder.configs(connection_parameters).create()

st.title("Python Code Executor")

st.write("Enter your Python code below:")
editor_btns = [{
    "name": "Run",
    "feather": "Play",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"bottom": "0.44rem", "right": "0.4rem"}
  }]
response_dict = code_editor.code_editor(code = "print('hi')", buttons=editor_btns)

# show response dict
if len(response_dict['id']) != 0 and ( response_dict['type'] == "selection" or response_dict['type'] == "submit" ):
    # Capture the text part
    code_text = response_dict['text']
    st.code(code_text, language='python') #Captured the code parameter.
