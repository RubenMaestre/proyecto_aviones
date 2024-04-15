import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

from modules.map.mapa_aeropuertos import mostrar_mapa_aeropuertos_globales
from modules.map.estados_usa import mostrar_mapa_aeropuertos_usa
from modules.map.selector_estado import mostrar_mapa_aeropuertos_por_estado
from modules.map.selector_estado_interactivo import mostrar_mapa_aeropuertos_por_estado_interactivo



# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Mapas con todos los aeropuertos en Estados Unidos, incluídos territorios no incorporados')
    # Aquí iría el resto de tu contenido de la página de inicio
    
    st.markdown("""
            #### El mapa tiene un zoom enorme para que pueda abarcar todos los aeropuertos que de alguna forma pertenecen a Estados Unidos. Puede hacer zoom para visualizar mejor por zonas.""")
    
    mostrar_mapa_aeropuertos_globales()

    st.markdown("---")

    st.markdown("""
                ### Selecciona un estado para ver los aeropuertos que contiene""")
    st.write("En este mapa puede ver la cantidad de aeropuertos que hay por estado. Por ello le rogamos que seleccione uno de los 50 estados, el distrito federal, estados asociados o no incorporados.")

    mostrar_mapa_aeropuertos_por_estado()

    st.markdown("---")




