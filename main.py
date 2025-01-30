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
    
    st.subheader("Filter data:")
    columns = df.columns.tolist()
    selected_column = st.selectbox("select column:", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("select value:", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Data visualization:")
    x_axis = st.selectbox("select x-axis for plot:", columns)
    y_axis = st.selectbox("select y-axis for plot:", columns)
    
    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_axis)[y_axis])

else:
    st.write("Waiting for upload a file...")