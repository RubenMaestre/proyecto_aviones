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

def datos_aviones_usa_2():
    df_todos = cargar_todos_df()

    # Calcular los datos convencionales
    aerolinea_mas_vuelos = df_todos['aerolinea'].value_counts().idxmax()
    aerolinea_menos_vuelos = df_todos['aerolinea'].value_counts().idxmin()

    # Día de la semana con más tráfico aéreo
    dia_mas_trafico = df_todos['dia_semana'].value_counts().idxmax()
    dias_semana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
    dia_mas_trafico_nombre = dias_semana[dia_mas_trafico]

    # Ruta más transitada
    df_todos['ruta'] = df_todos['ciudad_origen'] + '-' + df_todos['ciudad_destino']
    ruta_mas_transitada = df_todos['ruta'].value_counts().idxmax()

    # Promedio de retraso por aerolínea
    promedio_retraso_aerolinea = df_todos.groupby('aerolinea')['retraso_salida'].mean().idxmax()

    # Vuelo más largo por duración
    vuelo_mas_largo = df_todos['duracion_programada_vuelo'].idxmax()

    # Mayor retraso debido al clima
    mayor_retraso_clima = df_todos['tiempo_retraso_clima'].idxmax()

    # Aeropuertos con más retrasos en seguridad
    mayor_retraso_seguridad = df_todos.groupby('aeropuerto_origen')['tiempo_retraso_seguridad'].sum().idxmax()

    # Festivos con más vuelos
    festivos_mas_vuelos = df_todos[df_todos['festivos'] == 1]['fecha'].value_counts().idxmax()

    # Renderizar los datos en columnas
    col1, col2 = st.columns(2)
    with col1:
        render_data('Aerolínea con más vuelos', f"{aerolinea_mas_vuelos} ({df_todos['aerolinea'].value_counts().max()} vuelos)")
        render_data('Día de la semana con más tráfico', dia_mas_trafico_nombre)
        render_data('Ruta más transitada', ruta_mas_transitada)
        render_data('Promedio de retraso por aerolínea', promedio_retraso_aerolinea)
        render_data('Vuelo más largo', f"{df_todos.loc[vuelo_mas_largo, 'aerolinea']} - Duración: {df_todos.loc[vuelo_mas_largo, 'duracion_programada_vuelo']} minutos")
    with col2:
        render_data('Aerolínea con menos vuelos', f"{aerolinea_menos_vuelos} ({df_todos['aerolinea'].value_counts().min()} vuelos)")
        render_data('Mayor retraso debido al clima', f"{df_todos.loc[mayor_retraso_clima, 'aerolinea']} - Retraso: {df_todos.loc[mayor_retraso_clima, 'tiempo_retraso_clima']} minutos")
        render_data('Aeropuertos con más retrasos en seguridad', mayor_retraso_seguridad)
        render_data('Festivos con más vuelos', f"{festivos_mas_vuelos.strftime('%d/%m/%Y')} ({df_todos[df_todos['festivos'] == 1]['fecha'].value_counts().max()} vuelos)")
