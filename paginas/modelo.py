#paginas/modelo.py
import streamlit as st
from modules.ml.ml_1 import display_ml_page
from modules.ml.metricas import mostrar_metricas

def display():
    st.title('¿Quieres saber si tu vuelo llegará puntual en Estados Unidos?')
    st.markdown("""
    ¡Bienvenido al futuro de las predicciones de vuelos! Imagina poder saber con certeza si tu próximo vuelo llegará a tiempo o sufrirá algún retraso. **Gracias a nuestro avanzado modelo de predicción, esa realidad está más cerca que nunca.** Nuestro sistema, desarrollado por expertos en análisis de datos, utiliza algoritmos de vanguardia y ha sido entrenado con una base de datos meticulosamente seleccionada y exhaustivamente limpiada.

    **Nuestro modelo infalible,** diseñado con precisión milimétrica, te ofrece la oportunidad de planificar tu viaje sin las molestias de las incertidumbres aéreas. Hemos analizado cientos de miles de datos de vuelos para asegurarnos de que nuestro modelo prediga con la mayor precisión posible. **¡No más sorpresas en el aeropuerto!**

    ¿Estás listo para descubrir cómo puede cambiar tu experiencia de viaje? **Haz tu selección** y deja que nuestro modelo de predicción te demuestre su eficacia. ¡Descubre si tu vuelo llegará a tiempo y gestiona mejor tu tiempo y expectativas! Con nuestro modelo, cada predicción es un paso hacia un viaje más tranquilo y predecible. Ven y experimenta el poder de la ciencia de datos aplicada a la vida real. ¡Tu próximo viaje a Estados Unidos podría ser el más puntual de tu vida!
    """)
    st.markdown("---")
    
    display_ml_page()

    st.markdown("---")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.write("Presentamos a continuación las métricas de rendimiento del modelo desarrollado utilizando DecisionTreeClassifier de scikit-learn. Estos indicadores te ayudarán a comprender la eficacia y precisión del modelo en la clasificación de datos.")
        st.image("sources/metricas.jpg")  # Mostrar imagen en la columna central
    with col2:
        mostrar_metricas()
