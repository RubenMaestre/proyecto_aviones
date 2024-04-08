# paginas/eda.py
import streamlit as st
import plotly.express as px
from modules.botones_eda import crear_botones_eda  # Importa la función de botones

# Importa las funciones display de cada año y TODOS
from paginas.anual.todos import display as display_todos
from paginas.anual.dec_2023 import display as display_2023
from paginas.anual.dec_2022 import display as display_2022
from paginas.anual.dec_2021 import display as display_2021

from modules.pickles import unir_pickles

def display():
    st.title('Exploración de Datos de Vuelos')

    # Llama a la función para mostrar los botones de navegación
    crear_botones_eda()

    if st.button('Pulse aquí para cargar datos'):
        barra_progreso = st.progress(0)
        total_filas_texto = st.empty()  # Prepara un contenedor vacío para el texto

        generador_df = unir_pickles()  # Obtiene el generador
        for df_vuelos_limpio, porcentaje, total_filas in generador_df:
            barra_progreso.progress(porcentaje)  # Actualiza la barra de progreso
            total_filas_texto.write(f'Total de filas cargadas: {total_filas}')  # Actualiza el texto de filas cargadas

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

    st.success('Todos los datos han sido cargados.')
    total_filas_texto.empty()  # Limpia el texto de filas cargadas

    # Una vez cargados todos los datos, crea y muestra la gráfica
    vuelos_anuales = df_vuelos_limpio.groupby(['anio']).size().reset_index(name ='cantidad_vuelos_anuales')
    fig = px.bar(data_frame=vuelos_anuales, x='anio', y='cantidad_vuelos_anuales', opacity=0.8,
                     title="Cantidad de Vuelos Anuales", color='anio')
    fig.update_layout(title_x=0.5, xaxis_title='Año', yaxis_title='Cantidad de Vuelos', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)
    
# Llama a la función para mostrar la página
display()

