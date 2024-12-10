import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 
from func_vec import * 

st.title("Transformaciones Lineales") 
st.divider() 
st.subheader("Cuestion de movimiento") 
st.markdown(""" 
Cuando pensamos en transformacion lineales pensamos en funciones. Basicamente
una transformacion lineal toma un vector de entrada y lo transforma en un vector de salida.
""") 

st.latex ("L(\hat{v}) = \hat{u}") 

st.markdown("*¿Por que usamos la palabra transformacion para indicar funcion?*") 
st.markdown("""

Se usa esta palabra ya que ella indica movimiento. Cuando pensamos en transformar un vector estamos hablando de que un vector de entrada
se mueve hacia un vector de llegada
""") 

c1, c2 = st.columns(2) 
with c1: 
    st.markdown("**Vector de Entrada:** ") 
    st.latex ("\hat{v} = [-6,7]")  
    v = [-6,7]
    graf_1vec2d(v)
with c2: 
    st.markdown("**Vector de Llegada:** ") 
    st.latex ("\hat{u} = [6,2]")  
    u = [6,2]
    graf_1vec2d(u) 

st.markdown ("""
En este caso especifico el vector **v** (vector de entrada) se movio hacia el vector **u** (vector de llegada)
""")  

st.latex ("L(\hat{v}) = \hat{u}")   

st.markdown ("""
Esta idea de transformar vectores en otros tambien se puede llevar al plano en general, pensando que todas la combinaciones 
lineales de un subespacio vectorial son a su vez el conjunto de todas las tranformaciones lineales de un sistema de coordenadas.
""") 

st.markdown("""
""")  

st.divider()  

st.subheader("Representacion de un espacio vectorial como una matriz:") 

st.markdown (""" 
Cuando estamos hablando de un espacio vectorial, estamos hablando a su vez de una matriz. Ya que una matriz respresenta las bases del sistema de coordenadas. 

Volvamos a las bases del sistema de coordenadas de <span style="font-size: 1em;">R<sup>2</sup></span>
""",unsafe_allow_html=True ) 



c3, c4 = st.columns (2) 

with c3:  
    st.markdown (""" 
    Si estos son nuestros vectores base de <span style="font-size: 1em;">R<sup>2</sup></span> para hallar la matriz
    asociada solo basta con colocar  a **i** como columna y a **j** tambien como columna juntandolas como un arreglo. 
    """,unsafe_allow_html=True)   
    st.latex("\hat{i} = [1,0]") 
    st.latex("\hat{j} = [0,1]")  
    st.markdown("""
    El resultado es: 
    """)  

    st.latex (r""" 
    \begin {bmatrix}
    1 & 0 \\
    0 & 1
    \end{bmatrix}
    """)  
with c4: 
    st.markdown("""
    Representacion grafica de las bases de <span style="font-size: 1em;">R<sup>2</sup></span>
    """,unsafe_allow_html=True)
    
    graf_base ([1,0],[0,1])

c5, c6 = st.columns (2) 

with c5:  
    st.markdown("""
    Si en ves de tener a **i** y **j** como bases del sistema tenemos: 
    """)  
    st.latex("\hat{v} = [5,2]") 
    st.latex("\hat{u} = [4,-6]")  
    st.markdown("""
    Siguiendo el proceso anterior me da como resultado: 
    """)  
    st.latex (r""" 
    \begin {bmatrix}
    5 & 4 \\
    2 & -6
    \end{bmatrix}
    """)  
with c6: 
    st.markdown("""
    Representacion grafica de las bases de <span style="font-size: 1em;">R<sup>2</sup></span>
    """,unsafe_allow_html=True)
    
    graf_base ([5,2],[4,-6]) 

st.markdown(""" 
La cuadricula generada en la primera imagen representa el plano. En la segunda imagen la cuadricula representa el subespacio generado por los dos vectores **v** y **u** 

Si podemos observar ambas cualdriculas, aunque distintas, abarcan todo el plano. Por esta razon es que se puede representar cualquier vector de la base canonica, 
en terminos de cualquier otra base que sea una combinacion lineal y que esa combinacion sea linealmente independiente. Si la combinacion es linealmente dependiente
esta generara solo una linea que pasa por el origen, o en casos mas aburridos, el centro (0,0).

""") 

st.divider () 

st.subheader("*¿Como trasnformo un vector de la base canonica a cualquier otra base?*") 

st.markdown(""" 
Para trasladar un vector de la base canonica a cualquier otra base solo tenemos que tener 2 elementos: 
  1. El vector en terminos de la base canonica 
  2. La matriz de representacion de las nuevas bases.
""") 

st.markdown ("**Ejemplo:** ")  

c7, c8 = st.columns (2) 
with c7:
    st.markdown ("Sea **w** el vector descrito en terminos de la base canonica: ")
    st.latex ("\hat{w} = [-5,7]") 
    graf_1vec2d([-5,7]) 

with c8: 

    st.markdown("Sea **u** y **v** los vectores de la nueva base: ") 
    st.latex (r""" 
    \begin {bmatrix}
    5 & 4 \\
    2 & -6
    \end{bmatrix}
    """)   
    graf_base([5,2],[4,-6])  
st.markdown("""  
Para transformar el vector **w** solo multiplicamos la primera coordenada del vector con el vector **u** y la segunda coordenada con el vector **v**, asi:  
""") 
st.latex (r""" 
    \begin {bmatrix}
    (-5)*5 + (7)*4\\
    (-5)*2 + (7)*6
    \end{bmatrix} = \begin {bmatrix}
    3 \\
    32
    \end{bmatrix}
    """)   
st.markdown ("""
El resultado de la tranformacion, numericamente, es la siguiente:  
""")
st.latex("\hat{r} = [3,32]") 
graf_1vec2d([3,32])  

st.markdown(""" 
Generalizando para cualquier vector de la base canonica y cualquier **v** y **u** como vectores de la nueva base, tenemos:  
""") 

c9, c10 = st.columns (2) 
with c9:
    st.markdown ("Sea **w** el vector descrito en terminos de la base canonica: ")
    st.latex ("\hat{w} = [a,b]") 
   

with c10: 

    st.markdown("Sea **u** y **v** los vectores de la nueva base: ") 
    st.latex (r""" 
    \begin {bmatrix}
    u1 & v1 \\
    u2 & v2
    \end{bmatrix}
    """)   
st.markdown("""  
Para transformar el vector **w** solo multiplicamos la primera coordenada del vector con el vector **u** y la segunda coordenada con el vector **v**, asi:  
""") 
st.latex (r""" 
    \begin {bmatrix}
    (a)*u1 + (b)*v1\\
    (a)*u2 + (b)*v2
    \end{bmatrix} 
    """)    
st.markdown("Vista como combinacion lienal: ")
st.latex ("\hat{w} = a\hat{u} + b\hat{v}")   

st.markdown("""
Esta generalizacion nos hace ver como se comporta la multiplicacion de matrices con un vector. En
sencillas palabras una multiplicacion de una matriz por un vector es la representacion de una transformacion lineal o un vector de salida moviendose a uno de llegada.
""")  

st.markdown(""" 
Ahora que sabemos lo que significa transformar un vector, teniendo la base de llegada, surge la pregunta:
""")

st.divider ()  

st.subheader("*¿Puedo moverme de una de una base a otra?*")  
st.markdown(""" 
Si es posible de realizar. solo tenemos que tener 2 pares de bases y su reprensentacion matricial en <span style="font-size: 1em;">R<sup>2</sup></span> 

""",unsafe_allow_html=True)  

st.markdown("**Ejemplo:** ")

c11, c12 = st. columns(2) 

with c11: 
    st.markdown(""" 
    En la primera base usamos la base canonica: 
    """) 
    st.latex (r""" 
    \begin {bmatrix}
    1 & 0 \\
    0 & 1
    \end{bmatrix}
    """)
    graf_base([1,0],[0,1])  
with c12: 
    st.markdown(""" 
    En la segunda base usamos: 
    """) 
    st.latex (r""" 
    \begin {bmatrix}
    5 & 4 \\
    2 & -6
    \end{bmatrix}
    """)   
    graf_base([5,2],[4,-6])  
st.markdown ("""
Usaremos la logica del ejemplo anterior para multiplicar las bases, pero antes divideremos la segunda matriz en 2 columnas
""") 

st.latex("\hat{v1} = [5,2]")  
st.latex("\hat{v2} = [4,-6]")  

st.markdown(""" 
Con las columnas del primer vector separada procedemos a aplicar lo visto anteriormente: 
""")  
st.latex (r""" 
    \begin {bmatrix}
    (5)*1 + (2)*0\\
    (5)*0 + (2)*1
    \end{bmatrix} = \begin {bmatrix}
    5 \\
    2
    \end{bmatrix}
    """)    

st.markdown("""  
Obtiniendo la primera columna de la matriz resultante
""")  

st.latex (r""" 
    \begin {bmatrix}
    5\\
    2
    \end{bmatrix} 
    """)    
st.markdown(""" 
Ahora aplicamos el mismo razonamieto para la segunda columna: 
""")  
st.latex (r""" 
    \begin {bmatrix}
    (4)*1 + (-6)*0\\
    (4)*0 + (-6)*1
   \end{bmatrix} = \begin {bmatrix}
    4 \\
    -6
    \end{bmatrix}
    """)  
st.markdown("""  
Obtiniendo la segunda columna de la matriz resultante
""")  

st.latex (r""" 
    \begin {bmatrix}
    4\\
    -6
    \end{bmatrix} 
    """)     
st.markdown(""" 
Teniedo como representacion matricial:
""")  
st.latex (r""" 
    \begin {bmatrix}
    5 & 4 \\
    2 & -6
    \end{bmatrix}
    """)  
st.markdown("""
El cambio de bases se ve representado de la siguiente manera: 

""")    
superposicion_espacios_gen([5,2],[4,-6]) 

st.markdown("""
La cuadricula gris representa la base anterior, que en este caso es la base canonica del plano. Y la cuadricula generada por las lineas rosadas y azules 
representan la nueva base. Ambas estan superpuestas, ya que esto indica que nos movimos de una base hacia otra.
""") 

st.markdown(""" 
Generalizando para cualesquiera 2 bases en <span style="font-size: 1em;">R<sup>2</sup></span> tenemos:

""",unsafe_allow_html=True)   

c13, c14 = st. columns(2) 

with c13: 
    st.markdown(""" 
    Definimos M1 como la matriz de la primera base: 
    """) 
    st.latex (r""" 
    M1 = \begin {bmatrix}
    a & b \\
    c & d
    \end{bmatrix}
    """) 
with c14: 
    st.markdown(""" 
    Definimos M2 como la matriz de la seguda base: 
    """) 
    st.latex (r""" 
    M2 =\begin {bmatrix}
    e & f \\
    g & h
    \end{bmatrix}
    """) 

st.markdown ("""
Dividimos a M2 en 2 columnas: 
""")  
st.latex (r""" 
    \begin {bmatrix}
    e\\
    g
    \end{bmatrix} ; \begin {bmatrix}
    f\\
    h
    \end{bmatrix}
    """)   
st.markdown(""" 
Con las columnas de M2 separadas, prodemos a multiplicar M1 por la primera columna de M2: 
""")  
st.latex (r""" 
    \begin {bmatrix}
    (e)*a + (g)*b\\
    (e)*c + (g)*d
    \end{bmatrix} 
    """)    

st.markdown("""  
Obteniendo la primera columna de la matriz resultante
""")  

st.latex (r""" 
    \begin {bmatrix}
    (e)*a + (g)*b\\
    (e)*c + (g)*d
    \end{bmatrix} 
    """)     

st.markdown(""" 
Continuamos multiplicando a M1 por la segunda columna de M2: 
""")  
st.latex (r""" 
    \begin {bmatrix}
    (f)*a + (h)*b\\
    (f)*c + (h)*d
    \end{bmatrix} 
    """)    

st.markdown("""  
Obtiniendo la primera columna de la matriz resultante
""")  

st.latex (r""" 
    \begin {bmatrix}
    (f)*a + (h)*b\\
    (f)*c + (h)*d
    \end{bmatrix} 
    """)   
st.markdown(""" 
Teniendo como representacion matricial:
""")  
st.latex (r""" 
    \begin {bmatrix}
    ea + gb & fa + hb \\
    ec + gd & fc + hd
    \end{bmatrix}
    """)     

st.markdown(""" 
Si observamos con detenimiento podremos notar que el resultado anterior es la definicion de Multiplicacion de matrices en el plano. Multiplicando la primera 
fila de M1 con la primera columna de M2, la segunda fila de M1 con la primera columna de M2.... etc 

""")    

st.markdown(""" 
Y es aqui donde queria llegar con el desarrollo del aplicativo. Que nos dieramos cuenta por que mutliplicacion de matrices esta definida como la conocemos. 

Basicamente la 
multiplicacion entre matrices de igual dimension, representa el cambio o movimiento de un subespacio generado a otro. Esto es sorprendete ya que cada vez que hacemos 
operacione entre vectores o matrices, estamos continuamente cambiando el espacio en el cual trabajamos.

""")   

st.markdown("""
> *Desafortunadamente nadie puede decirte lo que es la :rainbow[Matriz].
> Tienes que verla por ti mismo*
>
> **- Morpheus**
""")
       

   















