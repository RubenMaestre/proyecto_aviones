import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

def graficar_cantidad_retrasos_por_hora(df):
    # Preprocesamiento de datos
    def asignar_rango(hora):
        if hora.hour < 6:
            return "00:00 - 05:59"
        elif hora.hour < 12:
            return "06:00 - 11:59"
        elif hora.hour < 18:
            return "12:00 - 17:59"
        else:
            return "18:00 - 23:59"

    df['rango_salida'] = df['hora_salida_real'].apply(asignar_rango)
    df['rango_llegada'] = df['hora_llegada_real'].apply(asignar_rango)
    df['retraso'] = df['retraso_llegada'].apply(lambda x: 1 if x > 15 else 0)

    # Agrupación y recuento de retrasos
    salida_retrasos = df.groupby('rango_salida')['retraso'].sum().reindex(["00:00 - 05:59", "06:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"], fill_value=0).reset_index()
    llegada_retrasos = df.groupby('rango_llegada')['retraso'].sum().reindex(["00:00 - 05:59", "06:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"], fill_value=0).reset_index()

    # Creación de gráficas
    fig1 = px.bar(salida_retrasos, x='rango_salida', y='retraso', title='Retrasos por Rango de Salida', opacity=0.7)
    fig2 = px.bar(llegada_retrasos, x='rango_llegada', y='retraso', title='Retrasos por Rango de Llegada', opacity=0.7)

    # Actualizar ejes y títulos
    fig1.update_xaxes(title_text='Rango de Salida')
    fig1.update_yaxes(title_text='Cantidad de Retrasos')
    fig2.update_xaxes(title_text='Rango de Llegada')
    fig2.update_yaxes(title_text='Cantidad de Retrasos')

    # Combinar gráficas en subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Retrasos por Rango de Salida', 'Retrasos por Rango de Llegada'))
    fig.add_trace(fig1['data'][0], row=1, col=1)
    fig.add_trace(fig2['data'][0], row=1, col=2)

    # Configurar el layout general
    fig.update_layout(title_text='Análisis de Retrasos por Rangos Horarios', title_x=0.5)

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)