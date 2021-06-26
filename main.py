import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import time


#SIDEBAR stuff---------------------------------
#imagen
st.sidebar.image('foto.jpeg', caption='Detector y clasificador de espermatozoides')

#umbral
st.sidebar.write("umbral de confianza")
e = st.sidebar.slider('x')  
st.write(e)
#----------------------------------------------

#titulo
st.title('Detect HOS Coomassie Sperm Solutions')

#descripcion
st.write("Seleccione el conjunto de imagenes a segmentar y clasificar")

#browse files
uploaded_files = st.file_uploader("Cargar Imágenes", accept_multiple_files=True)
cont = 0
for uploaded_file in uploaded_files:
     
     cont = cont + inc
     #bytes_data = uploaded_file.read()
     #st.write("filename:", uploaded_file.name)
     #st.image(detect(uploaded_file))
st.write('Imagenes Cargadas: ',cont)


#grafico de resultdos
y = [2,6,2,9,7,1,5,7,5,2,8] 
x = [1,2,3,4,5,6,7,8,9,10,11]

chart_data = pd.DataFrame(
     np.random.randn(5, 1),
     columns=['H+', 'H-', 'C+', 'C-', 'NC'])
st.bar_chart(chart_data)    
    
    
 
