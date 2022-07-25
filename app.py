import streamlit as st

st.title('Check Greatest of the Three')
a = st.number_input('Enter First number')
b = st.number_input('Enter Second number')
c = st.number_input('Enter Third number')
l = [a,b,c]

st.header('The Greatest number is: '+str(max(l)))
st.header('TDS week 8 Graded Assignment')
st.header('Submitted by : 21f1002085@student.onlinedegree.iitm.ac.in')
