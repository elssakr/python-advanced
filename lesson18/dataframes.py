import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24,27,22,37,35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

st.dataframe(data)