from functions import extraccion, load, transform
import logging
from connection import  conexion_db

if __name__ == "__main__":
    # Conectar a la base de datos
    connection = conexion_db()

    if connection is not None:

        # Extracción de datos
        data = extraccion()

        # Transformación de datos
        dataframes = transform(data)

        # Carga de datos a SQL Server
        try:
            load(dataframes, connection)  # Asegúrate de que load esté bien implementado
        except Exception as e:
            logging.error(f"Error durante la carga de datos: {e}")

        # Cerrar la conexión
        connection.close()
