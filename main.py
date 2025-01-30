import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Simple Data(csv) Analysis")

file = st.file_uploader("Choose your csv file", type=["csv", 'tsv'])

if file is not None:
    st.write("File uploaded successfully...🎉")
    
    df = pd.read_csv(file)
    
    st.subheader("Data Preview:")
    st.write(df.head())
    
    st.subheader("summary of the data:")
    st.write(df.describe())