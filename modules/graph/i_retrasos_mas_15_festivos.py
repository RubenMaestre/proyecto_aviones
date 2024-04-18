import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px

def graficar_retrasos_mas_15_festivos(df):
    # Contar vuelos con y sin retrasos en salida y llegada, distinguiendo entre días laborables y festivos
    salidas_laborables  = df[(df['retraso_salida'] <= 15) & (df['festivos'] == 0)].shape[0]
    salidas_festivos    = df[(df['retraso_salida'] <= 15) & (df['festivos'] == 1)].shape[0]
    llegadas_laborables = df[(df['retraso_llegada'] <= 15) & (df['festivos'] == 0)].shape[0]
    llegadas_festivos   = df[(df['retraso_llegada'] <= 15) & (df['festivos'] == 1)].shape[0]

    # Crear una figura con 4 subplots
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Salidas en días laborables", "Salidas en días festivos", "Llegadas en días laborables", "Llegadas en días festivos"),
                        specs=[[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]])

    # Añadir gráficos de pastel para cada condición
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[salidas_laborables, df.shape[0] - salidas_laborables]), 1, 1)
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[salidas_festivos, df.shape[0] - salidas_festivos]), 1, 2)
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[llegadas_laborables, df.shape[0] - llegadas_laborables]), 2, 1)
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[llegadas_festivos, df.shape[0] - llegadas_festivos]), 2, 2)

    # Actualizar el layout de la figura
    fig.update_layout(
        title_text="Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en Días Festivos",
        title_x=0.5,
        width=1000,
        height=800
    )

    # Personalizar las trazas de los gráficos de pastel
    fig.update_traces(pull=[0.05, 0.05], marker=dict(colors=px.colors.qualitative.Set3), rotation=60)

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
