import streamlit as st
import plotly.express as px

def graficar_diagrama_distancia_millas(df):
    fig = px.box(df, x='distancia_millas', notched=True, points="all")

    fig.update_layout(
        title='Diagrama de Caja de la Distancia en Millas',
        xaxis_title='Distancia en Millas',
        title_x=0.5,
        width=1080
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
