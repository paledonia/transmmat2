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

st.markdown (""" 
    Dependiendo del area del conocimiento existen diferentes formas de denominar a un elemento como vector.  

""")    

c1, c2 = st.columns (2)

with c1: 
    st.markdown("""
    <p>Si tenemos una flecha representada en cualquier espacio (<span style="font-size: 1em;">R<sup>2</sup></span> o 
    <span style="font-size: 1em;">R<sup>3</sup></span>), estamos hablando de un punto de vista físico. Se define
    como un elemento el cual tiene una dirección y sentido descritos. Si estos dos elementos no cambian, podremos
    colocar el vector en cualquier lugar del espacio y seguirá siendo el mismo.</p>
""", unsafe_allow_html=True) 

with c2:  
    st.image("https://www.3blue1brown.com/content/lessons/2016/vectors/figures/introduction/2dAnd3DVectors.png")  

c3, c4 = st.columns (2)

with c3: 
    st.markdown("""
    Desde el punto de vista de un programador los vectores son arreglos o listas ordenadas de numeros. 

    **Ej:** *[1,2,4,5]* una lista de 4 elementos numericos. El orden de los 
    elementos se lee de izquierda a derecha y su dimension esta dada por la cantidad de elementos que existan en la lista. Este vector es de dimension 4. 
    El orden de un arreglo es muy importante ya que si cambia no sera el mismo. 
    
    *[1,2,4,5]* es diferente a *[2,1,4,5]* ya que **1** y **2** cambiaron sus posicones, por lo 
    tanto son arreglos diferentes. Vector, en este caso, es una forma sofisticada de decir arreglo o lista.

""")  

with c4:   
    st.image ("https://www.3blue1brown.com/content/lessons/2016/vectors/figures/vector-operations/VectorAdditionPrep.svg")
    st.image ("https://mathslinks.net/images/jcogs_img/cache/5405_-_28de80_-_b34be6c0c73d368586aca2982aa7ac453962fde9.webp")     


st.subheader("*Operaciones Basicas: suma y multiplicacion por un escalar*") 

st.markdown (""" 
    El matematico generalmente generaliza estas dos formas de ver al vector, con ayuda de 2 operaciones basicas, suma (con ello tambien hablamos de resta) 
    y multiplicacion por un escalar. Que enriquecen, robustecen y extienden este concepto a las demas areas del conociemiento convirtiendolo en un elemento fundamental. 

""")        

opc = st.selectbox ("¿Que operacion quieres realizar?: ", ["Suma","Resta", "Multiplicacion por un escalar"])  

if opc == "Suma": 

    st.title("Suma de dos vectores en el plano")

    c5,c6 = st.columns(2) 


    with c5: 
        st.subheader("Vector **v**")  
        a = st.number_input("Coordenada X : ", min_value = -14, max_value=15, value = 3)  
        b = st.number_input("Coordenada Y : ", min_value = -14, max_value=15, value = 2)   
         
       
        u = [a,b]   
       
    with c6:  
        st.subheader("Vector **u**")  
        c = st.number_input("Coordena X : ", min_value = -14, max_value=15, value = 4)  
        d = st.number_input("Coordena Y : ", min_value = -14, max_value=15, value = 1) 
        v = [c,d]   

    graf_suma2vecx(u,v)      

elif opc == "Resta":  
    st.title("Resta de dos vectores en el plano")

    c7,c8 = st.columns(2) 
    with c7: 
        st.subheader("Vector **v**")  
        a = st.number_input("Coordenada X : ", min_value = -14, max_value=15, value = 3)  
        b = st.number_input("Coordenada Y : ", min_value = -14, max_value=15, value = 2)   
          
        u = [a,b]   
        
    with c8:  
        st.subheader("Vector **u**")  
        c = st.number_input("Coordena X : ", min_value = -14, max_value=15, value = 4)  
        d = st.number_input("Coordena Y : ", min_value = -14, max_value=15, value = 1) 
        v = [c,d] 
    
    graf_res2vecx(u,v)   
elif opc == "Multiplicacion por un escalar": 
    st.title("Multiplicacion de un vector por un escalar") 
    c9,c10 = st. columns(2) 
    
    with c9:  
        st.subheader("Vector **u**")  
        a = st.number_input("Coordenada X : ", min_value = -14, max_value=15, value = 3)  
        b = st.number_input("Coordenada Y : ", min_value = -14, max_value=15, value = 2)   
         
        u = [a,b]    

    with c10:   
        st.subheader("Escalar")  
        c = st.number_input("Coordena X : ", min_value = -14, max_value=15, value = 4) 
    
    graf_escvector(u,c)    


       



