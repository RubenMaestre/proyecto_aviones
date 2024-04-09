import streamlit as st
import plotly.express as px

def graficar_evolucion_vuelos_por_aerolinea(df):
    # Asegurarse de que 'aerolinea' y 'anio' sean los nombres correctos de las columnas
    df_agrupado = df.groupby(['aerolinea', 'anio']).size().reset_index(name='numero_vuelos')

    # Crear la figura con Plotly
    fig = px.line(df_agrupado, x='anio', y='numero_vuelos', color='aerolinea',
                  title='Evolución del número de vuelos por compañía aérea',
                  labels={'anio': 'Año', 'numero_vuelos': 'Número de vuelos'})

    # Ajustar el tamaño de la gráfica y otros aspectos del layout
    fig.update_layout(xaxis_title='Año', yaxis_title='Número de Vuelos',
                      xaxis={'type': 'category'},
                      width=1080, height=720)

    # Actualizar la leyenda para mostrar solo una aerolínea específica (ejemplo: "American Airlines")
    fig.for_each_trace(lambda t: t.update(visible=True if t.name == "American Airlines" else 'legendonly'))

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

    # Mensaje instructivo para los usuarios
    st.markdown("""
        **Instrucciones:** Haz click en los nombres de las aerolíneas en la leyenda para filtrar y ver la evolución de vuelos de aerolíneas específicas.
    """)
