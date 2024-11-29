import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def regresion_lineal_visitas_seguidores():
    # Leer el archivo CSV
    df = pd.read_csv("../proy/csv/consolidado_data.csv")

    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Asegurarse de que las columnas relevantes sean numéricas
    df["seguidores"] = pd.to_numeric(df["seguidores"], errors='coerce')
    df["visitas"] = pd.to_numeric(df["visitas"], errors='coerce')

    # Seleccionar las variables independientes y dependientes
    X = df[['visitas']]
    y = df['seguidores']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Crear el modelo de regresión lineal
    model = LinearRegression()

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = model.predict(X_test)

    # Evaluar el modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    intercept = model.intercept_
    coef = model.coef_[0]

    # Crear el gráfico con Plotly
    fig = px.scatter(df, x='visitas', y='seguidores', title='Regresión Lineal: Visitas vs Seguidores', labels={'visitas': 'Visitas', 'seguidores': 'Seguidores'})
    fig.add_scatter(x=X_test['visitas'], y=y_pred, mode='lines', name=f'Regresión Lineal<br>Intercepto: {intercept:.2f}<br>Coeficiente: {coef:.2f}<br>R²: {r2:.2f}', line=dict(color='red'))

    return fig