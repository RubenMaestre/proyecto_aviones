import streamlit as st
import pandas as pd
import plotly.express as px
from modules.graph.diccionario_estados import estados_EEUU  # Asegúrate de que la ruta de importación sea correcta

def graficar_estados_mas_retrasos(df):
    # Suponiendo que df ya tiene una columna 'estado_origen' con códigos de estado
    df['estado_origen'] = df['estado_origen'].map(estados_EEUU).fillna(df['estado_origen'])

    # Filtrado y cálculo como antes
    retrasos_estados_origen = df[df['retraso_llegada'] > 15].groupby('estado_origen').size().reset_index(name='con_retraso')
    top_estados_mas_retrasos = retrasos_estados_origen.nlargest(10, 'con_retraso')

    # Crear gráfica
    fig = px.bar(top_estados_mas_retrasos, 
                 x='estado_origen', 
                 y='con_retraso', 
                 title='Top 10 Estados con más retrasos en la llegada',
                 labels={'estado_origen': 'Estado', 'con_retraso': 'Cantidad de retrasos'},
                 opacity=0.8, 
                 color_discrete_sequence=["red"])

    fig.update_layout(title_x=0.5, xaxis={'categoryorder': 'total descending'})

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
