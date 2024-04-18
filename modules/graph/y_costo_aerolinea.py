import streamlit as st
import pandas as pd
import plotly.express as px

# Diccionario de categorización de aerolíneas por costo
diccionario_costo = {
    'alto_costo': ["Delta Air Lines", "American Airlines", "United Airlines", "Alaska Airlines", "Hawaiian Airlines"],
    'medio_costo': ["Southwest Airlines", "JetBlue Airways"],
    'bajo_costo': ['Allegiant Air', 'Frontier Airlines', 'Spirit Airlines', 'Envoy Air', 'SkyWest Airlines',
                   'PSA Airlines', 'Endeavor Air', 'Mesa Airlines', 'Republic Airways', 'Horizon Air']
}

def asignar_costo(aerolinea):
    for costo, aerolineas in diccionario_costo.items():
        if aerolinea in aerolineas:
            return costo
    return 'otro'  # Retorna 'otro' si la aerolínea no está en las listas

def graficar_vuelos_por_costo_aerolinea(df):
    # Aplicar categorías de costo a cada aerolínea en el DataFrame
    df['costo_aerolinea'] = df['aerolinea'].apply(asignar_costo)

    # Agrupar por categoría de costo y contar vuelos
    vuelos_aerolinea = df.groupby('costo_aerolinea').size().reset_index(name='numero_vuelos')

    # Crear gráfico de barras usando Plotly Express
    fig = px.bar(vuelos_aerolinea,
                 x='costo_aerolinea',
                 y='numero_vuelos',
                 title='Cantidad de Vuelos según el Costo de la Aerolínea',
                 labels={'costo_aerolinea': 'Costo de la Aerolínea', 'numero_vuelos': 'Cantidad de Vuelos'},
                 color='costo_aerolinea',
                 color_discrete_map={'alto_costo': 'red', 'medio_costo': 'orange', 'bajo_costo': 'green', 'otro': 'grey'})

    fig.update_layout(title_x=0.5, xaxis_title='Costo de la Aerolínea', yaxis_title='Cantidad de Vuelos')

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)