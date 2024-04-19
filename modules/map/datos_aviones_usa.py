import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def render_data(title, value, note=""):
    column_style = """
    <style>
    .data-column {{
        border: 2px solid #CCCCCC;  /* Grosor y color del borde */
        border-radius: 10px;  /* Bordes redondeados */
        padding: 20px;  /* Espaciado interno */
        text-align: center;  /* Alineación del texto */
        margin-bottom: 20px;  /* Espacio debajo de cada bloque */
    }}
    .note {{
        font-size: small;  /* Tamaño de la fuente más pequeño para la nota */
        color: #555555;  /* Color gris para la nota */
    }}
    </style>
    <div class='data-column'>
        <h4>{title}</h4>
        <h1>{value}</h1>
        {note}
    </div>
    """.format(title=title, value=value, note=note)
    st.markdown(column_style, unsafe_allow_html=True)

def datos_aviones_usa():
    df_todos = cargar_todos_df()
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')
    estado_a_nombre_estado = df_aeropuertos_unicos.set_index('estado')['nombre_estado'].to_dict()

    # Optimización: Calcular conteos una sola vez y reutilizarlos
    conteo_origen = df_todos['aeropuerto_origen'].value_counts()
    conteo_destino = df_todos['aeropuerto_destino'].value_counts()
    trafico_aeropuerto = conteo_origen.add(conteo_destino, fill_value=0)

    conteo_estado_origen = df_todos['estado_origen'].value_counts()
    conteo_estado_destino = df_todos['estado_destino'].value_counts()
    trafico_estado = conteo_estado_origen.add(conteo_estado_destino, fill_value=0)

    # Obtención de datos específicos
    aeropuerto_mas_trafico = trafico_aeropuerto.idxmax()
    aeropuerto_menos_trafico = trafico_aeropuerto.idxmin()
    estado_mas_trafico = trafico_estado.idxmax()
    estado_menos_trafico = trafico_estado.idxmin()

    # Renderizar los datos en columnas
    col1, col2 = st.columns(2)
    with col1:
        render_data('Aeropuerto con más tráfico aéreo', aeropuerto_mas_trafico)
        render_data('Estado con más tráfico aéreo', estado_mas_trafico)
    with col2:
        render_data('Aeropuerto con menos tráfico aéreo', aeropuerto_menos_trafico)
        render_data('Estado con menos tráfico aéreo', estado_menos_trafico)
