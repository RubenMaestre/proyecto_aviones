import pandas as pd
import streamlit as st
from modules.carga_todos_df import cargar_todos_df

def datos_aviones_usa_3():
    # Cargar todos los DataFrames
    df_todos = cargar_todos_df()

    # 1. Racha de puntualidad de aerolíneas
    # Este cálculo es bastante avanzado y podría requerir el uso de técnicas de análisis de series temporales o algoritmos específicos para identificar la racha más larga.
    
    # 2. Comparación día laboral vs. fin de semana
    df_todos['es_fin_de_semana'] = df_todos['dia_semana'].apply(lambda x: x in [5, 6])  # Asumiendo que 5 = Sábado y 6 = Domingo
    vuelos_dia_laboral = df_todos[~df_todos['es_fin_de_semana']]['numero_vuelo'].count()
    vuelos_fin_de_semana = df_todos[df_todos['es_fin_de_semana']]['numero_vuelo'].count()
    retraso_promedio_dia_laboral = df_todos[~df_todos['es_fin_de_semana']]['retraso_salida'].mean()
    retraso_promedio_fin_de_semana = df_todos[df_todos['es_fin_de_semana']]['retraso_salida'].mean()

    # 3. Impacto de la distancia en el retraso
    # Podría requerir análisis de correlación o regresión lineal.
    correlacion_distancia_retraso = df_todos[['distancia_millas', 'retraso_salida']].corr().iloc[0, 1]

    # 4. Análisis de retrasos por temporada
    # Asumiendo que ya tienes una columna 'temporada' o puedes crearla basándote en 'mes'
    retraso_por_temporada = df_todos.groupby('temporada')['retraso_salida'].mean()

    # 5. Perfil del vuelo perfecto
    # Podría requerir un análisis complejo para identificar combinaciones con cero retrasos o los retrasos mínimos.
    
    # Crear un DataFrame para mostrar la información
    datos = {
        'Categoría': [
            'Racha de puntualidad de aerolíneas',
            'Vuelos y retrasos promedio (Día laboral vs. Fin de semana)',
            'Correlación entre distancia y retraso',
            'Retraso promedio por temporada',
            'Perfil del vuelo perfecto'
        ],
        'Datos': [
            'Pendiente de análisis detallado',
            f"Día laboral: {vuelos_dia_laboral} vuelos, {retraso_promedio_dia_laboral:.2f} min de retraso promedio; Fin de semana: {vuelos_fin_de_semana} vuelos, {retraso_promedio_fin_de_semana:.2f} min de retraso promedio",
            f"Correlación: {correlacion_distancia_retraso:.2f}",
            f"Pendiente de análisis estacional",
            'Pendiente de análisis detallado'
        ]
    }

    df_datos = pd.DataFrame(datos)
    st.table(df_datos)

# Llamar a la función en Streamlit
datos_aviones_usa_3()
