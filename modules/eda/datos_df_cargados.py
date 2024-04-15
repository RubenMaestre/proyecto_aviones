# modules/datos_df_cargados.py
import streamlit as st
import locale
from babel.dates import format_date

def mostrar_estadisticas_df(df, columna_fecha):
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    except locale.Error:
        pass  # En caso de que el locale 'es_ES.UTF-8' no esté disponible

    total_datos = len(df)
    fecha_min = df[columna_fecha].min()
    fecha_max = df[columna_fecha].max()

    if 'locale' in locals() or 'locale' in globals():
        fecha_min_str = fecha_min.strftime('%d de %B de %Y')
        fecha_max_str = fecha_max.strftime('%d de %B de %Y')
    else:
        fecha_min_str = format_date(fecha_min, format='long', locale='es')
        fecha_max_str = format_date(fecha_max, format='long', locale='es')

    st.markdown(f"**Total de datos:** {total_datos:,d} vuelos nacionales en USA")
    st.markdown(f"**Fechas de datos:** Del {fecha_min_str} al {fecha_max_str}")
