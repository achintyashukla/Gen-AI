import streamlit as st

# Task 1: Basic Streamlit App

# 1. Displays a title
st.title("Welcome to Streamlit!")

# 2. Shows a text input box for entering your name
name = st.text_input("Enter your name:")

# 3. When user clicks a button, display "Hello, [name]!"
if st.button("Greet Me"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello, !")
