import streamlit as st
import plotly.express as px

def graficar_correlacion_lineal(df):
    # Asegúrate de que 'retraso_salida' y 'retraso_llegada' son los nombres correctos de las columnas en tu DataFrame
    fig = px.scatter(
        data_frame=df,
        x="retraso_salida",
        y="retraso_llegada",
        title="Correlación Lineal entre los indicadores de retraso en la salida y en la llegada de vuelos",
        opacity=0.5,
        trendline='ols'  # Añade una línea de tendencia de mínimos cuadrados ordinarios
    )

    fig.update_layout(title_x=0.5)  # Centrar el título

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
