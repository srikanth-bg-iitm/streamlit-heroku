import streamlit as st

st.write("""
# Division of 2 numbers

""")
#Get Input

st.header('User Input Parameters')

numerator = st.number_input("Numerator")
denominator = st.number_input("Denominator")

st.subheader('Result')
if denominator == 0:
    st.write('Denominator cannot be zero!')
else:
    st.write(numerator / denominator)
