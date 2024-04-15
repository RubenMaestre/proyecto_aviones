# paginas/eda_2.py
import streamlit as st
from modules.eda.botones_eda_2 import seleccionar_datos
from modules.eda.botones_graficas import seleccionar_grafica
from modules.eda.datos_df_cargados import mostrar_estadisticas_df

def display():
    st.markdown("<h2 style='text-align: center;'>Página de análisis exploratorio de datos (EDA)</h2>", unsafe_allow_html=True)
    st.markdown("---")
    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h4 style='text-align: center;'>En esta sección de nuestro proyecto, te ofrecemos la oportunidad de explorar un análisis detallado de los datos a través de diversos gráficos y visualizaciones. Este espacio está diseñado para que puedas entender mejor y analizar de forma intuitiva la información que hemos recopilado.</h4>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')

    st.markdown("---")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.write("Puedes seleccionar el mes de diciembre de los años 2021, 2022 y 2023, o bien elegir todos los años para ver todos los datos juntos.")
        df_seleccionado = seleccionar_datos()
        if df_seleccionado is not None:
            st.markdown("---")
            mostrar_estadisticas_df(df_seleccionado, 'fecha')
            st.markdown("---")
            st.write("Una vez que has elegido el año, ahora puedes elegir qué tipo de gráfica ver. Para ayudarte hemos agrupado las gráficas por categorías.")
            grafica_funcion = seleccionar_grafica()

    with col2:
        if df_seleccionado is not None and grafica_funcion is not None:
            grafica_funcion(df_seleccionado)

display()

