import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def graficar_histograma_distancias_millas(df):
    # Configurar el estilo de Seaborn
    sns.set(style="whitegrid")
    
    # Crear el histograma usando Matplotlib
    plt.figure(figsize=(12, 6))
    sns.histplot(df['distancia_millas'], bins=50, kde=False, color="skyblue", alpha=0.8)

    # Calcular media y mediana
    media = np.mean(df['distancia_millas'])
    mediana = np.median(df['distancia_millas'])

    # Añadir líneas verticales para la media y la mediana
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1, label=f'Mediana: {mediana:.2f}')

    # Añadir título y etiquetas
    plt.title('Histograma de Distancia en Millas', fontsize=16)
    plt.xlabel('Distancia en Millas', fontsize=14)
    plt.ylabel('Cantidad de Vuelos', fontsize=14)

    # Añadir leyenda
    plt.legend()

    # Mostrar el histograma en Streamlit
    st.pyplot(plt)

