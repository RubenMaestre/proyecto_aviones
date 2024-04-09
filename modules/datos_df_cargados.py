import streamlit as st

def mostrar_estadisticas_df(df, columna_fecha):
    total_datos = len(df)
    fecha_min = df[columna_fecha].min().strftime('%d de %B de %Y')
    fecha_max = df[columna_fecha].max().strftime('%d de %B de %Y')

    # Usamos st.columns para crear una tabla con 4 columnas de diferentes tamaños
    col1, col2, col3, col4 = st.columns([1, 3, 1, 3])

    with col1:
        st.write("Total datos:")

    with col2:
        st.write(total_datos)

    with col3:
        st.write("Fecha datos:")

    with col4:
        st.write(f"Del {fecha_min} al {fecha_max}")

    # Dibujar un borde alrededor de la "tabla"
    st.markdown("---")  # Esto crea una línea horizontal que actúa como borde inferior
