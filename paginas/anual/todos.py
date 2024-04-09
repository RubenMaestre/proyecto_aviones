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

    # Usamos st.columns para dividir la pantalla en dos columnas
    col1, col2 = st.columns(2)

    # En la primera columna, ponemos la gráfica de vuelos por aerolínea
    with col1:
        graficar_vuelos_por_aerolinea(df_todos)

    # En la segunda columna, ponemos la gráfica de evolución de vuelos por aerolínea
    with col2:
        graficar_evolucion_vuelos_por_aerolinea(df_todos)

    # Puedes seguir añadiendo más contenido debajo, si es necesario
