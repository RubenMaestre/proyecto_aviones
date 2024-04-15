# paginas/eda_2.py
import streamlit as st
from modules.botones_eda_2 import seleccionar_datos
from modules.botones_graficas import seleccionar_y_mostrar_grafica

def display():
    st.title('Exploración de Datos de Vuelos')

    # Muestra el texto centrado solo si no se ha seleccionado una subpágina
    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h3 style='text-align: center;'>Seleccione un año para visualizar los datos</h3>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')  

    # Seleccionar los datos según el año
    df_seleccionado = seleccionar_datos()

    # Seleccionar y mostrar la gráfica según el DataFrame cargado
    if df_seleccionado is not None:
        seleccionar_y_mostrar_grafica(df_seleccionado)

# Llama a la función para mostrar la página
display()
