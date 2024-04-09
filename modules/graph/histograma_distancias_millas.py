import streamlit as st
import plotly.express as px
import numpy as np

def graficar_histograma_distancias_millas(df):
    fig = px.histogram(df, x="distancia_millas", title="Histograma de Distancia en Millas", opacity=0.8, nbins=50)

    media = np.mean(df['distancia_millas'])
    mediana = np.median(df['distancia_millas'])

    fig.add_vline(x=media, line_dash="dash", line_color="red", name="Media")
    fig.add_vline(x=mediana, line_dash="dash", line_color="green", name="Mediana")

    fig.update_layout(
        title_x=0.5,
        xaxis_title='Distancia en Millas',
        yaxis_title='Cantidad de Vuelos',
        width=1080
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
