import itertools
import streamlit as st

def mostrar_correlaciones_significativas(df):
    # Selecciona solo las columnas numéricas deseadas
    columnas_numericas = ['numero_vuelo', 'duracion_programada_vuelo', 'duracion_real', 'retraso_salida', 'tiempo_pista_salida',
                          'tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion',
                          'tiempo_retraso_seguridad', 'retraso_llegada', 'dia_semana', 'anio', 'fin_de_semana', 'festivos']

    # Calcular y mostrar las correlaciones
    st.write("Correlaciones significativas (r >= 0.5):")
    for i, j in itertools.combinations(columnas_numericas, 2):
        corr_columnas = df[i].corr(df[j], method='pearson')
        if corr_columnas >= 0.5:
            st.write(f"Correlación entre {i} y {j}: {corr_columnas:.2f}")