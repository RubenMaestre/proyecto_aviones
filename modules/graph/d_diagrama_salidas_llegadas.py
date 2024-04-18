import streamlit as st
import plotly.graph_objs as go
import pandas as pd

def graficar_horas_vuelos(df):
    # Verificar y manejar valores nulos para las columnas de tiempo
    for col in ['hora_salida_real', 'hora_llegada_real']:
        if df[col].isnull().any():
            st.warning(f"Existen valores nulos en {col}. Se omitirán esos registros.")
            df = df.dropna(subset=[col])

    # Convertir las horas a minutos desde la medianoche para ordenarlas
    df["hora_salida_minutos"] = df["hora_salida_real"].apply(lambda x: x.hour * 60 + x.minute)
    df["hora_llegada_minutos"] = df["hora_llegada_real"].apply(lambda x: x.hour * 60 + x.minute)

    # Crear la figura con Plotly Graph Objects
    fig = go.Figure()

    fig.add_trace(go.Box(x=df["hora_salida_minutos"], name="Salida"))
    fig.add_trace(go.Box(x=df["hora_llegada_minutos"], name="Llegada"))

    # Definir las marcas personalizadas para el eje x
    tickvals = [i * 60 for i in range(25)]  # Cada hora en minutos
    ticktext = [f'{i}:00' for i in range(25)]  # Etiquetas de horas

    fig.update_layout(
        title="Diagrama de caja para las horas de salida y llegada de los vuelos",
        title_x=0.5,
        xaxis_title="Hora del día",
        yaxis_title="Distribución de las horas",
        xaxis=dict(
            tickmode='array',
            tickvals=tickvals,
            ticktext=ticktext
        ),
        width=900,  # Ancho personalizado
        height=600   # Altura personalizada
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

