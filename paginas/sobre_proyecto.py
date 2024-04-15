import streamlit as st

def display():
    st.title('Información sobre el proyecto')
    
    st.write("Aquí encontrarás respuestas a algunas preguntas frecuentes sobre nuestro proyecto.")

    # FAQ 1
    with st.expander("¿Cuál es el objetivo de este proyecto?"):
        st.write("""
            El objetivo principal de este proyecto es proporcionar una plataforma donde los usuarios puedan 
            analizar y visualizar datos de vuelos de manera interactiva, ayudando a entender mejor las tendencias 
            y comportamientos en el tráfico aéreo.
        """)

    # FAQ 2
    with st.expander("¿Qué tecnologías se utilizan en el proyecto?"):
        st.write("""
            Este proyecto utiliza Python y Streamlit para la interfaz web, junto con bibliotecas como Pandas para 
            el manejo de datos y Plotly para las visualizaciones gráficas.
        """)

    # FAQ 3
    with st.expander("¿Cómo puedo contribuir al proyecto?"):
        st.write("""
            Los interesados en contribuir al proyecto pueden hacerlo de varias maneras, como sugerir mejoras, 
            reportar bugs o colaborar en el desarrollo. Puedes contactarnos a través de [nuestro formulario de contacto](#).
        """)

    # Añade más FAQs de la misma manera

# Llama a la función para mostrar la página
display()
