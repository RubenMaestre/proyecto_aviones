import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

def graficar_numero_vuelos_acumulados_diciembre(df):
    df_fechas = df.groupby(['anio', 'fecha']).size().reset_index(name='numero_vuelos')
    df_fechas['vuelos_acumulativo'] = df_fechas.groupby('anio')['numero_vuelos'].cumsum()

    # Crear gráficos de línea para cada año
    fig1 = px.line(df_fechas[df_fechas['anio'] == 2021], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['skyblue'])
    fig2 = px.line(df_fechas[df_fechas['anio'] == 2022], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['violet'])
    fig3 = px.line(df_fechas[df_fechas['anio'] == 2023], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['springgreen'])

    # Combinar los gráficos en un solo gráfico con subplots de 2 filas y 2 columnas
    fig = make_subplots(rows=2, cols=2, subplot_titles=('2021', '2022', '2023', 'Todos los Años'))

    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=1, col=2)
    fig.add_trace(fig3.data[0], row=2, col=1)

    # Añadir el gráfico combinado de todos los años en el cuarto subplot
    for anio, color in zip([2021, 2022, 2023], ['skyblue', 'violet', 'springgreen']):
        fig.add_trace(
            px.line(df_fechas[df_fechas['anio'] == anio], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=[color]).data[0],
            row=2, col=2
        )

    # Actualizar ejes y layout
    for n in range(1, 3):
        fig.update_xaxes(title_text='Fecha', row=1, col=n)
        fig.update_xaxes(title_text='Fecha', row=2, col=n)

    fig.update_yaxes(title_text='Número de vuelos acumulados', row=1, col=1)
    fig.update_yaxes(title_text='Número de vuelos acumulados', row=2, col=1)
    fig.update_layout(
        title_text='Número de vuelos acumulados por día en Diciembre por Año',
        title_x=0.5,
        width=1080,
        height=800  # Ajusta la altura para acomodar las 2 filas de gráficos
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
