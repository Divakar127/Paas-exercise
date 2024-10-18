import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# Subtitle
st.subheader('Welcome to this simple app')

# Input field for user text
user_input = st.text_input('Enter your name:')

# Display the entered name
if user_input:
    st.write(f'Hello, {user_input}!')

# Number slider
number = st.slider('Pick a number', 0, 100, 50)

# Display the number
st.write(f'You selected: {number}')

# Button action
if st.button('Click me!'):
    st.write('Button clicked!')

# Sidebar example
st.sidebar.title('Sidebar')
st.sidebar.write('This is a sidebar example.')
