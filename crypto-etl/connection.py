import pyodbc

def conexion_db():
    try:
        conec = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-9345VIR,1433;'
            'DATABASE=cripto_db;'  # Conéctate a la base de datos ya existente
            'Trusted_Connection=yes;'
        )
        print('Conexión exitosa')
        return conec
    except Exception as e:
        print('Error en la conexión a la base de datos', e)
        return None
