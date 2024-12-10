import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 
from func_vec import *



st. title ("Vectores ")   
st.divider() 

st.subheader("*Pilar Fundamental del Algebra Lineal*")

st.markdown (""" 

El elemento mas importante en el algebra lineal es el **vector**, asi que en esta seccion 
repasaremos cuales son sus elementos, que significado tienen y sus operaciones basicas.  


""")

c1, c2 = st.columns (2)

with c1: 
    st.markdown (""" 
    Dependiendo del area del conocimiento existen diferentes formas de denominar a un elemento como vector. 
    Si tenemos un flecha representada en cualquier espacio, estamos hablando de un punto vista fisico. Se define 
    como un elemento el cual tiene una direccion y sentido descritos. Si estos dos elementos no cambian, podremos
    colocar el vector en cualquier lugar del espacio y seguira siendo el mismo.
    
    """) 

with c2:  
    st.image("https://www.3blue1brown.com/content/lessons/2016/vectors/figures/introduction/2dAnd3DVectors.png") 
    st.image ("https://mathslinks.net/images/jcogs_img/cache/5405_-_28de80_-_b34be6c0c73d368586aca2982aa7ac453962fde9.webp")

st.markdown("""
> *La introdccuin de los numeros como :rainbow[coordenadas] es un acto de violencia*
>
> **- Hermann Weyl**
""")