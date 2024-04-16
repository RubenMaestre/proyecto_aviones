# paginas/eda.py
import streamlit as st
from modules.eda.botones_eda import seleccionar_datos
from modules.eda.botones_graficas import seleccionar_grafica
from modules.eda.datos_df_cargados import mostrar_estadisticas_df
from modules.eda.descripciones_graficas import obtener_descripcion 

def display():
    st.markdown("<h2 style='text-align: center;'>Página de análisis exploratorio de datos (EDA)</h2>", unsafe_allow_html=True)
    st.markdown("---")
    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h4 style='text-align: center;'>En esta sección de nuestro proyecto, te ofrecemos la oportunidad de explorar un análisis detallado de los datos a través de diversos gráficos y visualizaciones. Este espacio está diseñado para que puedas entender mejor y analizar de forma intuitiva la información que hemos recopilado.</h4>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')

    st.markdown("---")
    # Inserta aquí el código CSS para la línea de separación
    
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{{
            max-width: 95%;
        }}
        .divider {{
            height: 100%;
            width: 2px;
            border-left: 2px solid #ffffff;
            margin-right: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, divider, col2 = st.columns([1, 0.3, 4])
    with col1:
        st.write("Puedes seleccionar el mes de diciembre de los años 2021, 2022 y 2023, o bien elegir todos los años para ver todos los datos juntos.")
        df_seleccionado = seleccionar_datos()
        if df_seleccionado is not None:
            st.markdown("---")
            mostrar_estadisticas_df(df_seleccionado, 'fecha')
            st.write("* Datos de diciembre")
            st.markdown("---")
            st.write("Una vez que has elegido el año, ahora puedes elegir qué tipo de gráfica ver. Para ayudarte hemos agrupado las gráficas por categorías.")
            grafica_funcion, grafica_nombre = seleccionar_grafica()  # Asumiendo que la función ahora devuelve ambos

    with divider:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    with col2:
        if df_seleccionado is not None and grafica_funcion:
            grafica_funcion(df_seleccionado)
            descripcion = obtener_descripcion(st.session_state['selected_year'], grafica_nombre)
            st.write("Descripción de la gráfica:")
            st.markdown(descripcion)

display()
