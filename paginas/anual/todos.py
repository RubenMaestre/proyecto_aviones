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

    st.markdown("""
    ### Cantidad de vuelos nacionales por compañía aérea en Estados Unidos
    
    Esta gráfica muestra la distribución del número total de vuelos nacionales operados por diferentes compañías aéreas en Estados Unidos. Cada barra representa una aerolínea específica y la altura de la barra indica el número total de vuelos que esa aerolínea ha operado.
    
    Puedes utilizar esta información para identificar las aerolíneas con mayor y menor número de vuelos, lo que puede ser indicativo de su tamaño, alcance y actividad en el mercado de vuelos nacionales.
""")

    # Llama a la función para mostrar la gráfica de vuelos por aerolínea
    graficar_vuelos_por_aerolinea(df_todos)

    st.markdown("---")

    st.markdown("""
    ### Evolución del número de vuelos por compañía aérea
    
    Esta visualización muestra cómo ha evolucionado el número de vuelos de cada compañía aérea a lo largo de los años 2021, 2022 y 2023. Cada línea representa una aerolínea diferente, y los puntos en la línea indican el número de vuelos operados en un año específico.
    
    Esta gráfica te permite observar tendencias a lo largo del tiempo, como el crecimiento o la disminución en el número de vuelos de una aerolínea, lo que puede reflejar cambios en su operativa, expansión del mercado o respuesta a la demanda de vuelos nacionales.
""")

    # Todos años por aerolínea / evolución
    graficar_evolucion_vuelos_por_aerolinea(df_todos)

    st.markdown("---")