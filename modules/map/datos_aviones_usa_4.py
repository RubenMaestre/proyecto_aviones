import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa_4():
    df_todos = cargar_todos_df()

    # Si 'hora_salida_real' es una cadena con formato de hora, conviértela a datetime.time
    # Asegúrate de ajustar el formato '%H:%M' si tus datos tienen un formato diferente
    if df_todos['hora_salida_real'].dtype == 'O':  # 'O' para objetos, usualmente cadenas
        df_todos['hora_salida_real'] = pd.to_datetime(df_todos['hora_salida_real'], format='%H:%M').dt.time

    # Verifica si la hora de salida es exactamente a la hora (minutos = 0)
    df_todos['hora_exacta_salida'] = df_todos['hora_salida_real'].apply(lambda x: x.minute == 0 if pd.notnull(x) else False)

    # Continúa con el resto del análisis
    vuelo_cercano_hora = df_todos[df_todos['hora_exacta_salida']]['numero_vuelo'].value_counts().idxmax()

    # Aeropuerto 'leyenda urbana', 'Viaje en el tiempo', etc.
    ...

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
