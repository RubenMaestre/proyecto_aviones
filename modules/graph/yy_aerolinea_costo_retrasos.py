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

def graficar_vuelos_retrasos_por_costo_aerolinea(df):
    # Asignar categorías de costo a cada aerolínea en el DataFrame
    df['costo_aerolinea'] = df['aerolinea'].apply(asignar_costo)

    # Crear columnas para vuelos con y sin retraso
    df['sin_retraso_llegada'] = (df['retraso_llegada'] <= 15).astype(int)
    df['con_retraso_llegada'] = (df['retraso_llegada'] > 15).astype(int)

    # Agrupar por categoría de costo y sumar los valores de retrasos y no retrasos
    vuelos_aerolinea = df.groupby('costo_aerolinea').agg({
        'sin_retraso_llegada': 'sum',
        'con_retraso_llegada': 'sum'
    }).reset_index()

    # Crear el gráfico de barras
    fig = px.bar(vuelos_aerolinea, 
                 x='costo_aerolinea', 
                 y=['sin_retraso_llegada', 'con_retraso_llegada'],
                 title='Número de Vuelos con y sin Retraso por Costo de Aerolínea',
                 labels={'value': 'Número de Vuelos', 'costo_aerolinea': 'Costo de la Aerolínea', 'variable': 'Tipo de Vuelo'},
                 barmode='group', 
                 opacity=0.8)

    # Configuración adicional del layout
    fig.update_layout(
        title_x=0.5, 
        xaxis={'categoryorder': 'total descending'},
        xaxis_title='Costo de la Aerolínea',
        yaxis_title='Cantidad de Vuelos'
    )

    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig)
