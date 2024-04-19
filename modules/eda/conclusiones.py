# modules/eda/conclusiones.py
import streamlit as st

def mostrar_conclusiones():
    st.markdown("## Conclusiones finales del EDA")
    st.markdown("""
    - **Tendencia de crecimiento en el número de vuelos**: A lo largo de los años analizados, se observa un incremento en el número de vuelos. Esto puede indicar un aumento en la demanda de viajes aéreos internos en EEUU.
    - **Variedad en el desempeño de las aerolíneas**: Existe una variabilidad significativa en la cantidad de vuelos realizados por cada compañía aérea. Las aerolíneas más grandes, como Southwest Airlines y American Airlines, lideran en número de vuelos, mientras que las más pequeñas tienen una presencia más limitada.
    - **Relación entre retrasos en la salida y llegada**: Se observa una relación positiva moderadamente fuerte entre los retrasos en la salida y los retrasos en la llegada de los vuelos. Esto sugiere que los vuelos que experimentan retrasos en la salida tienden a experimentar retrasos similares en la llegada.
    - **Impacto de los días festivos en los retrasos**: Durante los días festivos, se registra un aumento significativo en la incidencia de retrasos tanto en la salida como en la llegada de los vuelos, en comparación con los días laborables. Esto puede deberse a una combinación de factores, como la mayor congestión en los aeropuertos y los cambios en las operaciones de las aerolíneas.
    - **Desafíos en la puntualidad de los vuelos**: Algunos estados, como Florida, experimentan más retrasos en comparación con otros, a pesar de tener un alto número de vuelos. Esto sugiere que pueden existir desafíos adicionales en los aeropuertos de esos estados que afectan la puntualidad de los vuelos.
    - **Impacto de la distancia en los retrasos**: Existe una tendencia a que los vuelos de mayor distancia tengan menos retrasos en comparación con los vuelos de distancias más cortas. Esto puede ser útil para las aerolíneas al planificar sus rutas y horarios para minimizar los retrasos.
    - **Desempeño operativo de las aerolíneas según su categoría de costo**: Las aerolíneas de costo medio tienen un mayor número de retrasos en comparación con las aerolíneas de bajo costo, a pesar de tener más vuelos en total. Esto sugiere que el costo de los vuelos no necesariamente está relacionado con la puntualidad o la eficiencia operativa de las aerolíneas.
    """)
