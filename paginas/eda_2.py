# paginas/eda_2.py
import streamlit as st
from modules.botones_eda_2 import seleccionar_datos
from modules.botones_graficas import seleccionar_grafica

def display():
    st.title('Exploración de Datos de Vuelos')

    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h3 style='text-align: center;'>Seleccione un año para visualizar los datos</h3>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')
    
    col1, col2 = st.columns([1, 4])

    with col1:
        df_seleccionado = seleccionar_datos()
        if df_seleccionado is not None:
            grafica_funcion = seleccionar_grafica()

    with col2:
        if df_seleccionado is not None and 'grafica_funcion' in locals():
            grafica_funcion(df_seleccionado)

display()
