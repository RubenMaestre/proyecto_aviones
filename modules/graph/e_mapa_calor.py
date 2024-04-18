import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_mapa_calor_correlacion(df):
    # Calcula la matriz de correlación para las columnas seleccionadas
    columnas = ['numero_vuelo', 'duracion_programada_vuelo', 'duracion_real', 'retraso_salida', 'tiempo_pista_salida',
                'tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion',
                'tiempo_retraso_seguridad', 'retraso_llegada', 'dia_semana', 'anio', 'fin_de_semana', 'festivos']
    matriz_corr = df[columnas].corr().round(1)

    # Crear un mapa de calor con Plotly Express
    fig = px.imshow(matriz_corr, text_auto=True, title="Correlaciones Lineales de las Variables Numéricas",
                    aspect="auto", color_continuous_scale='reds')
    fig.update_layout(title_x=0.5, width=1000, height=800)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)