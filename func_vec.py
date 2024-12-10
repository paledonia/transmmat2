import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 

def graf_2vec2d (v1,v2): 
    
    #convierte los vectores en arreglos "Array"
    v1 = np.array(v1)
    v2 = np.array(v2) 

    #estable el canva para graficar
    fig, ax = plt.subplots() 

    #grafica los vectores 
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector 1')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector 2 ')

    # Configurar el gráfico
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Grafica de vectores en el plano")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)
    
    #muestra el grafico
    return st.pyplot(fig) 


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def graf_escvector (v, c): 
    v = np.array(v)  
    c = c 
    v_1 = c*v
    v_1 = np.array(v_1) 

    fig, ax = plt.subplots() 

    ax.quiver (0,0,v_1[0],v_1[1],angles='xy', scale_units='xy', scale=1, color='blue', label='Vector escalado')
    ax.quiver (0,0,v[0],v[1],angles='xy', scale_units='xy', scale=1, color='lightblue', label='Vector sin escalar')


    # Configurar el gráfico
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Vector multiplicado por un escalar")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)

    # Mostrar el gráfico 
    return st.pyplot(fig) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def graf_suma2vecx (v1 , v2):  

    v1 = np.array(v1) 
    v2 = np.array(v2) 

    suma_vec = v1 + v2 
    suma_vec = np.array(suma_vec)  

    fig, ax = plt.subplots()  

    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='$\mathbf{V}$')
    ax.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='grey', label='$\mathbf{U}$ en la punta de $\mathbf{V}$')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='black', label='$\mathbf{U}$')
    ax.quiver(0,0,suma_vec[0],suma_vec[1], angles='xy', scale_units='xy', scale = 1 , color='blue', label = '$\mathbf{V}$ + $\mathbf{U}$')

    # Configurar el gráfico
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Representacion Grafica de $\mathbf{V}$ + $\mathbf{U}$")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)

        # Mostrar el gráfico
    return st.pyplot(fig)  


  #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def graf_res2vecx (v1, v2): 
    v1 = np.array(v1) 

    v2 = np.array(v2)  
    v2_1 = -v2 
    v2_1 = np.array(v2_1)

    res_vec = v1 - v2 
    res_vec = np.array(res_vec)  

    fig, ax = plt.subplots()  

    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='$\mathbf{V}$')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='black', label='$\mathbf{U}$')
    ax.quiver(v1[0], v1[1], v2_1[0], v2_1[1], angles='xy', scale_units='xy', scale=1, color='grey', label='$\mathbf{U}$ en la punta de $\mathbf{V}$')
    ax.quiver(0,0,res_vec[0],res_vec[1], angles='xy', scale_units='xy', scale = 1 , color='blue', label = '$\mathbf{V}$ - $\mathbf{U}$')

    # Configurar el gráfico
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Representacion Grafica de $\mathbf{V}$ - $\mathbf{U}$")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)     

    return st.pyplot(fig)  

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graf_base (v1,v2):  
    v1 = np.array(v1) 
    v2 = np.array(v2) 
    r = 95   

    fig, ax = plt.subplots()    

     # Generar líneas paralelas a v1 (variando en dirección de v2)
    grid_range = np.arange(-r, r + 1, 1)
    for t in grid_range:
        start = t * v2 - (r * v1)  # Punto inicial
        end = t * v2 + r * v1    # Punto final
        ax.plot([start[0], end[0]], [start[1], end[1]], color='lightpink', linewidth=0.8, linestyle='--')

    # Generar líneas paralelas a v2 (variando en dirección de v1)
    for s in grid_range:
        start = s * v1 - (r * v2)  # Punto inicial
        end = s * v1 + r * v2    # Punto final
        ax.plot([start[0], end[0]], [start[1], end[1]], color='lightblue', linewidth=0.8, linestyle='--')

    # Graficar los vectores base
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'$\mathbf{{i_n}} = {v1}$')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='black', label=f'$\mathbf{{j_n}} = {v2}$')

    # Configurar el gráfico
    ax.axhline(0, color='black', linewidth=0.5)  # Eje X
    ax.axvline(0, color='black', linewidth=0.5)  # Eje Y
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Espacio generado por las Bases")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()     

    return st.pyplot(fig)  