import streamlit as st
import plotly.express as px

def graficar_correlacion_lineal(df):
    # Verificar y manejar valores nulos
    if df["retraso_salida"].isnull().any() or df["retraso_llegada"].isnull().any():
        st.warning("Advertencia: Se detectaron valores nulos en las columnas de datos.")
        df = df.dropna(subset=["retraso_salida", "retraso_llegada"])  # Eliminar valores nulos

    fig = px.scatter(
        data_frame=df,
        x="retraso_salida",
        y="retraso_llegada",
        title="Correlación Lineal entre los indicadores de retraso en la salida y en la llegada de vuelos",
        opacity=0.5,
        trendline='ols',  # Añade una línea de tendencia de mínimos cuadrados ordinarios
        hover_data={"retraso_salida": True, "retraso_llegada": True}  # Mostrar más datos al pasar el mouse
    )

    fig.update_layout(
        title_x=0.5,  # Centrar el título
        width=1080,  # Ancho personalizado
        height=720   # Altura personalizada
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)