# paginas/eda_2.py
import streamlit as st
from modules.botones_eda_2 import seleccionar_datos
from modules.botones_graficas import seleccionar_y_mostrar_grafica

def display():
    st.title('Exploración de Datos de Vuelos')

    # Muestra el texto centrado y la imagen si no se ha seleccionado una subpágina
    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h3 style='text-align: center;'>Seleccione un año para visualizar los datos</h3>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')
    
    # Dividir la interfaz en dos columnas
    col1, col2 = st.columns([1, 4])

    with col1:
        # Seleccionar los datos según el año desde el primer selector
        df_seleccionado = seleccionar_datos()

    with col2:
        # Si se ha seleccionado algún conjunto de datos, mostrar gráficas para ese conjunto
        if df_seleccionado is not None:
            seleccionar_y_mostrar_grafica(df_seleccionado)

# Llama a la función para mostrar la página
display()
