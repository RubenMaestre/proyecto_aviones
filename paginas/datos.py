import streamlit as st

def display():
    st.title('Extracción de Datos y Explicación')

    st.markdown("""
    Los datos presentados en esta plataforma han sido meticulosamente recolectados mediante técnicas avanzadas de web scraping, empleando un conjunto de herramientas especializadas en la extracción y manipulación de información de páginas web. Este proceso se llevó a cabo con el fin de proporcionar análisis detallados y actualizados sobre los vuelos nacionales en Estados Unidos.
    """)

    st.header('Tecnologías Utilizadas')
    st.markdown("""
    - **BeautifulSoup**: para el análisis del HTML de las páginas web y la extracción de datos.
    - **Selenium**: una herramienta para la automatización de navegadores web, utilizada para interactuar con elementos de la página que requieren de acciones como clics o selección de opciones.
    - **Pandas**: una librería de Python que ofrece estructuras de datos y herramientas de análisis.
    - **NumPy**: una librería fundamental para la computación científica con Python.
    - **Requests**: permite enviar solicitudes HTTP en Python, utilizada para obtener el contenido de la página web.
    """)

    st.header('Fuente de los Datos')
    st.markdown("""
    Los datos fueron extraídos de [Departamentos de Estadísticas de Transporte de EE. UU.](https://www.transtats.bts.gov/ONTIME/Departures.aspx)
    """)

    st.header('Proceso de Extracción')
    st.markdown("""
    El proceso de extracción se inició obteniendo listas de todos los aeropuertos y aerolíneas disponibles en el sitio web objetivo. Posteriormente, se automatizó la navegación en el sitio para seleccionar cada combinación de aeropuerto y aerolínea, aplicando filtros para obtener los datos de los vuelos de diciembre de los años 2021, 2022 y 2023.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Preselecciones')
        st.markdown("""
        - Seleccionar todas las estadísticas y días disponibles.
        - Foco específico en los vuelos nacionales.
        """)

    with col2:
        st.subheader('Descarga de Datos')
        st.markdown("""
        - Configuración de filtros para los meses de diciembre de 2021, 2022 y 2023.
        - Técnicas para manejar elementos dinámicos y esperas.
        """)

    st.header('Contenido de los Datos')
    st.markdown("""
    Los datos recopilados abarcan información detallada sobre los vuelos nacionales en Estados Unidos durante los meses de diciembre de 2021, 2022 y 2023. Esto incluye horarios de vuelo, retrasos, cancelaciones, aerolíneas y aeropuertos implicados.
    """)

    st.header('Uso de los Datos')
    st.markdown("""
    Esta valiosa colección de datos permite realizar una variedad de análisis y visualizaciones, ofreciendo insights sobre tendencias en el tráfico aéreo, la puntualidad de las aerolíneas, los aeropuertos más activos, entre otros aspectos relevantes para investigadores, analistas y entusiastas de la aviación.
    """)

# Llama a la función para mostrar la página
display()
