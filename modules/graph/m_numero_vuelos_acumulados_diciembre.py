import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_numero_vuelos_acumulados_diciembre(df):
    # Agrupar por año y fecha, y calcular vuelos acumulativos
    df_fechas = df.groupby(['anio', 'fecha']).size().reset_index(name='numero_vuelos')
    df_fechas['vuelos_acumulativo'] = df_fechas.groupby('anio')['numero_vuelos'].cumsum()

    # Crear un único gráfico de línea para los años 2021, 2022 y 2023
    fig = px.line(df_fechas, x='fecha', y='vuelos_acumulativo',
                  color='anio',  # Diferenciar las líneas por año
                  color_discrete_sequence=['skyblue', 'violet', 'springgreen'],  # Colores para cada año
                  labels={'anio': 'Año', 'vuelos_acumulativo': 'Número de vuelos acumulados'},
                  title='Número de vuelos acumulados por día en Diciembre por Año')

    # Ajustes adicionales al layout del gráfico
    fig.update_layout(
        title_x=0.5,
        xaxis_title='Fecha',
        yaxis_title='Número de vuelos acumulados',
        legend_title='Año',
        height=600  # Ajustar según sea necesario
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

