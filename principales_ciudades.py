import pandas as pd
import plotly.graph_objects as go

def grafico_ciudades_instagram():
    # Leer el archivo CSV
    df = pd.read_csv('C:/Users/USUARIO/Documents/proy/csv/principales_ciudades_instagram.csv')

    # Verificar que los datos se han leído correctamente
    #print(df.head())

    # Asumiendo que las columnas del CSV son 'ciudad' y 'cantidad'
    ciudades = df['ciudad']
    valores = df['cantidad']

    # Crear el gráfico de torta
    fig = go.Figure(data=[go.Pie(labels=ciudades, values=valores, 
                                 marker=dict(colors=['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'lightgrey']),
                                 textinfo='percent+label')])

    # Configurar el layout del gráfico
    fig.update_layout(title='Distribución por Ciudad')

    return fig
