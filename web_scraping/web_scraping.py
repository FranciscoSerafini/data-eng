from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #opciones para web scrapping
from selenium.webdriver.support.ui import Select #nos va permitir seleccionar valores dentro de una lista desplegable por ej
import pandas as pd

# Definición de la ruta del driver
ruta_driver = "C:\\Users\\54346\\Desktop\\CURSOS\\Ingenieria de datos\\Python\\Intermedio\\chromedriver-win64\\chromedriver.exe"

# Definición del sitio web
web_site = 'https://www.adamchoi.co.uk/teamgoals/detailed'

# Crear un servicio con la ruta del driver
service = Service(ruta_driver)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicializar el controlador de Chrome usando el servicio
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrir el sitio web
driver.get(web_site)
#buscame un nodo que tenga nombre de tag nodo y buscame un atributo que tenga de nombre
botonPartidos = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]') 
botonPartidos.click()

lista_desplegable = Select(driver.find_element(By.ID,'country'))
lista_desplegable.select_by_visible_text('Spain')

partidos = driver.find_elements(By.TAG_NAME,'tr') #detectamos un patron entre los partidos


data_partidos = []
for partido in partidos:
    data_partidos.append(partido.text)


driver.quit()
#traemos pandas para guardar la info en un csv
df = pd.DataFrame({'partidos':data_partidos})
print(df)
df.to_csv('PartidosLigaEspañola.csv', index=False)

