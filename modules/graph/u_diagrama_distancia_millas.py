import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
def graficar_diagrama_distancia_millas(df):
    # Configurar el estilo de Seaborn para los gráficos
    sns.set(style="whitegrid")
    
    # Crear la figura y el eje para el gráfico
    fig, ax = plt.subplots()
    
    # Crear el diagrama de caja
    sns.boxplot(x=df['distancia_millas'], notch=True, ax=ax)
    
    # Establecer el título y las etiquetas de los ejes
    ax.set_title('Diagrama de Caja de la Distancia en Millas', fontsize=16)
    ax.set_xlabel('Distancia en Millas', fontsize=14)
    
    # Ajustar las dimensiones de la figura si es necesario
    fig.set_size_inches(15, 6)  # Tamaño en pulgadas (ancho, alto)
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)