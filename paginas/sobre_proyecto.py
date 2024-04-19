import streamlit as st

def display():
    st.title('Información sobre el proyecto')
    
    st.write("Aquí encontrarás respuestas a algunas preguntas frecuentes sobre nuestro proyecto.")

        # FAQ 1: Objetivo del Proyecto
    with st.expander("¿Cuál es el objetivo de este proyecto?"):
        st.write("""
            Este proyecto constituye el trabajo final del Bootcamp de Data Science e Inteligencia Artificial en Hack a Boss. El objetivo principal es ofrecer una plataforma interactiva donde los usuarios puedan analizar y visualizar datos de vuelos, ayudando a entender mejor las tendencias y comportamientos en el tráfico aéreo de los Estados Unidos. Buscamos abordar un desafío crítico en la gestión aeronáutica: la optimización de la puntualidad y la gestión de retrasos en vuelos.

            A través de un análisis exploratorio de datos, proporcionamos perspectivas sobre las causas y factores que influyen en la puntualidad aérea y desarrollamos un modelo predictivo para mejorar la eficiencia de las operaciones aeroportuarias y la satisfacción de los pasajeros. El proyecto no solo cumple con los requisitos académicos de Hack a Boss, sino que también aplica lo aprendido en la solución de problemas prácticos, reflejando nuestra competencia técnica y determinación por innovar en el sector aeronáutico.
        """)

    # Otras FAQs
    with st.expander("¿Qué tecnologías se utilizan en el proyecto?"):
        st.write("""
            Este proyecto utiliza Python y Streamlit para la interfaz web, junto con bibliotecas como Pandas para 
            el manejo de datos y Plotly para las visualizaciones gráficas.
        """)

    # FAQ Nueva 1
    with st.expander("¿Qué desafíos nos hemos encontrado?"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    # FAQ Nueva 2
    with st.expander("¿Cuáles han sido los problemas más importantes que nos hemos encontrado?"):
        st.write("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

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