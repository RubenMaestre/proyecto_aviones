import streamlit as st
import locale
from babel.dates import format_date

def mostrar_estadisticas_df(df, columna_fecha):
    # Intentar establecer el locale a español
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    except locale.Error:
        pass  # En caso de que el locale 'es_ES.UTF-8' no esté disponible

    total_datos = len(df)
    
    # Usar babel para formatear las fechas si el locale no se ha podido cambiar
    fecha_min = df[columna_fecha].min()
    fecha_max = df[columna_fecha].max()
    
    if 'locale' in locals() or 'locale' in globals():
        fecha_min_str = fecha_min.strftime('%d de %B de %Y')
        fecha_max_str = fecha_max.strftime('%d de %B de %Y')
    else:
        fecha_min_str = format_date(fecha_min, format='long', locale='es')
        fecha_max_str = format_date(fecha_max, format='long', locale='es')

    # Usamos st.columns para crear una tabla con 4 columnas de diferentes tamaños
    st.markdown("---")  # Línea horizontal como borde superior
    col1, col2, col3, col4 = st.columns([1, 3, 1, 3])

    with col1:
        st.write("Total datos:")

    with col2:
        # Usar markdown con HTML para personalizar el estilo
        st.markdown(f"<h3 style='text-align: left; color: black;'>{total_datos:,}</h3>", unsafe_allow_html=True)

    with col3:
        st.write("Fecha datos:")

    with col4:
        st.write(f"Del {fecha_min_str} al {fecha_max_str}")

    st.markdown("---")  # Línea horizontal como borde inferior

