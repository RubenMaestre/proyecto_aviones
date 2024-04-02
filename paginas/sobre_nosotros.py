# paginas/sobre_nosotros.py
import streamlit as st

def display():
    st.title("Sobre nosotros")

    # Descripción del proyecto y el equipo
    st.markdown("""
    ### Proyecto final para Hack a Boss

    Este proyecto es el resultado del trabajo en equipo para el Bootcamp de Data Science & 
    Inteligencia Artificial de Hack a Boss. A través de este desafío, hemos profundizado en el 
    estudio de la puntualidad y los retrasos en los vuelos, utilizando una variedad de herramientas
    analíticas.

    #### El Equipo
    Compuesto por José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez, este grupo ha combinado 
    sus habilidades para abordar un tema apasionante y técnico con relevancia práctica y teórica.

    #### Metodología y Herramientas
    Con un enfoque en el Análisis Exploratorio de Datos (EDA) y el desarrollo de modelos de Machine Learning,
    el equipo ha utilizado herramientas como Python, Pandas, Numpy, Plotly, Matplotlib y Keras para 
    procesar, analizar y visualizar grandes conjuntos de datos.

    --- 
    """)

    # Imágenes y perfiles del equipo
    col1, col2, col3, col4 = st.columns(4)
    team_members = {
        'José Núñez': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
        'Rubén Maestre': 'Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Experto en Marketing Digital y Comunicación | MBA en Gestión Deportiva | Diseño Gráfico, WordPress y Redes Sociales | Proyectos Digitales',
        'Dafne Moreno': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
        'Nahuel Núñez': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
    }

    for name, (description, linkedin_url, github_url) in team_members.items():
        with col1:
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=150, caption=name)
            st.markdown(description)
            st.markdown(f'[![LinkedIn]({linkedin_url}sources/LinkedIn-icon.png)]({linkedin_url})', unsafe_allow_html=True)
            st.markdown(f'[![GitHub]({github_url}sources/GitHub-Mark.png)]({github_url})', unsafe_allow_html=True)

    for name, (description, linkedin_url, github_url) in team_members.items():
        with col2:
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=150, caption=name)
            st.markdown(description)
            st.markdown(f'[![LinkedIn]({linkedin_url}sources/LinkedIn-icon.png)]({https://www.linkedin.com/in/rubenmaestrezaplana/})', unsafe_allow_html=True)
            st.markdown(f'[![GitHub]({github_url}sources/GitHub-Mark.png)]({https://github.com/RubenMaestre})', unsafe_allow_html=True)

        for name, (description, linkedin_url, github_url) in team_members.items():
        with col3:
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=150, caption=name)
            st.markdown(description)
            st.markdown(f'[![LinkedIn]({linkedin_url}sources/LinkedIn-icon.png)]({linkedin_url})', unsafe_allow_html=True)
            st.markdown(f'[![GitHub]({github_url}sources/GitHub-Mark.png)]({github_url})', unsafe_allow_html=True)

    for name, (description, linkedin_url, github_url) in team_members.items():
        with col4:
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=150, caption=name)
            st.markdown(description)
            st.markdown(f'[![LinkedIn]({linkedin_url}sources/LinkedIn-icon.png)]({linkedin_url})', unsafe_allow_html=True)
            st.markdown(f'[![GitHub]({github_url}sources/GitHub-Mark.png)]({github_url})', unsafe_allow_html=True)


    st.markdown("""
    ---
    Esperamos que esta sección proporcione una visión más cercana de quiénes somos y qué nos impulsa
    en el campo de la ciencia de datos. Para más detalles sobre nuestro trabajo, síguenos en LinkedIn
    y consulta nuestros repositorios en GitHub.
    """)
    
# No olvides llamar a la función display en el archivo principal de Streamlit para que la página se muestre.
