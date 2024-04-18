import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_estados_menos_retrasos(df):
    # Calculo de retrasos
    retrasos_llegada = df[df['retraso_llegada'] > 15]
    retrasos_estados_origen = retrasos_llegada.groupby(['estado_origen']).size().reset_index(name='con_retraso')

    # Filtrado para obtener los 10 estados con menos retrasos
    top_estados_menos_retrasos = retrasos_estados_origen.nsmallest(10, 'con_retraso')

    # Gráfica
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