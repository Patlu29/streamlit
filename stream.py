import streamlit as st

st.title("My first app")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)