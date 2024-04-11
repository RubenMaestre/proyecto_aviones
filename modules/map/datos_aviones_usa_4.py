import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa_4():
    df_todos = cargar_todos_df()

    # Antes de usar '.dt', asegúrate de que 'hora_salida_real' esté en formato datetime
    df_todos['hora_salida_real'] = pd.to_datetime(df_todos['hora_salida_real'])

    df_todos['hora_exacta_salida'] = df_todos['hora_salida_real'].apply(lambda x: x.minute == 0 if pd.notnull(x) else False)

    vuelo_cercano_hora = df_todos[df_todos['hora_exacta_salida']]['numero_vuelo'].value_counts().idxmax()

    # Aeropuerto 'leyenda urbana'
    numeros_suerte = ['777', '666']
    df_todos['suerte'] = df_todos['numero_vuelo'].astype(str).apply(lambda x: any(num in x for num in numeros_suerte))
    aeropuerto_leyenda_urbana = df_todos[df_todos['suerte']]['aeropuerto_origen'].value_counts().idxmax()

    # Viaje en el tiempo
    df_todos['discrepancia_duracion'] = abs(df_todos['duracion_real'] - df_todos['duracion_programada_vuelo'])
    dia_viaje_tiempo = df_todos.sort_values(by='discrepancia_duracion', ascending=False)['fecha'].iloc[0]

    # Análisis del 'Efecto Mariposa' y 'Desfile de modas' de aerolíneas - Pendientes

    datos = {
        'Categoría': [
            "Vuelo más 'cercano a la hora'",
            "Aeropuerto 'leyenda urbana'",
            "Viaje en el tiempo",
            "Análisis del 'Efecto Mariposa'",
            "'Desfile de modas' de aerolíneas"
        ],
        'Datos': [
            f"Vuelo {vuelo_cercano_hora}",
            f"Aeropuerto {aeropuerto_leyenda_urbana}",
            f"Día {dia_viaje_tiempo.strftime('%d/%m/%Y')}",
            "Requiere análisis detallado",
            "Pendiente de implementación"
        ]
    }

    df_datos = pd.DataFrame(datos)
    st.table(df_datos)