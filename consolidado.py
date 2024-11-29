import pandas as pd
import plotly.graph_objects as go

def graficos_consolidados_separados():
    # Leer el archivo CSV
    df = pd.read_csv('../proy/csv/consolidado_data.csv')

    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Establecer 'Fecha' como el índice
    df.set_index('Fecha', inplace=True)

    # Agrupar los datos por mes y calcular la suma de cada mes
    df_mensual = df.resample('M').sum()

    # Colores para las líneas de los gráficos
    colores = ['skyblue', 'lightgreen', 'salmon', 'blue', 'red', 'black']

    # Crear un diccionario para almacenar las figuras de cada métrica
    figuras = {}

    # Plotear cada métrica en su propio gráfico con colores diferentes
    for i, columna in enumerate(df_mensual.columns):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_mensual.index,
            y=df_mensual[columna],
            mode='lines+markers',
            name=columna,
            line=dict(color=colores[i % len(colores)])
        ))
        
        # Configurar el layout del gráfico
        fig.update_layout(
            title=f'Suma Mensual de {columna}',
            xaxis_title='Mes',
            yaxis_title='Valor',
            showlegend=True
        )
        
        # Añadir la figura al diccionario
        figuras[columna] = fig

    return figuras
