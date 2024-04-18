import streamlit as st
import pandas as pd
import plotly.express as px
from modules.graph.diccionario_estados import estados_EEUU 

def graficar_estados_menos_retrasos(df):
    # Aplicar el mapeo del diccionario para convertir códigos de estado a nombres completos
    df['estado_origen'] = df['estado_origen'].map(estados_EEUU).fillna(df['estado_origen'])

    # Calcular los retrasos
    retrasos_llegada = df[df['retraso_llegada'] > 15]
    retrasos_estados_origen = retrasos_llegada.groupby('estado_origen').size().reset_index(name='con_retraso')

    # Filtrar para obtener los 10 estados con menos retrasos
    top_estados_menos_retrasos = retrasos_estados_origen.nsmallest(10, 'con_retraso')

    # Crear la gráfica
    fig = px.bar(top_estados_menos_retrasos, 
                 x='estado_origen', 
                 y='con_retraso', 
                 title='Top 10 Estados con menos retrasos en la llegada',
                 labels={'estado_origen': 'Estado', 'con_retraso': 'Cantidad de retrasos'},
                 opacity=0.8, 
                 color_discrete_sequence=["green"])

    fig.update_layout(title_x=0.5, xaxis={'categoryorder': 'total descending'})

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)