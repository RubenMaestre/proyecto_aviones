import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_maxima_distancia_millas(df):
    # Crear una columna única que represente el par de aeropuertos en ambos sentidos
    df['par_aeropuertos'] = df.apply(lambda x: '-'.join(sorted([x['aeropuerto_origen'], x['aeropuerto_destino']])), axis=1)

    # Agrupar por este par y encontrar la distancia máxima entre ellos
    max_distancias = df.groupby('par_aeropuertos')['distancia_millas'].max().reset_index()

    # Ordenar por distancia de mayor a menor y tomar los top 20
    top_10_distancias = max_distancias.sort_values(by='distancia_millas', ascending=False).head(10)

    # Crear un gráfico de barras usando Matplotlib
    plt.figure(figsize=(10, 8))  # Configurar el tamaño del gráfico
    sns.barplot(x='distancia_millas', y='par_aeropuertos', data=top_10_distancias, palette='viridis')

    plt.title('Top 20 Máxima Distancia en Millas entre Pares de Aeropuertos Únicos')
    plt.xlabel('Distancia en Millas')
    plt.ylabel('Par de Aeropuertos')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Mostrar la figura en la aplicación Streamlit
    st.pyplot(plt.gcf())