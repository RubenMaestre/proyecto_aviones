import streamlit as st
import plotly.express as px

def graficar_vuelos_por_aerolinea(df):
    # Asegúrate de que 'aerolinea' sea el nombre correcto de la columna en tu DataFrame
    vuelos_aerolinea = df.groupby(['aerolinea']).size().reset_index(name='Número total de vuelos')

    # Crear la figura con Plotly
    fig = px.bar(data_frame=vuelos_aerolinea,
                 x='Aerolineas',
                 y='Número total de vuelos',
                 opacity=0.8,
                 title="Cantidad de vuelos nacionales por compañía aérea en Estados Unidos",
                 color='Aerolineas',
                 category_orders={"aerolinea": ["American Airlines"]})  # Ordena para que American Airlines aparezca primero

    # Ajustar el tamaño de la gráfica y actualizar otros aspectos del layout
    fig.update_layout(
        title_x=0.5,
        xaxis_title='Compañías aéreas',
        yaxis_title='Cantidad total de vuelos',
        xaxis={'categoryorder': 'total descending'},
        width=1280,
        height=720
    )

    # Actualizar la leyenda para mostrar solo American Airlines
    fig.for_each_trace(lambda t: t.update(showlegend=True if t.name == "American Airlines" else False))

    # Texto instructivo sobre la interacción con la gráfica
    st.markdown("Haz click en la leyenda para filtrar y ver la evolución de vuelos de una aerolínea específica.")

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
