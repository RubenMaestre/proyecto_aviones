import streamlit as st
from modules.carga_dec_2022 import cargar_unir_2022 
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea


def display():
    st.title('Datos diciembre 2022')
    
    # Llama a la función para cargar el DataFrame de 2022
    df_dec_2022 = cargar_unir_2022()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_dec_2022, 'fecha')

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
        st.markdown("""
        ### Cantidad de vuelos nacionales por compañía aérea en Estados Unidos
        
        Esta gráfica muestra la distribución del número total de vuelos nacionales operados por diferentes compañías aéreas en Estados Unidos. Cada barra representa una aerolínea específica y la altura de la barra indica el número total de vuelos que esa aerolínea ha operado.
        
        Puedes utilizar esta información para identificar las aerolíneas con mayor y menor número de vuelos, lo que puede ser indicativo de su tamaño, alcance y actividad en el mercado de vuelos nacionales.
    """)

        # Llama a la función para mostrar la gráfica de vuelos por aerolínea
        graficar_vuelos_por_aerolinea(df_dec_2022)

        st.markdown("---")