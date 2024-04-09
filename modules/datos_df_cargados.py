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

    st.markdown("---")
    col1, col2, col3, col4 = st.columns([1, 3, 1, 3])

    with col1:
        st.markdown(f"<h5 style='text-align: left;'>Total datos:</h4>", unsafe_allow_html=True)

    with col2:
        total_datos_str = f"{total_datos:,.0f}".replace(',', '.')
        total_datos_str += " vuelos nacionales en USA"
        st.markdown(f"<h5 style='text-align: left;'>{total_datos_str}</h4>", unsafe_allow_html=True)

    with col3:
        st.markdown(f"<h5 style='text-align: left;'>Fecha datos:</h4>", unsafe_allow_html=True)

    with col4:
        st.markdown(f"<h5 style='text-align: left;'>Del {fecha_min_str} al {fecha_max_str}</h4>", unsafe_allow_html=True)

    st.markdown("---")
