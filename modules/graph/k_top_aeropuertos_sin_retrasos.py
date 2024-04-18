import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_top_aeropuertos_con_sin_retrasos(df):
    # Filtrar vuelos con y sin retraso
    retrasos_llegada = df[df['retraso_llegada'] > 15]
    sin_retraso_llegada = df[df['retraso_llegada'] <= 15]

    # Agrupar por aeropuerto y contar vuelos
    retraso_aeropuerto_llegada = retrasos_llegada.groupby(['aeropuerto_origen']).size().reset_index(name='con_retraso')
    sin_retraso_aeropuerto = sin_retraso_llegada.groupby(['aeropuerto_origen']).size().reset_index()
    sin_retraso_aeropuerto.columns = ['aeropuerto_origen', 'sin_retraso']

    # Combinar los datos en un solo DataFrame y ordenar
    retrasos_aeropuerto = retraso_aeropuerto_llegada.merge(sin_retraso_aeropuerto, on='aeropuerto_origen', how='left').fillna(0)
    retrasos_aeropuerto_ordenado = retrasos_aeropuerto.sort_values(by='con_retraso', ascending=False)

    # Crear un gráfico de barras para los 15 aeropuertos principales
    fig = px.bar(retrasos_aeropuerto_ordenado[:15], 
                 x='aeropuerto_origen', 
                 y=['con_retraso', 'sin_retraso'], 
                 title='Top 15 aeropuertos de origen con mayor cantidad de vuelos con retraso en la llegada',
                 labels={'aeropuerto_origen': 'Aeropuerto de Origen', 'value': 'Cantidad de vuelos'},
                 opacity=0.7, 
                 color_discrete_map={"con_retraso": "turquoise", "sin_retraso": "tan"})

    fig.update_layout(title_x=0.5, xaxis={'categoryorder': 'total descending'})

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)