import requests
import logging
import pandas as pd
import matplotlib.pyplot as plt
from connection import conexion_db

# Función para extraer desde las API de cripto
def extraccion():
    monedas = {'BTC':'bitcoin', "ETH":"ethereum", "ADA":"cardano"}
    data_historica = {}  # Guardaremos la información de las monedas extraídas de la API
    
    for coins, id in monedas.items():
        url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency=usd&days=365"
        logging.info(f"Se extrae información de la moneda {coins}...")
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            data = respuesta.json()
            data_historica[coins] = data['prices']
            logging.info(f"Correctamente la extracción {coins}")
        else:
            logging.error(f'Error en la extracción de {coins}: {respuesta.status_code}')

    return data_historica

def transform(data):
    data_frames = {}  # Creamos un diccionario para guardar los DataFrames
    
    for coins, precios in data.items():
        df = pd.DataFrame(precios, columns=['marca_tiempo', 'precio'])
        df['marca_tiempo'] = pd.to_datetime(df['marca_tiempo'], unit='ms')
        data_frames[coins] = df
    
    return data_frames

def load(dataframes, conexion):
    try:
        with conexion.cursor() as cursor:
            for moneda, df in dataframes.items():
                for i, r in df.iterrows():
                    insert_query = """
                    INSERT INTO precios_criptos (moneda, marca_tiempo, precio)
                    VALUES (?, ?, ?)
                    """
                    cursor.execute(insert_query, moneda, r['marca_tiempo'], r['precio'])
            conexion.commit()
            logging.info('Datos cargados correctamente')
    except Exception as e:
        logging.error(f"Error durante la carga de datos: {e}")
        conexion.rollback()  # Revertir cambios en caso de error
