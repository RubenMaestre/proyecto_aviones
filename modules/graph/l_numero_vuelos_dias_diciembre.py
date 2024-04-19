import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

def graficar_numero_vuelos_dias_diciembre(df):
    df_fechas = df.groupby(['anio', 'fecha']).size().reset_index(name='numero_vuelos')

    # Crear gráficos de línea para cada año
    fig1 = px.line(df_fechas[df_fechas['anio'] == 2021], x='fecha', y='numero_vuelos', color_discrete_sequence=['skyblue'])
    fig2 = px.line(df_fechas[df_fechas['anio'] == 2022], x='fecha', y='numero_vuelos', color_discrete_sequence=['violet'])
    fig3 = px.line(df_fechas[df_fechas['anio'] == 2023], x='fecha', y='numero_vuelos', color_discrete_sequence=['springgreen'])

    # Combinar los gráficos en un solo gráfico con subplots
    fig = make_subplots(
        rows=1,  # Tres filas
        cols=3,  # Una columna
        subplot_titles=('2021', '2022', '2023'),
        vertical_spacing=0.1  # Ajustar el espaciado vertical
    )

    # Añadir cada gráfico a su respectiva fila
    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=2, col=1)
    fig.add_trace(fig3.data[0], row=3, col=1)

    # Actualizar ejes y layout
    fig.update_xaxes(title_text='Fecha', row=1, col=1)
    fig.update_xaxes(title_text='Fecha', row=2, col=1)
    fig.update_xaxes(title_text='Fecha', row=3, col=1)

    fig.update_yaxes(title_text='Número de vuelos', row=1, col=1)
    fig.update_yaxes(title_text='Número de vuelos', row=2, col=1)
    fig.update_yaxes(title_text='Número de vuelos', row=3, col=1)

    fig.update_layout(
        title_text='Número de vuelos por días en Diciembre por Año',
        title_x=0.5,
        width=1080,
        height=1200  # Ajusta la altura para acomodar los tres gráficos
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

