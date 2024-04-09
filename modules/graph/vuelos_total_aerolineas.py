import streamlit as st
import plotly.express as px

def graficar_vuelos_por_aerolinea(df):
    # Asegúrate de que 'aerolinea' sea el nombre correcto de la columna en tu DataFrame
    vuelos_aerolinea = df.groupby(['aerolinea']).size().reset_index(name='numero_vuelos')

    # Crear la figura con Plotly
    fig = px.bar(data_frame=vuelos_aerolinea,
                 x='aerolinea',
                 y='numero_vuelos',
                 opacity=0.8,
                 title="Cantidad de Vuelos por Compañía Aérea",
                 color='aerolinea')

    fig.update_layout(title_x=0.5, xaxis_title='Compañía Aérea', yaxis_title='Cantidad de Vuelos', xaxis={'categoryorder': 'total descending'})
    
    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
