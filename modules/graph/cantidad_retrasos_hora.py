import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def graficar_cantidad_retrasos_por_hora(df):
    llegada_salida_retrasos = df[['hora_salida_real', 'hora_llegada_real', 'retraso_llegada']].copy()

    def asignar_rango(hora):
        if hora.hour < 6:
            return "00:00 - 05:59"
        elif hora.hour < 12:
            return "06:00 - 11:59"
        elif hora.hour < 18:
            return "12:00 - 17:59"
        else:
            return "18:00 - 23:59"
    
    llegada_salida_retrasos['rango_salida'] = llegada_salida_retrasos['hora_salida_real'].apply(asignar_rango)
    llegada_salida_retrasos['rango_llegada'] = llegada_salida_retrasos['hora_llegada_real'].apply(asignar_rango)
    llegada_salida_retrasos['retraso'] = llegada_salida_retrasos['retraso_llegada'].apply(lambda x: 1 if x > 15 else 0)

    salida_retrasos = llegada_salida_retrasos.groupby('rango_salida')['retraso'].sum().reindex(["00:00 - 05:59", "06:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"], fill_value=0)
    llegada_retrasos = llegada_salida_retrasos.groupby('rango_llegada')['retraso'].sum().reindex(["00:00 - 05:59", "06:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"], fill_value=0)

    index = range(len(salida_retrasos))
    bar_width = 0.35

    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Bar(x=index, y=salida_retrasos, name='Rango de Salida', marker_color='skyblue', width=bar_width), row=1, col=1)
    fig.add_trace(go.Bar(x=[i + bar_width for i in index], y=llegada_retrasos, name='Rango de Llegada', marker_color='salmon', width=bar_width), row=1, col=1)

    fig.update_layout(
        title_text='Cantidad de retrasos en llegadas/salidas por rangos horarios',
        xaxis=dict(title='Rango horario', tickvals=[i + bar_width / 2 for i in index], ticktext=salida_retrasos.index),
        yaxis=dict(title='Cantidad de retrasos'),
        legend=dict(x=0.01, y=0.99),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        width=1080,
        height=600
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
