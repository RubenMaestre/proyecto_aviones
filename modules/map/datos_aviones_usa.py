import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa():
    # Cargar todos los DataFrames
    df_todos = cargar_todos_df()

    # Calcular los aeropuertos y ciudades/estados con más y menos salidas/llegadas
    aeropuerto_mas_salidas = df_todos['aeropuerto_origen'].value_counts().idxmax()
    aeropuerto_menos_salidas = df_todos['aeropuerto_origen'].value_counts().idxmin()
    aeropuerto_mas_llegadas = df_todos['aeropuerto_destino'].value_counts().idxmax()
    aeropuerto_menos_llegadas = df_todos['aeropuerto_destino'].value_counts().idxmin()

    estado_origen_mas_salidas = df_todos['estado_origen'].value_counts().idxmax()
    estado_origen_menos_salidas = df_todos['estado_origen'].value_counts().idxmin()
    estado_destino_mas_llegadas = df_todos['estado_destino'].value_counts().idxmax()
    estado_destino_menos_llegadas = df_todos['estado_destino'].value_counts().idxmin()

    ciudad_origen_mas_salidas = df_todos['ciudad_origen'].value_counts().idxmax()
    ciudad_origen_menos_salidas = df_todos['ciudad_origen'].value_counts().idxmin()
    ciudad_destino_mas_llegadas = df_todos['ciudad_destino'].value_counts().idxmax()
    ciudad_destino_menos_llegadas = df_todos['ciudad_destino'].value_counts().idxmin()

    # Crear un DataFrame para mostrar la información
    datos = {
        'Categoría': ['Aeropuerto con más salidas', 'Aeropuerto con menos salidas',
                      'Aeropuerto con más llegadas', 'Aeropuerto con menos llegadas',
                      'Estado origen con más salidas', 'Estado origen con menos salidas',
                      'Estado destino con más llegadas', 'Estado destino con menos llegadas',
                      'Ciudad origen con más salidas', 'Ciudad origen con menos salidas',
                      'Ciudad destino con más llegadas', 'Ciudad destino con menos llegadas'],
        'Datos': [aeropuerto_mas_salidas, aeropuerto_menos_salidas,
                  aeropuerto_mas_llegadas, aeropuerto_menos_llegadas,
                  estado_origen_mas_salidas, estado_origen_menos_salidas,
                  estado_destino_mas_llegadas, estado_destino_menos_llegadas,
                  ciudad_origen_mas_salidas, ciudad_origen_menos_salidas,
                  ciudad_destino_mas_llegadas, ciudad_destino_menos_llegadas]
    }

    df_datos = pd.DataFrame(datos)
    st.table(df_datos)