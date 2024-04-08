# paginas/eda.py
import streamlit as st
from modules.botones_eda import crear_botones_eda  # Importa la función de botones

# Importa las funciones display de cada año y TODOS
from paginas.anual.todos import display as display_todos
from paginas.anual.dec_2023 import display as display_2023
from paginas.anual.dec_2022 import display as display_2022
from paginas.anual.dec_2021 import display as display_2021

from modules.pickles import unir_pickles

if st.button('Pulse aquí para cargar datos'):
    generador_df = unir_pickles()  # Obtiene el generador
    try:
        while True:  # Este bucle seguirá intentando obtener DataFrames del generador
            df_vuelos_limpio = next(generador_df)  # Obtiene el próximo DataFrame
            st.write(df_vuelos_limpio)  # Muestra el DataFrame actual
            st.text("Cargando más datos...")  # Mensaje de carga (puedes quitarlo si no lo necesitas)
    except StopIteration:
        st.success('Todos los datos han sido cargados.')

def display():
    st.title('Exploración de Datos de Vuelos')

    # Llama a la función para mostrar los botones de navegación
    crear_botones_eda()

    # Muestra el texto centrado solo si no se ha seleccionado una subpágina
    if 'subpagina_eda' not in st.session_state or st.session_state.subpagina_eda is None:
        st.markdown("<h3 style='text-align: center;'>Seleccione un año para visualizar los datos</h3>", unsafe_allow_html=True)

    # Navegación interna basada en el estado de la sesión
    if 'subpagina_eda' in st.session_state:
        if st.session_state.subpagina_eda == 'todos':
            # Llama a la función para mostrar los datos de TODOS los años
            display_todos()
        elif st.session_state.subpagina_eda == '2023':
            # Llama a la función para mostrar los datos del año 2023
            display_2023()
        elif st.session_state.subpagina_eda == '2022':
            # Llama a la función para mostrar los datos del año 2022
            display_2022()
        elif st.session_state.subpagina_eda == '2021':
            # Llama a la función para mostrar los datos del año 2021
            display_2021()

# Llama a la función para mostrar la página
display()

