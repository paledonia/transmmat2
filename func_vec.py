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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def superposicion_espacios_gen( v1_base, v2_base, rango=10):
    """
    Superpone dos cuadrículas generadas por las bases canonicas y las nuevas bases.
    : i_can: base canonica (1 , 0)
    : j_can: base canonica (0 , 1)
    : v1_base: Primer vector base del segundo sistema.
    : v2_base: Segundo vector base del segundo sistema.
    : rango: Rango para la cuadrícula (por defecto 10).
    """
    # Convertir los vectores base a arreglos de NumPy
    i_can = np.array([1,0])
    j_can = np.array([0,1])

     #creacion de la matriz de bases

    mat_1 = [[i_can],[j_can]]
    mat_1 = np.array(mat_1)
    trans_m_1 = mat_1.T

    v1_base = np.array(v1_base)
    v2_base = np.array(v2_base)

    mat_2 = [[v1_base],[v2_base]]
    mat_2 = np.array(mat_2)
    trans_m_2 = mat_2.T

    # Crear la figura
    fig, ax = plt.subplots()    

    # Rango para la cuadrícula
    grid_range = np.arange(-rango, rango + 1, 1)

    # Dibujar la primera cuadrícula (Base 1)
    for t in grid_range:
        start = t * j_can - rango * i_can
        end = t * j_can + rango * i_can
        ax.plot([start[0], end[0]], [start[1], end[1]], color='gray', linewidth=0.8, linestyle='--', alpha=0.7)
    for s in grid_range:
        start = s * i_can - rango * j_can
        end = s * i_can + rango * j_can
        ax.plot([start[0], end[0]], [start[1], end[1]], color='gray', linewidth=0.8, linestyle='--', alpha=0.7)

    # Dibujar la segunda cuadrícula (Base 2)
    for t in grid_range:
        start = t * v2_base - rango * v1_base
        end = t * v2_base + rango * v1_base
        ax.plot([start[0], end[0]], [start[1], end[1]], color='pink', linewidth=0.8, linestyle='--', alpha=0.7)
    for s in grid_range:
        start = s * v1_base - rango * v2_base
        end = s * v1_base + rango * v2_base
        ax.plot([start[0], end[0]], [start[1], end[1]], color='blue', linewidth=0.8, linestyle='--', alpha=0.7)

    # Graficar los vectores base de ambos sistemas
    ax.quiver(0, 0, i_can[0], i_can[1], angles='xy', scale_units='xy', scale=1, color='black', label='Base canonica $\mathbf{i}$')
    ax.quiver(0, 0, j_can[0], j_can[1], angles='xy', scale_units='xy', scale=1, color='black', label='Base canonica $\mathbf{j}$')
    ax.quiver(0, 0, v1_base[0], v1_base[1], angles='xy', scale_units='xy', scale=1, color='pink', label='i nuevo $\mathbf{i_n}$')
    ax.quiver(0, 0, v2_base[0], v2_base[1], angles='xy', scale_units='xy', scale=1, color='blue', label='j nuevo $\mathbf{j_n}$')

    # Configurar el gráfico
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Superposicion de espacios vectoriales")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)

    return st.pyplot(fig)
  
 #__________________________________________________________________________________________________________________________________________
def graficar_determinante(matriz):
    try:
        matriz = np.array(matriz) # Convert the input to a numpy array
        if matriz.shape != (2, 2):
            st.error("La matriz debe ser de 2x2.")
            return

        a, b = matriz[0, :]
        c, d = matriz[1, :]

        det = np.linalg.det(matriz)

        plt.figure(figsize=(6, 6))
        plt.quiver(0, 0, a, c, angles='xy', scale_units='xy', scale=1, color='blue', label=f'i_n ({a},{c})')
        plt.quiver(0, 0, b, d, angles='xy', scale_units='xy', scale=1, color='red', label=f'j_n ({b},{d})')

        paralelogramo_x = [0, a, a + b, b, 0]
        paralelogramo_y = [0, c, c + d, d, 0]
        plt.fill(paralelogramo_x, paralelogramo_y, color='lightblue', alpha=0.5, label=f'Área: {det:.2f}')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(f"Determinante de la Matriz: {det:.2f}")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.legend()
        plt.grid(True)

        st.pyplot(plt) # Use st.pyplot

    except ValueError:
        st.error("La matriz no es válida. Asegúrate de que es una matriz de 2x2")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}") 

def graf_1vec2d (v1): 
    
    #convierte los vectores en arreglos "Array"
    v1 = np.array(v1)
  

    #estable el canva para graficar
    fig, ax = plt.subplots() 

    #grafica los vectores 
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector 1')
    
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
