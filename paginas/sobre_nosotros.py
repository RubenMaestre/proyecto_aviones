# paginas/sobre_nosotros.py
import streamlit as st

def display():
    st.title("Sobre nosotros")

    st.markdown("""
    ### Proyecto final para Hack a Boss
    Este proyecto es el resultado del trabajo en equipo para el Bootcamp de Data Science & 
    Inteligencia Artificial de Hack a Boss. A través de este desafío, hemos profundizado en el 
    estudio de la puntualidad y los retrasos en los vuelos, utilizando una variedad de herramientas
    analíticas.
    ...
    """)

    # Información del equipo
    team_members = {
        'José Núñez': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.', 'https://www.linkedin.com/', 'https://www.github.com/'),
        'Rubén Maestre': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Experto en Marketing Digital y Comunicación | MBA en Gestión Deportiva | Diseño Gráfico, WordPress y Redes Sociales | Proyectos Digitales', 'https://www.linkedin.com/in/rubenmaestrezaplana/', 'https://github.com/RubenMaestre'),
        'Dafne Moreno': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.', 'https://www.linkedin.com/', 'https://www.github.com/'),
        'Nahuel Núñez': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.', 'https://www.linkedin.com/', 'https://www.github.com/'),
    }

    cols = st.columns(4)
    for index, (name, (description, linkedin_url, github_url)) in enumerate(team_members.items()):
        with cols[index % 4]:  # Esto rotará entre las 4 columnas
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=300, caption=name)
            st.markdown(description)
            st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="sources/linkedin.png" alt="LinkedIn" style="width: 30px;"></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="sources/github.png" alt="GitHub" style="width: 30px;"></a>', unsafe_allow_html=True)

    st.markdown("""
    ---
    Esperamos que esta sección proporcione una visión más cercana de quiénes somos y qué nos impulsa
    en el campo de la ciencia de datos. Para más detalles sobre nuestro trabajo, síguenos en LinkedIn
    y consulta nuestros repositorios en GitHub.
    """)

    st.image('sources/linkedin.png')
    st.image('sources/github.png')
display()


