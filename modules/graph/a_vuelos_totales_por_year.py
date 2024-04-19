import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_vuelos_totales_por_year(df):
    # Asegurarse que el año sea tipo string para la visualización
    df["anio"] = df["anio"].astype(str)

    # Agrupar los datos por año y contar los vuelos
    vuelos_anuales = df.groupby(['anio']).size().reset_index(name='cantidad_vuelos_anuales')

    # Crear el gráfico de barras usando Plotly Express
    fig = px.bar(data_frame=vuelos_anuales,
                 x='anio',
                 y='cantidad_vuelos_anuales',
                 opacity=0.8,
                 title="Cantidad de vuelos anuales",
                 color='anio')

    # Actualizar la configuración del layout del gráfico
    fig.update_layout(
        title_x=0.5,
        xaxis_title='Años',
        yaxis_title='Cantidad de vuelos',
        xaxis={'categoryorder': 'total descending', 'type': 'category'}  # Especificar que el eje x es categórico
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)
