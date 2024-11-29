import mysql.connector 
import pandas as pd

# Conectar a la base de datos 
conexion = mysql.connector.connect( 
                                   host="localhost", 
                                   user="root", 
                                   password="12345678", 
                                   database="bootcamps" )

# Obtener las fechas existentes 
consulta = "SELECT Fecha FROM seguidores_instagram t where t.Primary != 0 ORDER BY Fecha" 
df = pd.read_sql(consulta, conexion) 

# Convertir las fechas a una lista de pandas 
fechas_existentes = pd.to_datetime(df['Fecha']).to_list() 


# Crear un rango de fechas completo desde la primera hasta la última fecha existente 
fecha_inicio = '2024-01-01'
fecha_fin = max(fechas_existentes) 
rango_completo = pd.date_range(start=fecha_inicio, end=fecha_fin).to_list() 

# Identificar las fechas faltantes 
fechas_faltantes = set(rango_completo) - set(fechas_existentes) 

# Imprimir las fechas faltantes 

#print(fechas_faltantes)

# Crear un cursor para ejecutar las inserciones 
cursor = conexion.cursor() 

# Insertar las fechas faltantes 

for fecha in fechas_faltantes: 
    consulta_insercion = "INSERT INTO seguidores_instagram (Fecha) VALUES (%s)" 
    cursor.execute(consulta_insercion, (fecha.strftime('%Y-%m-%d'),)) 
# Confirmar los cambios 

conexion.commit() 
# Cerrar la conexión 
cursor.close() 
conexion.close() 
print("Fechas faltantes insertadas exitosamente.")
