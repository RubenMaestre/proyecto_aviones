import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea



def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_todos, 'fecha')

    # Llama a la función para mostrar la gráfica de vuelos por aerolínea
    graficar_vuelos_por_aerolinea(df_todos)

    # Todos años por aerolínea / evolución
    graficar_evolucion_vuelos_por_aerolinea(df_todos)