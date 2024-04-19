# paginas/vuelos/datos.py
import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.map.datos_aviones_usa import datos_aviones_usa
from modules.map.datos_aviones_usa_2 import datos_aviones_usa_2
#from modules.map.datos_aviones_usa_3 import datos_aviones_usa_3
#from modules.map.datos_aviones_usa_4 import datos_aviones_usa_4



def display():
    st.title('Datos y curiosidades sobre distancias')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    datos_aviones_usa()
    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
    
        

        st.markdown("---")

        datos_aviones_usa_2()

        st.markdown("---")

        #datos_aviones_usa_3()

        st.markdown("---")

        #datos_aviones_usa_4()

        st.markdown("---")
        