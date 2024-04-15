# paginas/eda_2.py
import streamlit as st
import plotly.express as px
from modules.botones_eda_2 import seleccionar_datos

def display():
    st.title('Exploración de Datos de Vuelos')

    # Llama a la función para mostrar los botones de navegación
    seleccionar_datos()

    # Muestra el texto centrado solo si no se ha seleccionado una subpágina
    if 'subpagina_eda' not in st.session_state or st.session_state.subpagina_eda is None:
        st.markdown("<h3 style='text-align: center;'>Seleccione un año para visualizar los datos</h3>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')  
        
   
# Llama a la función para mostrar la página
display()

