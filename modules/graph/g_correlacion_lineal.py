import streamlit as st
import plotly.express as px
import pandas as pd

def graficar_correlacion_lineal(df):
    # Verificar y manejar valores nulos
    if df["retraso_salida"].isnull().any() or df["retraso_llegada"].isnull().any():
        st.warning("Advertencia: Se detectaron valores nulos en las columnas de datos.")
        df = df.dropna(subset=["retraso_salida", "retraso_llegada"])  # Eliminar valores nulos
    
    # Tamaño de la muestra y random_state configurados
    sample_size = 300000
    random_state = 42

    # Comprobación del tamaño de los datos para decidir si se toma una muestra
    if len(df) > 10000:
        df_sample = df.sample(n=sample_size, random_state=random_state)
        message = f"Esta visualización está basada en una muestra aleatoria de {sample_size} datos del total, " \
                  f"utilizando un estado aleatorio (random state) de {random_state}."
        st.info(message)
    else:
        df_sample = df

    # Crear gráfico de dispersión
    fig = px.scatter(
        data_frame=df_sample,
        x="retraso_salida",
        y="retraso_llegada",
        title="Correlación Lineal entre los indicadores de retraso en la salida y en la llegada de vuelos",
        opacity=0.5,
        trendline=None  # Remover la línea de tendencia para mejorar el rendimiento
    )
    # Cambiar el color de los puntos a fucsia
    fig.update_traces(marker=dict(color='fuchsia'))

    # Ajustes de visualización y rendimiento
    fig.update_layout(
        title_x=0.5,
        width=800,
        height=600,
        showlegend=False
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)