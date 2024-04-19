import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_relacion_retrasos_millas(df):
    def asignar_rango_millas(milla):
        if milla < 500:
            return 'menos de 500'
        elif 500 <= milla < 1000:
            return '500-1000'
        elif 1000 <= milla < 1500:
            return '1000-1500'
        elif 1500 <= milla < 2000:
            return '1500-2000'
        else:
            return 'más de 2000'
    
    df['rango_millas'] = df['distancia_millas'].apply(asignar_rango_millas)
    df['retraso'] = df['retraso_llegada'].apply(lambda x: 'con_retraso' if x > 15 else 'sin_retraso')
    
    # Definir el orden de las categorías para el eje x
    orden_rangos = ['menos de 500', '500-1000', '1000-1500', '1500-2000', 'más de 2000']
    df['rango_millas'] = pd.Categorical(df['rango_millas'], categories=orden_rangos, ordered=True)
    
    # Preparar los datos para el gráfico
    datos_grafico = df.groupby(['rango_millas', 'retraso']).size().unstack(fill_value=0).reset_index()
    
    # Configurar el estilo de Seaborn
    sns.set(style="whitegrid")
    
    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(12, 6))
    datos_grafico.set_index('rango_millas').plot(kind='bar', stacked=True, ax=ax,
                                                 color={"con_retraso": "tomato", "sin_retraso": "lightseagreen"})
    
    # Configuraciones del gráfico
    ax.set_title('Cantidad de vuelos con y sin retraso en la llegada según el recorrido del vuelo', fontsize=16)
    ax.set_xlabel('Rango de millas', fontsize=14)
    ax.set_ylabel('Cantidad de vuelos', fontsize=14)
    ax.legend(title='Retraso en la llegada', fontsize=12)
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)