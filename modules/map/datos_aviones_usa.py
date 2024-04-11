import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa():
    # Cargar todos los DataFrames
    df_todos = cargar_todos_df()
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

    estado_a_nombre_estado = df_aeropuertos_unicos.set_index('estado')['nombre_estado'].to_dict()


    # Calcular los aeropuertos y ciudades/estados con más y menos salidas/llegadas
    aeropuerto_mas_salidas = df_todos['aeropuerto_origen'].value_counts().idxmax()
    aeropuerto_menos_salidas = df_todos['aeropuerto_origen'].value_counts().idxmin()
    aeropuerto_mas_llegadas = df_todos['aeropuerto_destino'].value_counts().idxmax()
    aeropuerto_menos_llegadas = df_todos['aeropuerto_destino'].value_counts().idxmin()

    
    estado_origen_mas_salidas_abbr = df_todos['estado_origen'].value_counts().idxmax()
    estado_origen_mas_salidas_nombre = estado_a_nombre_estado.get(estado_origen_mas_salidas_abbr, "Desconocido")
    estado_origen_menos_salidas_abbr = df_todos['estado_origen'].value_counts().idxmin()
    estado_origen_menos_salidas_nombre = estado_a_nombre_estado.get(estado_origen_menos_salidas_abbr, "Desconocido")
    estado_destino_mas_llegadas_abbr = df_todos['estado_destino'].value_counts().idxmax()
    estado_destino_mas_llegadas_nombre = estado_a_nombre_estado.get(estado_destino_mas_llegadas_abbr, "Desconocido")
    estado_destino_menos_llegadas_abbr = df_todos['estado_destino'].value_counts().idxmin()
    estado_destino_menos_llegadas_nombre = estado_a_nombre_estado.get(estado_destino_menos_llegadas_abbr, "Desconocido")


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
        'Datos': [
            f"{aeropuerto_mas_salidas} ({df_todos['aeropuerto_origen'].value_counts().max()} salidas)",
            f"{aeropuerto_menos_salidas} ({df_todos['aeropuerto_origen'].value_counts().min()} salidas)",
            f"{aeropuerto_mas_llegadas} ({df_todos['aeropuerto_destino'].value_counts().max()} llegadas)",
            f"{aeropuerto_menos_llegadas} ({df_todos['aeropuerto_destino'].value_counts().min()} llegadas)",
            f"{estado_origen_mas_salidas_nombre} ({df_todos['estado_origen'].value_counts().max()} salidas)",
            f"{estado_origen_menos_salidas_nombre} ({df_todos['estado_origen'].value_counts().min()} salidas)",
            f"{estado_destino_mas_llegadas_nombre} ({df_todos['estado_destino'].value_counts().max()} llegadas)",
            f"{estado_destino_menos_llegadas_nombre} ({df_todos['estado_destino'].value_counts().min()} llegadas)",
            f"{ciudad_origen_mas_salidas} ({df_todos['ciudad_origen'].value_counts().max()} salidas)",
            f"{ciudad_origen_menos_salidas} ({df_todos['ciudad_origen'].value_counts().min()} salidas)",
            f"{ciudad_destino_mas_llegadas} ({df_todos['ciudad_destino'].value_counts().max()} llegadas)",
            f"{ciudad_destino_menos_llegadas} ({df_todos['ciudad_destino'].value_counts().min()} llegadas)"
        ]
    }

    print(df_todos['ciudad_origen'].value_counts())
    print(df_todos['ciudad_destino'].value_counts())
    df_datos = pd.DataFrame(datos)
    st.table(df_datos)