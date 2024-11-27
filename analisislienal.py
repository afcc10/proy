import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

def analisis_lineal():
    # Leer el archivo CSV
    df = pd.read_csv('C:/Users/USUARIO/Documents/proy/csv/consolidado_data.csv')

    # Convertir la columna 'Fecha' a datetime (opcional, si es necesario para otros análisis)
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Definir las variables independientes (X) y dependientes (y)
    X = df[['seguidores']]
    y = df['alcance']

    # Crear y ajustar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)

    # Realizar predicciones
    y_pred = model.predict(X)

    # Coeficientes del modelo
    coef = model.coef_[0]
    intercept = model.intercept_
    
    print("coeficiente ", model.coef_)
    print("intercepcion ", model.intercept_)
    print("score ", model.score(X,y))

    # Crear el gráfico de dispersión con la línea de regresión
    fig = px.scatter(df, x='seguidores', y='alcance', 
                     title='Análisis de Regresión Lineal: Alcance vs Seguidores',
                     labels={'seguidores': 'Seguidores', 'alcance': 'Alcance'})
    
    # Agregar la línea de regresión al gráfico
    fig.add_scatter(x=df['seguidores'], y=y_pred, mode='lines', name='Línea de Regresión')

    # Agregar texto con los coeficientes
    fig.add_annotation(x=max(df['seguidores']), y=max(y_pred),
                       text=f'y = {coef:.2f}x + {intercept:.2f}',
                       showarrow=False, font=dict(size=12, color='black'))
    
    

    return fig
