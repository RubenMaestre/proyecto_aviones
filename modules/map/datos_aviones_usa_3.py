import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa_3():
    df_todos = cargar_todos_df()

    # Extraer el día del mes de la columna 'fecha'
    df_todos['dia'] = df_todos['fecha'].dt.day

    # Definir los segmentos semanales para diciembre
    def asignar_segmento_semanal(dia):
        if 1 <= dia <= 10:
            return 'Primera Decena (1-10)'
        elif 11 <= dia <= 19:
            return 'Segunda Decena (11-19)'
        elif 20 <= dia <= 26:
            return 'Semana de Navidad (20-26)'
        else:  # del 27 al 31
            return 'Semana de Nochevieja (27-31)'

    # Aplicar la función para crear una nueva columna 'segmento_semanal' basada en el 'dia'
    df_todos['segmento_semanal'] = df_todos['dia'].apply(asignar_segmento_semanal)

    # Análisis de retrasos por segmento semanal
    retraso_por_segmento_semanal = df_todos.groupby('segmento_semanal')['retraso_salida'].mean().reset_index()
    retraso_por_segmento_semanal['Retraso Promedio de Salida (min)'] = retraso_por_segmento_semanal['retraso_salida'].round(2)
    retraso_por_segmento_semanal = retraso_por_segmento_semanal[['segmento_semanal', 'Retraso Promedio de Salida (min)']]

    # Otros análisis...

    # 1. Racha de puntualidad de aerolíneas - Pendiente de análisis detallado

    # 2. Comparación día laboral vs. fin de semana
    df_todos['es_fin_de_semana'] = df_todos['dia_semana'].apply(lambda x: x in [5, 6])
    vuelos_dia_laboral = df_todos[~df_todos['es_fin_de_semana']]['numero_vuelo'].count()
    vuelos_fin_de_semana = df_todos[df_todos['es_fin_de_semana']]['numero_vuelo'].count()
    retraso_promedio_dia_laboral = df_todos[~df_todos['es_fin_de_semana']]['retraso_salida'].mean()
    retraso_promedio_fin_de_semana = df_todos[df_todos['es_fin_de_semana']]['retraso_salida'].mean()

    # 3. Impacto de la distancia en el retraso
    correlacion_distancia_retraso = df_todos[['distancia_millas', 'retraso_salida']].corr().iloc[0, 1]

    # 4. Retraso promedio por segmento semanal - Sustituye el análisis de temporada

    # 5. Perfil del vuelo perfecto - Pendiente de análisis detallado

    # Crear un DataFrame para mostrar la información
    datos = {
        'Categoría': [
            'Racha de puntualidad de aerolíneas',
            'Vuelos y retrasos promedio (Día laboral vs. Fin de semana)',
            'Correlación entre distancia y retraso',
            'Retraso promedio por segmento semanal',
            'Perfil del vuelo perfecto'
        ],
        'Datos': [
            'Pendiente de análisis detallado',
            f"Día laboral: {vuelos_dia_laboral} vuelos, {retraso_promedio_dia_laboral:.2f} min de retraso promedio; Fin de semana: {vuelos_fin_de_semana} vuelos, {retraso_promedio_fin_de_semana:.2f} min de retraso promedio",
            f"Correlación: {correlacion_distancia_retraso:.2f}",
            f"{retraso_por_segmento_semanal.to_string(index=False)}",  # Mostrar los resultados del análisis semanal
            'Pendiente de análisis detallado'
        ]
    }

    df_datos = pd.DataFrame(datos)
    st.table(df_datos)
