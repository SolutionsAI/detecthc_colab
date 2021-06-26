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
#st.sidebar.image('foto.jpeg')

#umbral
st.sidebar.title('Opciones de configuración')
st.sidebar.write("Umbral de confianza para detección:")
e = st.sidebar.slider('conf')  
#st.sidebar.write(e)
#----------------------------------------------

#titulo
st.title('Detector y clasificador HOS-Coomassie')

#descripcion
st.write("Seleccione el conjunto de imágenes a segmentar y clasificar")

#browse files
uploaded_files = st.file_uploader("Cargar Imágenes", accept_multiple_files=True)
cont = 0
for uploaded_file in uploaded_files:
     
     cont = cont + inc
     #bytes_data = uploaded_file.read()
     #st.write("filename:", uploaded_file.name)
     #st.image(detect(uploaded_file))
st.write('Imagenes Cargadas: ',cont)
st.write('')
st.write('A continuación haga click en "Comenzar" para realizar el proceso de detección y clasificación de espermatozoides')

#boton detectar
st.button("Comenzar")

#grafico de resultdos
st.write('Resultados:')
y = [2,6,2,9,7,1,5,7,5,2,8] 
x = [1,2,3,4,5,6,7,8,9,10,11]


chart_data = pd.DataFrame({
     'index': ['H+', 'H-', 'C+', 'C-', 'NC'],
     'clases': [70,50,100,78,64]
}).set_index('index')

st.bar_chart(chart_data)   

st.write('')

#descargar imagenes clasificadas
st.write('Descargar imágenes procesadas:')
st.button("Descargar")
    
    
 
