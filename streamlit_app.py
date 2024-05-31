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

response_dict = code_editor.code_editor(code = "print('hi')")

#code_input = st.text_area("Python Code", height=200, value="print('hello')")
if st.button("Execute"):
    try:
        # Redirect output to the Streamlit interface
        exec_globals = {'session': session}
        exec(response_dict['text'], exec_globals)
        st.code(response_dict['text'], language=response_dict['lang'])
        st.success("Code executed successfully!")
    except Exception as e:
        st.code(response_dict['text'],language='python')
        st.error(f"An error occurred:\n{traceback.format_exc()}")
