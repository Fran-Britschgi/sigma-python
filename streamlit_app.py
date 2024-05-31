import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import traceback
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

code_input = st.text_area("Python Code", height=200)

if st.button("Execute"):
    try:
        # Redirect output to the Streamlit interface
        exec_globals = {}
        exec(code_input, exec_globals)
        st.success("Code executed successfully!")
        st.success(f"{traceback.print_last()}")
    except Exception as e:
        st.error(f"An error occurred:\n{traceback.format_exc()}")
