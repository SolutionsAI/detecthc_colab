import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Detect HOS Coomassie Sperm Solutions')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))



def detect():
    print("Hello from a function")
    st.image('foto.jpeg', caption='ejemplo de esperma por funcion')
    

b = False

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)




if st.button('Detectar'):
    b = !b
    
    
st.write(b)

if b:
    detect()
    
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

    
    
 
