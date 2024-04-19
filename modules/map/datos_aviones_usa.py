import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa():
    # Cargar todos los DataFrames
    df_todos = cargar_todos_df()
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

    # Código para calcular los datos aquí...

    # Agrupar aeropuertos y estados según las especificaciones
    trafico_aeropuerto = df_todos['aeropuerto_origen'].value_counts() + df_todos['aeropuerto_destino'].value_counts()
    aeropuerto_mas_trafico = trafico_aeropuerto.idxmax()
    aeropuerto_menos_trafico = trafico_aeropuerto.idxmin()

    trafico_estado_origen = df_todos['estado_origen'].value_counts() + df_todos['estado_destino'].value_counts()
    estado_mas_trafico = trafico_estado_origen.idxmax()
    estado_menos_trafico = trafico_estado_origen.idxmin()

    # Suponiendo que las ciudades están de manera similar en tus datos
    trafico_ciudad_origen = df_todos['ciudad_origen'].value_counts() + df_todos['ciudad_destino'].value_counts()
    ciudad_mas_trafico = trafico_ciudad_origen.idxmax()
    ciudad_menos_trafico = trafico_ciudad_origen.idxmin()

    # Renderizar los datos
    col1, col2 = st.columns(2)
    with col1:
        render_data('Aeropuerto con más tráfico aéreo', aeropuerto_mas_trafico)
        render_data('Estado con más tráfico aéreo', estado_mas_trafico)
        render_data('Ciudad con más tráfico aéreo', ciudad_mas_trafico)
    with col2:
        render_data('Aeropuerto con menos tráfico aéreo', aeropuerto_menos_trafico)
        render_data('Estado con menos tráfico aéreo', estado_menos_trafico)
        render_data('Ciudad con menos tráfico aéreo', ciudad_menos_trafico)

    