import streamlit as st
import plotly.graph_objs as go

def graficar_horas_vuelos(df):
    # Convertir las horas a minutos desde la medianoche para ordenarlas
    df["hora_salida_minutos"] = df["hora_salida_real"].apply(lambda x: x.hour * 60 + x.minute)
    df["hora_llegada_minutos"] = df["hora_llegada_real"].apply(lambda x: x.hour * 60 + x.minute)

    # Crear la figura con Plotly Graph Objects
    fig = go.Figure()

    fig.add_trace(go.Box(x=df["hora_salida_minutos"], name="Salida"))
    fig.add_trace(go.Box(x=df["hora_llegada_minutos"], name="Llegada"))

    fig.update_layout(
        title="Diagrama de caja para las horas de salida y llegada de los vuelos",
        title_x=0.5,
        xaxis_title="Minutos desde la medianoche",
        yaxis_title="Distribución de las horas",
        width=1080,  # Ancho personalizado
        height=720   # Altura personalizada
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)