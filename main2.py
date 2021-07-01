import streamlit as st
from PIL import Image
import cv2 
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import time

from detect import *


k = hola()
#SIDEBAR stuff---------------------------------
#imagen
#st.sidebar.image('foto.jpeg')

#umbral
st.sidebar.title('Opciones de Configuración')
st.sidebar.write("Umbral de confianza para detección:")
e = st.sidebar.slider('Confianza HOS')  
f = st.sidebar.slider('Confianza Coomassie') 
#st.sidebar.write(e)
#----------------------------------------------

#titulo
st.title('Detector y clasificador HOS-Coomassie')

#descripcion
st.write("Seleccione el conjunto de imágenes a segmentar y clasificar")

#browse files
uploaded_files = st.file_uploader("Cargar Imágenes", accept_multiple_files=True)
i = 0
for uploaded_file in uploaded_files:
     
     i = i + 1
     
     cv2.imwrite("img"+str(i)+".jpeg",uploaded_file)
     #bytes_data = uploaded_file.read()
     #st.write("filename:", uploaded_file.name)
     #st.image(detect(uploaded_file))
     
     
st.write('Imagenes Cargadas: ',i)
st.write('')
st.write('Haga click en "Comenzar" para realizar el proceso de detección y clasificación de espermatozoides')

#boton detectar
st.button("Comenzar")

#grafico de resultdos
st.write('Resultados:')
y = [2,6,2,9,7,1,5,7,5,2,8] 
x = [1,2,3,4,5,6,7,8,9,10,11]


chart_data = pd.DataFrame({
     'index': ['H+C+', 'H+C-', 'H-C+', 'H-C-', 'NC'],
     'clases': [28,20,15,12,35]
}).set_index('index')

st.bar_chart(chart_data)   

#cv2.imwrite('')
st.write('')

#descargar imagenes clasificadas
st.write('Descargar imágenes procesadas:')
i = st.button("Descargar")
if i:
     st.write("IMAGEN ORIGINAL")
     h = cv2.imread("foto.jpeg")
     #st.image(h)
     
     st.write("IMAGEN GUARDADA")
     cv2.imwrite("recorte.jpeg",h)
     p = cv2.imread("recort.jpeg")
     #st.image(p)
     p1 = cv2.imread("img1.jpeg")
     st.image(p1)
     p2 = cv2.imread("img2.jpeg")
     st.image(p2)
     p3 = cv2.imread("img3.jpeg")
     st.image(p3)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
 
