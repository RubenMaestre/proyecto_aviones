import streamlit as st
import plotly.express as px
import pandas as pd

def graficar_correlacion_lineal(df):
    # Verificar y manejar valores nulos
    if df["retraso_salida"].isnull().any() or df["retraso_llegada"].isnull().any():
        st.warning("Advertencia: Se detectaron valores nulos en las columnas de datos.")
        df = df.dropna(subset=["retraso_salida", "retraso_llegada"])  # Eliminar valores nulos
    
    # Usar una muestra de datos para mantener el rendimiento
    df_sample = df.sample(n=100000, random_state=42) if len(df) > 100000 else df

    # Crear gráfico de dispersión
    fig = px.scatter(
        data_frame=df_sample,
        x="retraso_salida",
        y="retraso_llegada",
        title="Correlación Lineal entre los indicadores de retraso en la salida y en la llegada de vuelos",
        opacity=0.5,
        trendline=None  # Remover la línea de tendencia para mejorar el rendimiento
    )

    # Ajustes de visualización y rendimiento
    fig.update_layout(
        title_x=0.5,
        width=900,
        height=600,
        showlegend=False
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
