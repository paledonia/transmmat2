import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 
from func_vec import * 

st.title("Subespacios Vectoriales")   
st.divider()  

st.subheader("*Un poema escrito como una operacion algebraica*") 

st.markdown(""" 
Teniendo en cuenta lo aprendido en el anterior capitulo. Conociendo que los vectores pueden representarse como una flecha o una lista y sus 
operaciones basicas. 

Se introducira una nueva forma de ver estos vectores y sus representaciones. Especialmente lo correspondiente a sus coordenadas (componentes) y 
como se descomponen en vectores mas sencillos.  

""") 

st.markdown (""" 
Cuando tenemos por ejemplo el vector **v** = *[6 , 9]* , graficamente se ve asi: 
    """) 
v = [6,9] 
u = [0,0]
graf_2vec2d (v,u)     

st.markdown(""" 
Podemos pensar que cada una de las componentes del vector es un escalar, es decir que cada una de ellas sirve para alargar o encoger vectores.

""")   
st.markdown(" En el  sistema de coordenadas **XY** existen 2 vectores especiales.")
c1, c2 = st.columns([2,1])  

with c1: 
    st.markdown(""" 
    
    
    
    
     """)

    st. markdown(""" 
    Uno de ellos esta ubicado a la *derecha* y tiene longitud uno, que se denomina: 
    """) 
    st.latex("\hat{i} = [1,0]")
    st.markdown(""" 
    El otro esta ubicado hacia *arriba*, tambien de longitud uno y se denomina:  
    """) 
    st.latex("\hat{j} = [0,1]") 
with c2:   
    #st.markdown("*Juntos en el sitema de coordenadas XY se verian asi:* ") 

    i = [8,0] 
    j = [0,8]
    graf_2vec2d(i,j)     

st.markdown("""
Ahora piensa que las coordenada del vector anterior funcionan como escalares. La primera coordenada del vector escala a **i**:  
""")

st.latex("6\hat{i} = 6[1,0] = [6*1 , 6*0] = [6, 0]")  

st.markdown ("Y la segunda coordenada del vector escala a **j**: ")  
st.latex("9\hat{j} = 9[0,1] = [9*0 , 9*1] = [0, 9]")   

st.markdown (""" 
Si ahora sumamos tanto i como j escalados con las coordenadas del primer vector. podremos describir el vector como la suma de las componentes escaladas. 
""") 
st.latex("6\hat{i} + 9\hat{j} = [6 , 0] + [0,9] = [6 , 9]" ) 
v = [6,0] 
u = [0,9]
graf_suma2vecx(v,u)   

st.markdown("""
Esto es muy importante para el Algebra, ya que podemos descomponer cualquier vector de un espacio vectorial y representar este vector como la suma de dos vectores
especiales escalados.
""") 

st.markdown("""Estos vectores especiales: 
""")
c3, c4 = st.columns(2) 
with c3:
    st.latex("\hat{i} = [1,0] ;")
with c4: 
    st.latex("\hat{j} = [0,1]")     

st.markdown("""
Son conocidos como los *vectores base* del sistema de coordenadas **XY**. Y con ellos se puede describir cualquier vector de 
<span style="font-size: 1em;">R<sup>2</sup></span>, descrito como en el desarrollo anterior. 
<span style="font-size: 1em;">R<sup>2</sup></span> es comumente conocido como el plano.
""",unsafe_allow_html=True )

st.divider()   

st.subheader ("""
*¿Es posible elegir otros vectores base?* 
""") 
c5, c6 = st.columns (2) 
with c5:
    st. markdown(""" 
    Si elegimos por ejemplo: 
    """)
    st.latex ("\hat{v} = [5,8]") 
    st.latex ("\hat{u} = [6,2]")
    st.markdown("""
    como nuevos vectores base. Usando la operacion de suma de vectores y
    multiplicacion por un escalar. podremos escalar estos vectores y describir cualquier vector en el plano.  
    """)  
with c6 :
    graf_2vec2d([5,8],[6,2]) 

v = [5,8]
u = [6,2]

st.markdown("""
Sean **a** y **b** escalares podremos describir cualquier vector utilizando las bases **v** y **u**, asi: 
""") 

c7,c8 = st.columns([1,2]) 

with c7: 
    a = st.number_input("Elige el valor para el escalar **a**: ", min_value = -14, max_value=15, value = 4)  
    v = [a*v[0], a*v[1]] 
    st.markdown(f"El vector escaldo es: {v}") 
    b = st.number_input("Elige el valor para el escalar **b**: ", min_value = -14, max_value=15, value = 3)  
    u = [b*u[0], b*u[1]] 
    st.markdown(f"El vector escaldo es: {u}")
with c8: 
    graf_suma2vecx (v,u)

st.markdown("""
Un nuevo par de vectores bases como estos nos proporciona una forma valida de describir cualquier vector en el plano, pero esta descripcion sera distinta de
las descripciones de vectores usando la base del sistema de coordenadas **XY**. Entonces hay que tener en cuenta que cuando describimos
vectores esta descripcion esta atada a unas bases asignadas previamente. 
""")

st.divider()  

st.subheader("*Un tema de espacios:* ")

st.markdown ("""
Cada vez que escalas 2 vectores y los sumas a esto se le conoce como **Combinacion lineal**
""") 

st.latex ("\hat{w} = a\hat{v} + b\hat{u}")

st.markdown("""
Con diferentes escalares puedes generar diferentes *combinaciones lineales* las cuales describen cualquier vector que resida en el plano, pero con 
bases distintas a *i* y *j*. Generando a su vez un espacio creado con estas bases. A esta generacion de espacios se le conoce como **Subespacio vectorial**
""") 


st.subheader("*Para tener en cuenta:* ")

st.markdown (""" 
**Cuando tenemos una combinacion lineal puede pasar 3 cosas:**  
""")

st.markdown ("*1. Que la combinacion lineal genere un nuevo subespacio vectorial que cubre el plano:* ")
  
graf_base ([5,8],[6,2]) 

st.markdown ("esto sucede cuando v y u no son combinacion lineal uno del otro") 

st.latex(r"\hat{v} \neq\ b\hat{u}")   

st.markdown ("*2. Que la combinacion lineal genere un nuevo subespacio vectorial que solo esta en una linea:* ")
  
graf_base ([6,2],[12,4]) 

st.markdown ("esto sucede cuando v y u son combinacion lineal uno del otro") 

st.latex(r"\hat{v} = b\hat{u}")  

st.markdown ("*3. Que la combinacion lineal genere un subespacio vectorial que se centre en el origen* ")
  
graf_base ([0,0],[0,0]) 

st.markdown ("esto sucede cuando v y u son ambos el origen o estan escalados un factor de 0") 

st.latex(r"\hat{v} = 0\hat{u}")   

st.markdown(""" 
Cuando tenemos cualquier par de vectores **v** y **u** junto con cualquier escalar **a** y **b** podremos generar cualquier subespacio que genere a su vez 
el plano. Esto sucede gracias a que **u** y **v** son *Linealmente independietes* o que tanto **v** como **u** no se pueden ver como 
combinacion lineal el uno del otro.  
""") 

st.markdown(""" 
En cambio si un par de vectores **v** u **u** junto con
**a** y **b** escalares generan una linea o se centran en el origen esto indica que los vectores son *Linealmente depedientes* o que tanto **v** como **u**
se pueden ver como combinacion líneal el uno del otro.
""")























st.markdown("""
> *Los matematicos requieren una pequeña dosis, no de genialidad, sino de :rainbow[libertad imaginativa] que, en mayor
> dosis, seria locura.*
>
> **- Angus K. Rodgers**
""")
       