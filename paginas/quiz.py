import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 
from func_vec import * 

st.title("Quiz: *Prueba tus conociemientos*") 
st.divider() 

st.subheader("1. ¿Que es un vector?")  

st.markdown("""
 - a. un escalar 
 - b. Un lista de numeros 
 - c. Una flecha 
 - d. Todas las anteriores
""")  

opc = st.selectbox ("Elije tu opción: ", [" ","un escalar ","Un lista de numeros", "Una flecha", "Todas las anteriores"]) 

if opc == "un escalar": 
    st.markdown ("Respuesta incorrecta") 
elif opc == "Un lista de numeros": 
    st.markdown ("Respuesta incorrecta") 
elif opc == "Una flecha": 
    st.markdown ("Respuesta incorrecta") 
elif opc == "Todas las anteriores": 
    st.markdown ("Respuesta Correcta") 

st.subheader("2. Que operaciones estan definidas para los vectores?")  

st.markdown("""
 - a. Suma y multiplicacion por un escalar 
 - b. Division de vectores
 - c. Todas las anteriores 
 - d. Ninguna

""")  

opc2 = st.selectbox ("Elije tu opción: ", [" ","Suma y multiplicacion por un escalar ","Division de vectores", "todas las anteriores", "Ninguna"]) 

if opc2 == "Suma y multiplicacion por un escalar": 
    st.markdown ("Respuesta correcta") 
elif opc2 == "Division de vectores": 
    st.markdown ("Respuesta incorrecta") 
elif opc2 == "todas las anteriores": 
    st.markdown ("Respuesta incorrecta") 
elif opc2 == "Ninguna": 
    st.markdown ("Respuesta incorrecta")  

st.subheader("3. Que representa una transformacion lineal?")  

st.markdown("""
 - a. Multiplicar las componentes del vector por un escalar 
 - b. El moviento de un vector o subespacio 
 - c. Las bases de un sistema de coordenadas

""")  

opc3 = st.selectbox ("Elije tu opción: ", [" ","Multiplicar las componentes del vector por un escalar ","El moviento de un vector o subespacio", "Las bases de un sistema de coordenadas",]) 

if opc3 == "Multiplicar las componentes del vector por un escalar": 
    st.markdown ("Respuesta correcta") 
elif opc3 == "El moviento de un vector o subespacio": 
    st.markdown ("Respuesta correcta") 
elif opc3 == "Las bases de un sistema de coordenadas": 
    st.markdown ("Respuesta incorrecta")  

st.subheader("4. Que representa en en plano **i** y **j?**")  

st.markdown("""
 - a. Vectores linealmente depentientes
 - b. Una tranformacion lineal
 - c. Las bases del sistema de coordenadas XY

""")  

opc4 = st.selectbox ("Elije tu opción: ", [" ","Vectores linealmente depentientes","Una tranformacion lineal", "Las bases del sistema de coordenadas XY",]) 

if opc4 == "Vectores linealmente depentientes": 
    st.markdown ("Respuesta incorrecta") 
elif opc4 == "Una tranformacion lineal": 
    st.markdown ("Respuesta incorrecta") 
elif opc4 == "Las bases del sistema de coordenadas XY": 
    st.markdown ("Respuesta correcta")  

st.subheader("5. Podemos utilizar cualquier base **u** y **v** para describir la base de un sistemas de coordenadas que cubra el plano?")  

st.markdown("""
 - a. Si, cualesquiera **v** y **u** vectores
 - b. SI, siempre y cuando **v** no sea combinacion lineal de **u**
 - c. No, es imposible generar el plano con cualquier base que no sea **i** y **j**

""")  

opc4 = st.selectbox ("Elije tu opción: ", [" ","Si, cualesquiera **v** y **u** vectores","SI, siempre y cuando **v** no sea combinacion lineal de **u**", "No, es imposible generar el plano con cualquier base que no sea **i** y **j**",]) 

if opc4 == "Si, cualesquiera **v** y **u** vectores": 
    st.markdown ("Respuesta incorrecta") 
elif opc4 == "SI, siempre y cuando **v** no sea combinacion lineal de **u**": 
    st.markdown ("Respuesta correcta") 
elif opc4 == "No, es imposible generar el plano con cualquier base que no sea **i** y **j**": 
    st.markdown ("Respuesta incorrecta") 


