import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa_2():
    # Cargar todos los DataFrames
    df_todos = cargar_todos_df()

    # Calcular los datos convencionales
    aerolinea_mas_vuelos = df_todos['aerolinea'].value_counts().idxmax()
    aerolinea_menos_vuelos = df_todos['aerolinea'].value_counts().idxmin()

    dia_mas_salidas = df_todos['dia_semana'].value_counts().idxmax()
    mes_mas_actividad = df_todos['mes'].value_counts().idxmax()

    # Combinar ciudad origen-destino para identificar la ruta más transitada
    df_todos['ruta'] = df_todos['ciudad_origen'] + '-' + df_todos['ciudad_destino']
    ruta_mas_transitada = df_todos['ruta'].value_counts().idxmax()

    # Promedio de retraso por aerolínea
    promedio_retraso_aerolinea = df_todos.groupby('aerolinea')['retraso_salida'].mean().idxmax()

    # Vuelos más largo y más corto por duración
    vuelo_mas_largo = df_todos['duracion_programada_vuelo'].idxmax()
    vuelo_mas_corto = df_todos['duracion_programada_vuelo'].idxmin()

    # Mayor retraso debido al clima
    mayor_retraso_clima = df_todos['tiempo_retraso_clima'].idxmax()

    # Aeropuertos con más retrasos en seguridad
    mayor_retraso_seguridad = df_todos.groupby('aeropuerto_origen')['tiempo_retraso_seguridad'].sum().idxmax()

    # Festivos con más vuelos
    festivos_mas_vuelos = df_todos[df_todos['festivos'] == 1]['fecha'].value_counts().idxmax()

    # Crear un DataFrame para mostrar la información
    datos = {
        'Categoría': [
            'Aerolínea con más vuelos', 'Aerolínea con menos vuelos', 
            'Día de la semana con más salidas', 'Mes con más actividad', 
            'Ruta más transitada', 'Promedio de retraso por aerolínea', 
            'Vuelo más largo', 'Vuelo más corto', 'Mayor retraso debido al clima', 
            'Aeropuertos con más retrasos en seguridad', 'Festivos con más vuelos'
        ],
        'Datos': [
            f"{aerolinea_mas_vuelos} ({df_todos['aerolinea'].value_counts().max()} vuelos)",
            f"{aerolinea_menos_vuelos} ({df_todos['aerolinea'].value_counts().min()} vuelos)",
            f"{dia_mas_salidas}",
            f"{mes_mas_actividad}",
            f"{ruta_mas_transitada}",
            f"{promedio_retraso_aerolinea}",
            f"{df_todos.loc[vuelo_mas_largo, 'aerolinea']} - Duración: {df_todos.loc[vuelo_mas_largo, 'duracion_programada_vuelo']} minutos",
            f"{df_todos.loc[vuelo_mas_corto, 'aerolinea']} - Duración: {df_todos.loc[vuelo_mas_corto, 'duracion_programada_vuelo']} minutos",
            f"{df_todos.loc[mayor_retraso_clima, 'aerolinea']} - Retraso: {df_todos.loc[mayor_retraso_clima, 'tiempo_retraso_clima']} minutos",
            f"{mayor_retraso_seguridad}",
            f"{festivos_mas_vuelos.strftime('%d/%m/%Y')} ({df_todos[df_todos['festivos'] == 1]['fecha'].value_counts().max()} vuelos)"
        ]
    }

    df_datos = pd.DataFrame(datos)
    st.table(df_datos)