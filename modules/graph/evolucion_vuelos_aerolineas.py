import streamlit as st
import plotly.express as px

def graficar_evolucion_vuelos_por_aerolinea(df):
    # Asegurarse de que 'aerolinea' y 'anio' sean los nombres correctos de las columnas
    df_agrupado = df.groupby(['aerolinea', 'anio']).size().reset_index(name='numero_vuelos')

    # Crear la figura con Plotly
    fig = px.line(df_agrupado, x='anio', y='numero_vuelos', color='aerolinea',
                  title='Evolución del número de vuelos por compañía aérea',
                  labels={'anio': 'Año', 'numero_vuelos': 'Número de vuelos'})

    fig.update_layout(xaxis_title='Año', yaxis_title='Número de Vuelos',
                      xaxis={'type': 'category'},  # Asegurar que el eje x trate los años como categorías
                      width=1280, height=720)  # Tamaño personalizado

    # Permitir a los usuarios seleccionar/deseleccionar aerolíneas específicas para comparar
    fig.update_layout(legend_title_text='Compañía Aérea')
    fig.for_each_trace(lambda t: t.update(name=t.name.replace('aerolinea=', '')))

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
