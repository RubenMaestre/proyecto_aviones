import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def graficar_diagrama_caja_retrasos(df):
    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 6))
    
    # Crear el boxplot
    plt.boxplot(df['retraso_llegada'].dropna(), vert=False)  # Usar dropna() para asegurar que no hay NaNs que puedan causar errores
    
    # Añadir títulos y etiquetas
    plt.title('Diagrama de Caja del Retraso en la Llegada')
    plt.xlabel('Retraso en la llegada (minutos)')
    plt.yticks([1], ['Retrasos'])  # Etiquetas para el eje y, aunque solo hay una categoría

    # Mejorar el diseño
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Mostrar el gráfico en la aplicación Streamlit
    st.pyplot(plt.gcf())