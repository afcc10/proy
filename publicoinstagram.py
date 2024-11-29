import pandas as pd
import plotly.graph_objects as go

def grafico_rango_edad_genero():
    # Leer el archivo CSV
    df = pd.read_csv("../proy/csv/publico_instagram.csv")

    # Crear el gráfico de barras apiladas
    fig = go.Figure(data=[
        go.Bar(name='Mujeres', x=df['Rango_edad'], y=df['Mujeres'], marker_color='lightcoral',
               text=df['Mujeres'], textposition='inside'),
        go.Bar(name='Hombres', x=df['Rango_edad'], y=df['Hombres'], marker_color='lightblue',
               text=df['Hombres'], textposition='inside')
    ])

    # Configurar el layout del gráfico
    fig.update_layout(barmode='stack', 
                      title='Distribución por Rango de Edad y Género',
                      xaxis_title='Rango de Edad',
                      yaxis_title='Porcentaje',
                      legend_title='Género')

    return fig
