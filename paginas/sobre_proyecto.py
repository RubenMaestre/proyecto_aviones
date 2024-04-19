import streamlit as st

def display():
    st.title('Información sobre el proyecto')
    
    st.write("Aquí encontrarás respuestas a algunas preguntas frecuentes sobre nuestro proyecto.")

        # FAQ 1: Objetivo del Proyecto
    with st.expander("¿Cuál es el objetivo de este proyecto?"):
        st.write("""
            Este proyecto constituye el trabajo final del Bootcamp de Data Science e Inteligencia Artificial en Hack a Boss. El objetivo principal es ofrecer una plataforma interactiva donde los usuarios puedan analizar y visualizar datos de vuelos, ayudando a entender mejor las tendencias y comportamientos en el tráfico aéreo de los Estados Unidos. Buscamos abordar un desafío crítico en la gestión aeronáutica: la optimización de la puntualidad y la gestión de retrasos en vuelos.

            A través de un análisis exploratorio de datos, proporcionamos perspectivas sobre las causas y factores que influyen en la puntualidad aérea y desarrollamos un modelo predictivo para mejorar la eficiencia de las operaciones aeroportuarias y la satisfacción de los pasajeros. El proyecto no solo cumple con los requisitos académicos de Hack a Boss, sino que también aplica lo aprendido en la solución de problemas prácticos, reflejando nuestra competencia técnica y determinación por innovar y ser creativos en la realización de proyectos.
        """)

    # Otras FAQs
    with st.expander("¿Qué tecnologías se utilizan en el proyecto?"):
        st.write("""
            En este proyecto, hemos utilizado una amplia variedad de tecnologías y bibliotecas para la recolección, análisis y visualización de datos. La recolección de datos se realizó mediante técnicas de web scraping utilizando **BeautifulSoup** y **Selenium**, herramientas que nos permitieron automatizar la interacción con páginas web y extraer información de manera eficiente. **Requests** fue usado para manejar las solicitudes HTTP durante el scraping.

            Para el análisis y manipulación de datos, empleamos **Pandas**, una biblioteca fundamental en ciencia de datos para operaciones de manipulación de datos, y **NumPy** para operaciones numéricas complejas. **Datetime** facilitó la manipulación de fechas y tiempos.

            La visualización de datos es crucial para interpretar eficazmente las tendencias y patrones. Utilizamos **Matplotlib** y **Seaborn** para generar gráficos estáticos, mientras que **Plotly** nos permitió crear visualizaciones interactivas y dinámicas. **Folium** fue utilizado específicamente para mapas interactivos, permitiendo una contextualización geográfica de los datos.

            En cuanto al modelado predictivo, implementamos varios modelos de aprendizaje automático utilizando bibliotecas como **Scikit-learn**, que nos proporcionó algoritmos de clasificación como KNeighbors, DecisionTree, RandomForest y GradientBoosting, entre otros. **Imblearn** fue crucial para manejar el desbalance de clases mediante técnicas de OverSampling y UnderSampling.

            Para la interfaz de usuario, elegimos **Streamlit** por su capacidad para desarrollar aplicaciones de ciencia de datos de manera rápida y con un alto nivel de interactividad. Además, para el control de versiones y manejo de grandes volúmenes de datos, utilizamos **Git** con **GitHub** y **Git LFS** (Large File Storage), lo que nos permitió gestionar eficientemente los archivos de tamaño considerable generados durante el proyecto.

            Todas estas herramientas y tecnologías juntas nos han permitido crear un sistema robusto que no solo cumple con los requisitos técnicos del análisis de datos, sino que también proporciona una plataforma accesible y fácil de usar para cualquier usuario interesado en la puntualidad aérea.
        """)

    # FAQ Nueva 1
    with st.expander("¿Qué desafíos nos hemos encontrado?"):
        st.write("""
            El primer gran desafío que enfrentamos en cualquier proyecto de datos es asegurar la disponibilidad de datos de calidad. Una vez que decidimos enfocarnos en la puntualidad de los vuelos en Estados Unidos, comenzamos a aplicar todo lo aprendido durante nuestra formación en Hack a Boss. Trabajar en equipo fue crucial; nos apoyamos mutuamente en los momentos complicados para superar los desafíos que surgían. 
            Gracias a la colaboración y determinación del equipo, logramos superar los obstáculos y alcanzar con éxito los objetivos marcados por Hack a Boss para nuestro proyecto.
        """)


    # FAQ Nueva 2
    with st.expander("¿Cuáles han sido los problemas más importantes que nos hemos encontrado?"):
        st.write("""
            A lo largo del proyecto, nos enfrentamos a varios problemas que requirieron soluciones creativas y un pensamiento crítico agudo. Manejar un gran volumen de datos fue una tarea compleja, especialmente porque adaptamos muchos de los datos al contexto español, como las unidades de tiempo, distancias y nombres, lo que añadió una capa adicional de dificultad.
            El proceso de limpieza de datos fue intenso pero fructífero, permitiéndonos realizar un Análisis Exploratorio de Datos (EDA) con una amplia variedad de gráficos que ahora presentamos en este proyecto de Streamlit.
            Sin embargo, el mayor reto fue la selección del modelo de machine learning adecuado. Experimentamos con múltiples algoritmos, incluyendo Random Forest, Naive Bayes, GaussianNB, KNN, Gradient Boosting, NearestCentroid, DecisionTreeClassifier y AdaBoostClassifier, así como pruebas con redes neuronales de Deep Learning. Finalmente, optamos por el DecisionTreeClassifier, que no solo ofreció buenas métricas sino que también fue factible integrarlo en Streamlit dadas las restricciones de tamaño de archivo, con muchos modelos superando los 3GB que no podíamos cargar en la plataforma. Este fue, sin duda, uno de los desafíos más significativos que tuvimos que afrontar.
        """)


    # FAQ Nueva 3
    with st.expander("¿Cómo ha sido el desarrollo con Streamlit?"):
        st.write("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

    # FAQ Nueva 4
    with st.expander("¿Qué tipo de fortalezas destacamos en la ejecución del proyecto?"):
        st.write("Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    # FAQ Nueva 5
    with st.expander("Autocrítica con el proyecto"):
        st.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.")

    # FAQ Nueva 6
    with st.expander("¿Qué lecciones hemos aprendido con el proyecto?"):
        st.write("Eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.")

    # FAQ Nueva 7
    with st.expander("Conclusión final del proyecto"):
        st.write("Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione.")

    # FAQ 3 (Retrasada)
    with st.expander("¿Cómo puedo contribuir al proyecto?"):
        st.write("""
            Los interesados en contribuir al proyecto pueden hacerlo de varias maneras, como sugerir mejoras, 
            reportar bugs o colaborar en el desarrollo. Puedes contactarnos a través de [nuestro formulario de contacto](#).
        """)

# Llama a la función para mostrar la página
display()