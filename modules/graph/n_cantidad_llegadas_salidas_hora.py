import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def graficar_cantidad_llegadas_salidas_por_hora(df):
    llegada_salida = pd.DataFrame()
    llegada_salida[['hora_salida_real', 'hora_llegada_real']] = df[['hora_salida_real', 'hora_llegada_real']]

    def asignar_rango(hora):
        if hora.hour < 6:
            return "00:00 - 05:59"
        elif hora.hour < 12:
            return "06:00 - 11:59"
        elif hora.hour < 18:
            return "12:00 - 17:59"
        else:
            return "18:00 - 23:59"
    
    llegada_salida['rango_salida'] = llegada_salida['hora_salida_real'].apply(asignar_rango)
    llegada_salida['rango_llegada'] = llegada_salida['hora_llegada_real'].apply(asignar_rango)

    salida_counts = llegada_salida['rango_salida'].value_counts().reindex(["00:00 - 05:59", "06:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"], fill_value=0)
    llegada_counts = llegada_salida['rango_llegada'].value_counts().reindex(["00:00 - 05:59", "06:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"], fill_value=0)

    index = np.arange(len(salida_counts))
    bar_width = 0.35

    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Bar(x=index, y=salida_counts, name='Rango de Salida', marker_color='skyblue', width=bar_width), row=1, col=1)
    fig.add_trace(go.Bar(x=index + bar_width, y=llegada_counts, name='Rango de Llegada', marker_color='salmon', width=bar_width), row=1, col=1)

    fig.update_layout(
        title_text='Cantidad de llegadas/salidas por rangos horarios',
        xaxis=dict(title='Rango horario', tickvals=index + bar_width / 2, ticktext=salida_counts.index),
        yaxis=dict(title='Cantidad de llegadas/salidas'),
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(205, 223, 212, 0.4)', bordercolor='rgba(0, 0, 0, 0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        width=1080,
        height=600
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

