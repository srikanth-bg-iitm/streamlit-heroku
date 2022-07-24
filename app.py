import streamlit as st

st.write("""
# Division of 2 numbers

""")
#Get Input

st.header('User Input Parameters')

numerator = st.number_input("Numerator",step=1)
denominator = st.number_input("Denominator",step=1)

st.subheader('Result')
if denominator == 0:
    st.write('Denominator cannot be zero!')
else:
    st.write(numerator / denominator)
