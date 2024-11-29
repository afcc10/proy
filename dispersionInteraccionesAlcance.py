import pandas as pd
import plotly.express as px

def grafico_dispersion():
    # Leer el archivo CSV
    df = pd.read_csv('../proy/csv/consolidado_data.csv')

    # Crear el gráfico de dispersión comparando interacciones y alcance
    fig = px.scatter(df, x='interacciones', y='alcance', 
                     title='Relación entre Interacciones y alcance',
                     labels={'interacciones': 'Interacciones', 'alcance': 'Alcance'})

    return fig


""""
import pandas as pd
import plotly.express as px

def grafico_dispersion():
    # Leer el archivo CSV
    df = pd.read_csv('C:/Users/USUARIO/Documents/proy/csv/consolidado_data.csv')

    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Crear el gráfico de dispersión sin agrupar por mes
    fig = px.scatter(df, x='Fecha', y='alcance', 
                     title='Relación entre Alcance e Interacciones',
                     labels={'Fecha': 'Fecha', 'alcance': 'Alcance'})
    
    fig.add_scatter(x=df['Fecha'], y=df['interacciones'], mode='lines+markers', name='Interacciones')

    return fig


import pandas as pd
import plotly.express as px

def grafico_dispersion():
    # Leer el archivo CSV
    df = pd.read_csv('C:/Users/USUARIO/Documents/proy/csv/consolidado_data.csv')

    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Agrupar por mes y calcular la suma de cada mes
    df_mensual = df.resample('M', on='Fecha').sum().reset_index()

    # Crear el gráfico de dispersión
    fig = px.scatter(df_mensual, x='Fecha', y='alcance', 
                     title='Relación entre Alcance e Interacciones (Agrupado por Mes)',
                     labels={'Fecha': 'Fecha', 'value': 'Valor'})
    
    fig.add_scatter(x=df_mensual['Fecha'], y=df_mensual['interacciones'], mode='markers', name='Interacciones')

    return fig
"""
