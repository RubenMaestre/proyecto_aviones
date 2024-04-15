# paginas/eda_2.py
import streamlit as st
from modules.botones_eda_2 import seleccionar_datos
from modules.botones_graficas import seleccionar_grafica

def display():
    st.title('Página de análisis exploratorio de datos (EDA)')

    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h3 style='text-align: center;'>En esta sección de nuestro proyecto podrás encontrar un análisis de los datos empleados a través de gráficos y visualizaciones para explorar y analizar el conjunto de los datos</h3>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')
    
    col1, col2 = st.columns([1, 4])

    with col1:
        st.write("Puedes seleccionar el mes de diciembre de los años 2021, 2022 y 2023, o bien elegir todos los años para ver todos los datos juntos.")
        df_seleccionado = seleccionar_datos()
        if df_seleccionado is not None:
            st.write("Una vez que has elegido el año, ahora puedes elegir qué tipo de gráfica ver.")
            grafica_funcion = seleccionar_grafica()

    with col2:
        if df_seleccionado is not None and grafica_funcion is not None:
            grafica_funcion(df_seleccionado)

display()
