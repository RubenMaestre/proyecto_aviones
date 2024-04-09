import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_relacion_retrasos_millas(df):
    retraso_millas = df[df['retraso_llegada'] > 15].copy()
    sin_retraso_millas = df[df['retraso_llegada'] <= 15].copy()

    def asignar_rango_millas(milla):
        if milla < 500:
            return 'menos de 500'
        elif 500 <= milla < 1000:
            return '500-1000'
        elif 1000 <= milla < 1500:
            return '1000-1500'
        elif 1500 <= milla < 2000:
            return '1500-2000'
        else:
            return 'más de 2000'

    retraso_millas['rango_millas'] = retraso_millas['distancia_millas'].apply(asignar_rango_millas)
    sin_retraso_millas['rango_millas'] = sin_retraso_millas['distancia_millas'].apply(asignar_rango_millas)

    retrasos_rango_millas = retraso_millas.groupby('rango_millas').size().reset_index(name='con_retraso')
    sin_retrasos_rango_millas = sin_retraso_millas.groupby('rango_millas').size().reset_index(name='sin_retraso')

    millas = retrasos_rango_millas.merge(sin_retrasos_rango_millas, on='rango_millas', how='outer').fillna(0)

    fig = px.bar(millas, 
                x='rango_millas', 
                y=['con_retraso', 'sin_retraso'], 
                title='Cantidad de vuelos con y sin retraso en la llegada según el recorrido del vuelo',
                labels={'rango_millas': 'Rango de millas', 'value': 'Cantidad de vuelos'},
                opacity=0.7, 
                color_discrete_map={"con_retraso": "tomato", "sin_retraso": "lightseagreen"})

    fig.update_layout(title_x=0.5, xaxis={'categoryorder': 'total descending'}, width=1080)

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
