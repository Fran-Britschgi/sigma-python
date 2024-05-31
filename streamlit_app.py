import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import traceback
import code_editor
from snowflake.snowpark import Session

st.set_page_config(layout="wide")

st.title("Python Code Executor")
account = st.text_input("Snowflake Account")

connection_parameters = {
    "account": account,
    "user": "francis",
    "password": st.secrets["password"],
    "role": "sigma_se",
    "warehouse": "PAPERCRANE",
    "database": "SE_DEMO_DB",
    "schema": "SNOWPARK_UDF",
}

session = Session.builder.configs(connection_parameters).create()


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
response_dict = code_editor.code_editor(code = "my_df = session.table('DATABASE.SCHEMA.TABLE').to_pandas \nnew_df = my_df *2 \nsession.create_dataframe(new_df).write.mode('overwrite').save_as_table('DATABASE.SCHEMA.NEW_TABLE')", buttons=editor_btns)
code_input = response_dict['text']

# Display Results
if len(response_dict['id']) != 0 and ( response_dict['type'] == "selection" or response_dict['type'] == "submit" ):
    try:
        # Redirect output to the Streamlit interface
        exec_globals = {'session': session}
        exec(code_input, exec_globals)
        st.success("Code executed successfully!")
    except Exception as e:
        st.code(code_input,language='python')
        st.error(f"An error occurred:\n{traceback.format_exc()}")
