import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def modelo_regresion_lineal():
    # Leer el archivo CSV
    df = pd.read_csv("C:/Users/USUARIO/Documents/proy/csv/consolidado_data.csv")

    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Asegurarse de que las columnas relevantes sean numéricas
    df["alcance"] = pd.to_numeric(df["alcance"], errors='coerce')
    df["seguidores"] = pd.to_numeric(df["seguidores"], errors='coerce')
    df["visitas"] = pd.to_numeric(df["visitas"], errors='coerce')

    # Seleccionar las variables independientes y dependientes
    X = df[['seguidores', 'visitas']]
    y = df['alcance']

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

    print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
    print(f"Coeficiente de Determinación (R^2): {r2:.2f}")

    # Visualizar los resultados con plotly
    fig1 = px.scatter(x=X_test['visitas'], y=y_test, title='Valores Reales vs Predicciones: Alcance vs Visitas', labels={'x': 'Visitas', 'y': 'Alcance'}, color_discrete_sequence=['blue'])
    fig1.add_scatter(x=X_test['visitas'], y=y_pred, mode='markers', marker=dict(color='red'), name='Predicciones')
    
    fig2 = px.scatter(x=X_test['seguidores'], y=y_test, title='Valores Reales vs Predicciones: Alcance vs Seguidores', labels={'x': 'Seguidores', 'y': 'Alcance'}, color_discrete_sequence=['blue'])
    fig2.add_scatter(x=X_test['seguidores'], y=y_pred, mode='markers', marker=dict(color='red'), name='Predicciones')

    return fig1, fig2
