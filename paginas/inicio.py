# paginas/inicio.py
import streamlit as st

def display():
    st.image('sources/cabecera.jpg', use_column_width=True)

    # Título
    st.title("Estudio de puntualidad aérea: Un análisis en profundidad sobre la puntualidad en los aeropuertos estadounidenses")

    st.markdown("""
        ### Proyecto final para Hack a Boss
        """)
    st.markdown("""##### Este proyecto constituye el punto culminante de nuestra formación en el Bootcamp de Data Science e Inteligencia Artificial en Hack a Boss. En nuestro tercer y último proyecto, hemos decidido abordar un desafío crítico y de alta aplicabilidad en el sector aeronáutico: la optimización de la puntualidad y la gestión de retrasos en vuelos operados desde y hacia aeropuertos en Estados Unidos. A través de un exhaustivo análisis exploratorio de datos, este estudio ofrece perspectivas sobre causas, desempeños y factores influyentes en la puntualidad aérea, proporcionando un modelo predictivo en cuanto a la puntualidad de las aerolíneas para mejorar la satisfacción de los pasajeros.
        
    """)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([5, 1, 5])
    
    with col1:
        st.markdown("""
            #### El Equipo
        
        Este estudio ha sido desarrollado por José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez. Como equipo, hemos combinado nuestras competencias técnicas y experiencia analítica para investigar los retrasos en los vuelos, un tema crítico en la gestión aeronáutica. A través del análisis de grandes volúmenes de datos, hemos identificado tendencias significativas y patrones de comportamiento que influyen en la puntualidad aérea. Nuestro trabajo se centra en proporcionar un entendimiento detallado de los factores que afectan los tiempos de vuelo, con el objetivo de contribuir a la mejora de las operaciones en aeropuertos estadounidenses.

        Nuestro enfoque sistemático nos ha permitido desglosar los elementos clave que contribuyen a los retrasos aéreos, evaluando cómo variaciones en la gestión de aerolíneas, la infraestructura aeroportuaria y condiciones externas como festividades y clima impactan en la eficiencia operacional. Las conclusiones derivadas de este análisis proporcionan una base para la formulación de estrategias que pueden ser implementadas por entidades del sector para optimizar la puntualidad de sus operaciones.
        """)
    
    with col2:
        st.write("")

    with col3:
        st.markdown("""
            #### Metodología y Objetivos

        En la fase inicial de nuestro estudio, implementamos técnicas de web scraping utilizando Selenium para recolectar datos relevantes de múltiples fuentes en línea. Este enfoque nos permitió compilar un conjunto de datos exhaustivo y actualizado, esencial para nuestro Análisis Exploratorio de Datos (EDA). Durante el EDA, investigamos diversas variables para identificar aquellas que influyen significativamente en la puntualidad de los vuelos. El objetivo principal de esta fase era preparar el terreno para el desarrollo de un modelo predictivo.

        Con los insights obtenidos del EDA, procedimos a entrenar varios modelos de Machine Learning, buscando el que ofreciera la mejor capacidad predictiva respecto a la probabilidad de retraso de los vuelos. Aunque enfrentamos desafíos técnicos debido al gran tamaño de algunos modelos, que dificultaba su integración en plataformas como GitHub y Streamlit debido a restricciones de almacenamiento, seleccionamos un modelo con excelentes métricas de rendimiento. Este modelo está preparado para ser utilizado en entornos operativos, y estamos dispuestos a desarrollar un análisis más detallado y personalizado para aerolíneas que estén interesadas en optimizar sus operaciones.
        """)

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    col4, col5 = st.columns([5,2])

    with col4:
        st.markdown("""
        #### Herramientas y Tecnologías

        Para la realización de este proyecto, hemos empleado una variedad de herramientas tecnológicas adquiridas durante nuestro curso, incluyendo Python, Pandas, Numpy, Plotly, Matplotlib y Keras. Estas herramientas han sido fundamentales para procesar y analizar grandes volúmenes de datos de manera eficiente, así como para la visualización clara e interactiva de los resultados, facilitando el entendimiento de las tendencias y patrones detectados.

        Mediante el uso de Streamlit, hemos logrado presentar nuestros resultados de manera dinámica y accesible, proporcionando a los usuarios la posibilidad de interactuar con los datos y explorar en profundidad las diversas facetas de nuestro análisis. Este proyecto refleja no solo el aprendizaje alcanzado en Hack a Boss, sino también nuestra determinación por aplicar la ciencia de datos en la solución de problemas prácticos del mundo real. Confiamos en que los insights y visualizaciones que ofrecemos sean tanto informativos como de utilidad práctica para los interesados.
    """)

    with col5:
        st.image("sources/logotipo_hack_a_boss.png")