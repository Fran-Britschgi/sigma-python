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

response_dict = code_editor.code_editor("print('hi')")

code_input = st.text_area("Python Code", height=200, value="my_df = session.table('DATABSE.SCHEMA.TABLE').to_pandas' \nnew_df = my_df *2 \nsession.create_dataframe(new_df).write.mode('overwrite').save_as_table('DATABASE.SCHEMA.NEW_TABLE')")

if st.button("Execute"):
    try:
        # Redirect output to the Streamlit interface
        exec_globals = {'session': session}
        exec(code_input, exec_globals)
        st.code(response_dict,language='python')
        st.success("Code executed successfully!")
    except Exception as e:
        st.code(code_input,language='python')
        st.error(f"An error occurred:\n{traceback.format_exc()}")
