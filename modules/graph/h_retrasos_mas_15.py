import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px

def graficar_retrasos_mas_15(df):
    # Contar vuelos con y sin retrasos en salida y llegada
    sin_retraso_salida = df[df['retraso_salida'] <= 15].shape[0]
    con_retraso_salida = df[df['retraso_salida'] > 15].shape[0]

    sin_retraso_llegada = df[df['retraso_llegada'] <= 15].shape[0]
    con_retraso_llegada = df[df['retraso_llegada'] > 15].shape[0]

    # Crear una figura con subplots
    fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=('Salidas', 'Llegadas'))

    # Añadir gráficos de pastel para salidas y llegadas
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_salida, con_retraso_salida]), 1, 1)
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_llegada, con_retraso_llegada]), 1, 2)

    # Actualizar el layout de la figura
    fig.update_layout(
        title_text="Porcentaje de Retrasos Superiores a 15 Minutos en los Vuelos",
        title_x=0.5,
        width=1080  # Establecer el ancho de la figura
    )

    # Personalizar las trazas de los gráficos de pastel
    fig.update_traces(pull=[0.05, 0.05], marker=dict(colors=px.colors.qualitative.Set2))

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)