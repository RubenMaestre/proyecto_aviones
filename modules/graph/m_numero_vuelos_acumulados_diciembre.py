import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

def graficar_numero_vuelos_acumulados_diciembre(df):
    # Agrupar por año y fecha, y calcular vuelos acumulativos
    df_fechas = df.groupby(['anio', 'fecha']).size().reset_index(name='numero_vuelos')
    df_fechas['vuelos_acumulativo'] = df_fechas.groupby('anio')['numero_vuelos'].cumsum()

    # Crear gráficos de línea para cada año
    fig1 = px.line(df_fechas[df_fechas['anio'] == 2021], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['skyblue'])
    fig2 = px.line(df_fechas[df_fechas['anio'] == 2022], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['violet'])
    fig3 = px.line(df_fechas[df_fechas['anio'] == 2023], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['springgreen'])

    # Combinar los gráficos en un solo gráfico con subplots verticales
    fig = make_subplots(rows=3, cols=1, subplot_titles=('2021', '2022', '2023'))

    # Añadir cada gráfico a su respectiva fila
    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=2, col=1)
    fig.add_trace(fig3.data[0], row=3, col=1)

    # Actualizar ejes y layout para mejorar la presentación
    for i in range(1, 4):
        fig.update_xaxes(title_text='Fecha', row=i, col=1)
        fig.update_yaxes(title_text='Número de vuelos acumulados', row=i, col=1)

    fig.update_layout(
        title_text='Número de vuelos acumulados por día en Diciembre por Año',
        title_x=0.5,
        height=1200  # Aumentar la altura para acomodar los tres gráficos
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
