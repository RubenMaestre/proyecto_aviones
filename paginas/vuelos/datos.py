# paginas/vuelos/datos.py
import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.map.datos_aviones_usa import datos_aviones_usa



def display():
    st.title('Datos y curiosidades sobre distancias')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
    
        datos_aviones_usa()

        st.markdown("---")

        