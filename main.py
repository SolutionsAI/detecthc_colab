import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt

st.title('Detect HOS Coomassie Sperm Solutions')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))



def detect():
    print("Hello from a function")
    st.sidebar.image('foto.jpeg', caption='ejemplo de esperma por funcion')
    

b = False

e = st.sidebar.slider('x')  # 👈 this is a widget
st.write(e, 'squared is', e * e)




if st.sidebar.button('Detectar'):
    b = not b
    
    
st.write(b)

if b:
    detect()
    
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

y = [2,6,2,9,7,1,5,7,5,2,8] 
x = [1,2,3,4,5,6,7,8,9,10,11]

plt.plot(x,y)
st.write(plt.show())

    
    
 
