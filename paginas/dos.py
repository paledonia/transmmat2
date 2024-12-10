import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 
from func_vec import *



st.title("Grafica de 2 vectores en el plano")

c1,c2 = st.columns(2) 


with c1: 
    st.subheader("Vector 1")  
    a = st.number_input("Coordenada X : ", min_value = -14, max_value=15, value = 3)  
    b = st.number_input("Coordenada Y : ", min_value = -14, max_value=15, value = 2)  
with c2: 
    st.subheader("Vector 2")  
    c = st.number_input("Coordena X : ", min_value = -14, max_value=15, value = 4)  
    d = st.number_input("Coordena Y : ", min_value = -14, max_value=15, value = 1) 

u = [a,b] 
v = [c,d] 
c_3 = st.number_input("Coordena X : ", min_value = 90, max_value=100, value = 95)

graf_base (u, v)




#____________________________________________________________________________________________________________________________________________________________________
st.divider()  

st.title("Escalar un vector en el plano") 

c_1,c_2 = st.columns(2) 


with c_1: 
    st.subheader("Vector")  
    r = st.number_input("Coordenada X : ", min_value = -14, max_value=15, value = 1)  
    t = st.number_input("Coordenada Y : ", min_value = -14, max_value=15, value = 5)   
    u = [r,t] 
with c_2: 
    st.subheader("Numero que usaremos como escalar")  
    c = st.number_input("Coordena X : ", min_value = -14, max_value=15, value = 6)  

graf_escvector (u,c) 
st.markdown(f"El vector *[{r} , {t}]* esta escaldo un factor de {c} y el resultado es: *[{r*c} , {t*c}]*")
