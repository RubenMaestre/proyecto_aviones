import streamlit as st
from modules.datos_page.data_count import cargar_y_contar_datos

def display():
    st.title('Extracción de datos y explicación')

    st.markdown("""
            <div style='text-align: justify;'>
            <p><strong style='font-size: 18px;'>Los datos presentados en esta plataforma han sido meticulosamente recolectados mediante técnicas avanzadas de web scraping, empleando un conjunto de herramientas especializadas en la extracción y manipulación de información de páginas web. Este proceso se llevó a cabo con el fin de proporcionar análisis detallados y actualizados sobre los vuelos nacionales en Estados Unidos. <br>Uno de los mayores desafíos al iniciar un proyecto de análisis de datos desde cero es, sin duda, la búsqueda y adquisición de datos relevantes y confiables. Antes de decidirnos por este enfoque específico, llevamos a cabo una exhaustiva investigación exploratoria en busca de temas potencialmente interesantes. Durante esta fase, exploramos múltiples fuentes de datos, incluyendo repositorios populares como Kaggle, diversas páginas gubernamentales y otras plataformas especializadas en datos abiertos. Después de evaluar varias opciones y temáticas, nos decantamos por el estudio de la puntualidad en los vuelos internos de Estados Unidos. Esta elección estuvo motivada tanto por la disponibilidad de datos como por la relevancia del tema en el contexto actual de la industria de la aviación, donde la eficiencia operativa es crucial. <br>Este enfoque nos permitió centrarnos en una problemática de alta relevancia y aplicabilidad, donde nuestras habilidades en ciencia de datos podrían ser aplicadas para generar insights significativos y propuestas de valor concretas para mejorar la experiencia de viaje en Estados Unidos.</strong></p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5, 12, 0.5])
    with col2:  # Utilizamos la columna del medio para la imagen
        st.image('sources/cabecera_datos.jpg')  # Asegúrate de que la ruta de la imagen sea correcta

    st.header('Tecnologías utilizadas')
    st.markdown("""
    - **BeautifulSoup**: Una librería de Python que facilita la extracción de información de páginas web, parseando los documentos HTML y permitiendo la manipulación eficiente de los mismos.
    - **Requests**: Un módulo de Python para enviar solicitudes HTTP de manera sencilla, utilizado para obtener el código fuente de las páginas web desde las cuales recolectamos datos.
    - **Selenium WebDriver**: Herramienta de automatización para manejar navegadores web, que permite interactuar con elementos web de forma programática en sitios que requieren interacciones dinámicas.
    - **By**: Módulo en Selenium utilizado para localizar elementos dentro de una página web usando varios métodos como id, name, xpath, entre otros.
    - **Select**: Clase en Selenium para interactuar con los elementos `<select>` de los formularios HTML, facilitando la selección automática en menús desplegables.
    - **WebDriverWait y Expected Conditions (EC)**: Utilizados para gestionar la espera de elementos específicos en la página que pueden tardar en aparecer, asegurando que los datos estén disponibles antes de proceder con su extracción.
    - **sleep (time)**: Función del módulo `time` de Python que pausa la ejecución del script para simular interacciones humanas o cumplir con las políticas de uso de los servidores web, evitando ser detectados como bots.
    """)


    st.header('Fuente de los datos')
    st.markdown("""
        Los datos para este estudio fueron extraídos del [Departamento de Estadísticas de Transporte de EE. UU. (BTS)](https://www.transtats.bts.gov/ONTIME/Departures.aspx), una entidad del Departamento de Transporte (DOT). El BTS es reconocido como la principal fuente de estadísticas sobre la aviación comercial, la actividad de transporte multimodal de mercancías y la economía del transporte, proporcionando datos esenciales para tomadores de decisiones y el público en general.

        El BTS asegura la credibilidad de sus productos y servicios a través de un análisis riguroso, una calidad de datos transparente y una independencia de la influencia política, promoviendo métodos innovadores de recolección, análisis, visualización y difusión de datos. Estos esfuerzos ayudan a mejorar la eficiencia operativa, explorar temas emergentes y crear productos informativos que contribuyen a un entendimiento profundo del transporte y su papel transformador en la sociedad.

        La directora del BTS, la Sra. Patricia S. Hu, posee una extensa experiencia estadística, un profundo conocimiento del transporte y una sólida formación en investigación. El Dr. Rolf R. Schmitt, el Subdirector, es un experto reconocido en política de transporte y en el desarrollo de estadísticas para informar decisiones de transporte. Ambos lideran un equipo que es clave en el establecimiento de normativas y estrategias que influyen en el panorama del transporte estadounidense y global.
        """)


    st.header('Proceso de extracción')
    st.markdown("""
        El proceso de extracción se inició almacenando la URL de la página web de vuelos desde la que extraeríamos la información. Esta URL corresponde a la página oficial del [Departamento de Estadísticas de Transporte de EE. UU.](https://www.transtats.bts.gov/ONTIME/Departures.aspx).

        Desarrollamos una función en Python diseñada para desplegar y extraer las opciones disponibles de los menús desplegables de la página. La función, denominada `obtener_opciones`, realiza una solicitud GET a la URL, analiza el HTML de la página utilizando BeautifulSoup y extrae las opciones del menú especificado. A continuación, se muestra un ejemplo de cómo funciona esta función para obtener las listas de aeropuertos y aerolíneas:
        """)

    st.code("""
        url = "https://www.transtats.bts.gov/ONTIME/Departures.aspx"

        def obtener_opciones(url, aeropuertos_aerolineas):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            seleccionar_aeropuerto_aerolinea = soup.find("select", attrs={"name": aeropuertos_aerolineas})
            opciones = seleccionar_aeropuerto_aerolinea.find_all("option")
            listado_opciones = [opcion.text for opcion in opciones]
            return listado_opciones

        listado_aeropuertos = obtener_opciones(url, "cboAirport")
        listado_aerolineas = obtener_opciones(url, "cboAirline")
        """, language='python')

    st.markdown("""
        Utilizando estas listas, procedimos a iterar sobre cada combinación de aeropuerto y aerolínea, aplicando filtros en la página para obtener datos de vuelos específicos de diciembre de los años 2021, 2022 y 2023. Este método automatizado facilitó la recolección sistemática y eficiente de los datos necesarios para nuestro análisis.
        """)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([5,1,5])

    with col1:
        st.image('sources/datos_1.jpg', use_column_width=True)
        st.header('Automatización del Proceso de Selección')
        st.markdown("""
            Esta función automatiza la selección de elementos en un menú desplegable. Se utiliza específicamente para seleccionar los aeropuertos y aerolíneas previamente almacenados en dos listas. La elección de **By.NAME** se debe al hecho de que estos elementos están identificados por su nombre en el código HTML.
            """)

        st.code("""
            def seleccionar_por_indice(url, nombre_seleccionado, lista_elementos):
                \"\"\"Esta función selecciona los aeropuertos y las aerolíneas en el menú desplegable\"\"\"
                driver = webdriver.Firefox()
                driver.get(url)
                seleccion = Select(driver.find_element(By.NAME, nombre_seleccionado))
                
                for elemento in lista_elementos:
                    seleccion.select_by_visible_text(elemento)
                    sleep(1) 
        """, language='python')

    with col2:
        st.write("")

    with col3:
        st.image('sources/datos_2.jpg', use_column_width=True) 
        st.header('Función para preselecciones')
        st.markdown("""
            La función **preselecciones** se utiliza al inicio para marcar de antemano todas las estadísticas (por qué sale tarde, el tiempo que tarda en despegar, etc.), todos los días del mes, el mes de diciembre y los tres años con los que hemos hecho el trabajo.
            """)

        st.code("""
            def preselecciones(driver):
                \"\"\"Preselecciona las casillas necesarias para la extracción\"\"\"
                driver.find_element(By.ID, "chkAllStatistics").click() 
                driver.find_element(By.ID, "chkAllDays").click()  
                driver.find_element(By.ID, "chkMonths_11").click()  # click_mes_diciembre
                
                # Selecciona 2021, 2022 y 2023
                driver.find_element(By.ID, "chkYears_34").click()
                driver.find_element(By.ID, "chkYears_35").click() 
                driver.find_element(By.ID, "chkYears_36").click()
        """, language='python')


    # Llamar a la función para obtener los datos calculados
    numero_total_estados, numero_total_ciudades, numero_total_aeropuertos, numero_total_aerolineas = cargar_y_contar_datos()

    # Crear 4 columnas para mostrar los datos
    col1, col2, col3, col4 = st.columns(4)

    # Definir el estilo CSS para el borde y el contenido de la columna
    column_style = """
        <style>
        .data-column {{
            border: 2px solid #CCCCCC;  /* Grosor y color del borde */
            border-radius: 10px;  /* Bordes redondeados */
            padding: 20px;  /* Espaciado interno */
            text-align: center;  /* Alineación del texto */
        }}
        </style>
        <div class='data-column'>
            <h4>{title}</h4>
            <h1>{value}</h1>
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
    "*" Aquí se incluyen estados de los Estados Unidos y también territorios no incorporados.
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
