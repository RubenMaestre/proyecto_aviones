# paginas/sobre_nosotros.py
import streamlit as st

def display():
    st.title("Sobre nosotros")

    st.markdown("""
            ### Sobre Nosotros - Proyecto Final en Hack a Boss

            Somos un equipo de aspirantes a científicos de datos que se han unido con un propósito común en el Bootcamp de Data Science & Inteligencia Artificial de Hack a Boss. Este proyecto es el culmen de meses de aprendizaje intensivo y colaboración, donde cada miembro ha aportado su dedicación, conocimientos técnicos y creatividad para superar los retos propuestos.

            #### Nuestro Viaje

            Desde el comienzo de este proyecto, nos propusimos no solo cumplir con los requisitos académicos, sino también superar nuestras propias expectativas en cuanto a la profundidad y utilidad del análisis. A través del uso integrado de tecnologías avanzadas como Python, Streamlit, Pandas y Plotly, hemos logrado manipular y presentar grandes volúmenes de datos sobre la puntualidad aérea de manera que no solo es comprensible, sino también visualmente atractiva y práctica.

            #### Colaboración y Crecimiento

            El trabajo en equipo ha sido esencial para nuestro éxito. Nos hemos enfrentado a desafíos técnicos y logísticos, aprendiendo en el proceso la importancia de una comunicación efectiva y el soporte mutuo. Este proyecto ha sido una valiosa lección sobre el trabajo colaborativo en situaciones de alta exigencia, preparándonos para futuros desafíos profesionales.

            #### Impacto y Futuro

            Miramos hacia adelante con entusiasmo, conscientes del potencial de expansión de nuestro proyecto. Estamos interesados en explorar nuevas variables, técnicas de modelado predictivo y expandir nuestro análisis a otras regiones. Cada paso adelante es una oportunidad para profundizar nuestro conocimiento y perfeccionar nuestras habilidades.

            #### Invitación a Colaborar

            Creemos firmemente en el poder de la comunidad y el intercambio de conocimientos. Si encuentras valor en nuestro trabajo o te sientes inspirado por nuestros esfuerzos, te animamos a compartirlo en tus redes sociales y plataformas profesionales. Tu apoyo amplifica nuestro alcance y abre puertas a nuevas oportunidades, acercándonos a nuestro sueño de convertirnos en influenciadores en el campo de la ciencia de datos.

            Además, puedes mostrar tu apoyo a nuestro proyecto dando una estrella en Streamlit. Esta acción incrementa la visibilidad de nuestro trabajo dentro de la comunidad y es un gran estímulo para nosotros. Habla de nuestro proyecto, comparte nuestra historia y ayuda a que más personas reconozcan la pasión y el esfuerzo que hemos invertido en convertirnos en profesionales capaces y comprometidos.

            **¡Gracias por tu apoyo y por ser parte de nuestro viaje!**
            """)

    # Información del equipo
    team_members = {
        'José Núñez': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Químico | Profesor de ciencias | Haz las cosas bien, pero sobre todo, disfrútalas.', 'https://www.linkedin.com/in/jose-nunez-ben-ali/', 'https://github.com/josnuzbel'),
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


