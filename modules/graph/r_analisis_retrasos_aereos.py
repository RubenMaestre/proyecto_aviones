import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px

def graficar_analisis_retrasos_aereos(df):
    tipos_retrasos = df[['tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion', 'tiempo_retraso_seguridad']]
    
    porcentaje_por_columna = tipos_retrasos.sum() / tipos_retrasos.sum().sum() * 100  # Calcular el porcentaje de cada tipo de retraso.
    valores_no_cero = tipos_retrasos.astype(bool).sum(axis=0)  # Calcular el número de veces que ocurre cada tipo de retraso.

    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=("Tiempo de retraso acumulados", "Porcentaje de retrasos"),
                        specs=[[{'type': 'domain'}, {'type': 'domain'}]])

    fig.add_trace(go.Pie(labels=porcentaje_por_columna.index, values=porcentaje_por_columna.values, name="Tiempo acumulado"), row=1, col=1)
    fig.add_trace(go.Pie(labels=valores_no_cero.index, values=valores_no_cero.values, name="Cantidad de ocurrencias"), row=1, col=2)

    fig.update_layout(
        title_text='Análisis de Retrasos Aéreos',
        title_x=0.5,
        width=1080,
        height=600
    )

    fig.update_traces(pull=[0.05, 0.05], marker=dict(colors=px.colors.qualitative.Set3))

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
