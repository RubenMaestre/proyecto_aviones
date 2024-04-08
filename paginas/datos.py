import streamlit as st
from modules.data_count import cargar_y_contar_datos

def display():
    st.title('Extracción de datos y explicación')

    st.markdown("""
    Los datos presentados en esta plataforma han sido meticulosamente recolectados mediante técnicas avanzadas de web scraping, empleando un conjunto de herramientas especializadas en la extracción y manipulación de información de páginas web. Este proceso se llevó a cabo con el fin de proporcionar análisis detallados y actualizados sobre los vuelos nacionales en Estados Unidos.
    """)

    col1, col2, col3 = st.columns([1, 12, 1])
    with col2:  # Utilizamos la columna del medio para la imagen
        st.image('sources/cabecera_datos.jpg')  # Asegúrate de que la ruta de la imagen sea correcta

    st.header('Tecnologías utilizadas')
    st.markdown("""
    - **BeautifulSoup**: para el análisis del HTML de las páginas web y la extracción de datos.
    - **Selenium**: una herramienta para la automatización de navegadores web, utilizada para interactuar con elementos de la página que requieren de acciones como clics o selección de opciones.
    - **Pandas**: una librería de Python que ofrece estructuras de datos y herramientas de análisis.
    - **NumPy**: una librería fundamental para la computación científica con Python.
    - **Requests**: permite enviar solicitudes HTTP en Python, utilizada para obtener el contenido de la página web.
    """)

    st.header('Fuente de los datos')
    st.markdown("""
    Los datos fueron extraídos de [Departamentos de Estadísticas de Transporte de EE. UU.](https://www.transtats.bts.gov/ONTIME/Departures.aspx)
    """)

    st.header('Proceso de extracción')
    st.markdown("""
    El proceso de extracción se inició obteniendo listas de todos los aeropuertos y aerolíneas disponibles en el sitio web objetivo. Posteriormente, se automatizó la navegación en el sitio para seleccionar cada combinación de aeropuerto y aerolínea, aplicando filtros para obtener los datos de los vuelos de diciembre de los años 2021, 2022 y 2023.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image('sources/datos_1.jpg')
        st.subheader('Preselecciones')
        st.markdown("""
        - Seleccionar todas las estadísticas y días disponibles.
        - Foco específico en los vuelos nacionales.
        """)

    with col2:
        st.image('sources/datos_2.jpg') 
        st.subheader('Descarga de datos')
        st.markdown("""
        - Configuración de filtros para los meses de diciembre de 2021, 2022 y 2023.
        - Técnicas para manejar elementos dinámicos y esperas.
        """)

    st.header('Contenido de los datos')
    st.markdown("""
    Los datos recopilados abarcan información detallada sobre los vuelos nacionales en Estados Unidos durante los meses de diciembre de 2021, 2022 y 2023. Esto incluye horarios de vuelo, retrasos, cancelaciones, aerolíneas y aeropuertos implicados.
    """)

    # Llamar a la función para obtener los datos calculados
    numero_total_estados, numero_total_ciudades, numero_total_aeropuertos, numero_total_aerolineas = cargar_y_contar_datos()

    # Crear 4 columnas para mostrar los datos
    col1, col2, col3, col4 = st.columns(4)

    # Definir el estilo CSS para el borde y el contenido de la columna
    column_style = """
    <style>
    .data-column {
        border: 2px solid #CCCCCC;  /* Grosor y color del borde */
        border-radius: 10px;  /* Bordes redondeados */
        padding: 20px;  /* Espaciado interno */
        text-align: center;  /* Alineación del texto */
    }
    </style>
    <div class='data-column'>
        <h4 style='color: black;'>{title}</h4>
        <h1 style='color: #B0B0B0;'>{value}</h1>
    </div>
    """

    with col1:
        st.markdown(column_style.format(title='Número total de Estados*', value=numero_total_estados), unsafe_allow_html=True)

    with col2:
        st.markdown(column_style.format(title='Número total de ciudades', value=numero_total_ciudades), unsafe_allow_html=True)

    with col3:
        st.markdown(column_style.format(title='Número total de aeropuertos', value=numero_total_aeropuertos), unsafe_allow_html=True)

    with col4:
        st.markdown(column_style.format(title='Número total de aerolíneas', value=numero_total_aerolineas), unsafe_allow_html=True)

    st.markdown("""
    * Aquí se incluyen Estados de los Estados Unidos y también territorios no incorporados.
    """)

    st.header('Uso de los datos')
    st.markdown("""
    Esta valiosa colección de datos permite realizar una variedad de análisis y visualizaciones, ofreciendo insights sobre tendencias en el tráfico aéreo, la puntualidad de las aerolíneas, los aeropuertos más activos, entre otros aspectos relevantes para investigadores, analistas y entusiastas de la aviación.
    """)

    st.header('Compromiso futuro')
    st.markdown("""
    En el futuro iremos incorporando los datos de todos los meses y años de los que hay registro. Debido al enorme volumen de datos, hemos decidido seleccionar los meses de diciembre los 3 últimos años para arrancar el proyecto.
    """)

# Llama a la función para mostrar la página
display()
