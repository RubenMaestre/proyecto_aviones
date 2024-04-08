# paginas/eda.py
import streamlit as st
from modules.botones_eda import crear_botones_eda  # Importa la función de botones
from modules.cargar_unir_df import unir_dataframes_pickle  # Asume que esta es la ubicación de tu función

# Importa las funciones display de cada año y TODOS
from paginas.anual.todos import display as display_todos
from paginas.anual.dec_2023 import display as display_2023
from paginas.anual.dec_2022 import display as display_2022
from paginas.anual.dec_2021 import display as display_2021

def display():
    st.title('Exploración de Datos de Vuelos')

    # Llamada a la función para cargar y unir los DataFrames pickle
    directorio_pickle = 'data/pickles'  # Asegúrate de que esta sea la ruta correcta
    df_vuelos_limpio = unir_dataframes_pickle(directorio_pickle)

    # Llama a la función para mostrar los botones de navegación
    crear_botones_eda()

    # Muestra el texto centrado solo si no se ha seleccionado una subpágina
    if 'subpagina_eda' not in st.session_state or st.session_state.subpagina_eda is None:
        st.markdown("<h3 style='text-align: center;'>Seleccione un año para visualizar los datos</h3>", unsafe_allow_html=True)

    # Navegación interna basada en el estado de la sesión
    if 'subpagina_eda' in st.session_state:
        if st.session_state.subpagina_eda == 'todos':
            display_todos()
        elif st.session_state.subpagina_eda == '2023':
            display_2023()
        elif st.session_state.subpagina_eda == '2022':
            display_2022()
        elif st.session_state.subpagina_eda == '2021':
            display_2021()

# Llama a la función para mostrar la página
display()
