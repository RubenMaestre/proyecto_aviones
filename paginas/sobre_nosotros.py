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
        'José Núñez': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Químico | Profesor de ciencias | Haz las cosas bien, pero sobre todo, disfrútalas.', 'https://www.linkedin.com/in/jos%C3%A9-n%C3%BA%C3%B1ez-ben-al%C3%AD-561b3a298/', 'https://github.com/josnuzbel'),
        'Rubén Maestre': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Experto en Marketing Digital y Comunicación | MBA en Gestión Deportiva | Diseño Gráfico, WordPress y Redes Sociales | Proyectos Digitales', 'https://www.linkedin.com/in/rubenmaestrezaplana/', 'https://github.com/RubenMaestre'),
        'Dafne Moreno': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL, Machine Learning, Deep Learning, Streamlit | Desarrollo web: HTML, CSS, JavaScript / Terapeuta Ocupacional: salud mental', 'https://www.linkedin.com/in/dafne-moreno-palomares-86a30526b/', 'https://github.com/dafnemorenop'),
        'Nahuel Núñez': ('Argentino, actualmente viviendo en Málaga. Me considero un trabajador muy eficiente para tareas en solitario como así también en grupo.', 'https://www.linkedin.com/in/nahuel-nunez-/', 'https://www.github.com/'),
    }

    cols = st.columns(4)
    for index, (name, (description, linkedin_url, github_url)) in enumerate(team_members.items()):
        with cols[index % 4]:
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=300, caption=name)
            st.markdown(description)
            # Botones de LinkedIn y GitHub
            if st.button("LinkedIn", key=f"linkedin-{name}", 
                         help="Visita mi perfil de LinkedIn"):
                st.write(f"Redirigiendo a {linkedin_url}")
            if st.button("GitHub", key=f"github-{name}", 
                         help="Visita mi perfil de GitHub"):
                st.write(f"Redirigiendo a {github_url}")

    st.markdown("""
    ---
    Esperamos que esta sección proporcione una visión más cercana de quiénes somos y qué nos impulsa
    en el campo de la ciencia de datos. Para más detalles sobre nuestro trabajo, síguenos en LinkedIn
    y consulta nuestros repositorios en GitHub.
    """)

display()


