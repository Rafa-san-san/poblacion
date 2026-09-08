import requests
from bs4 import BeautifulSoup
import pandas as pd
# Guardar el script completo en un archivo .py local
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/?utm_source=chatgpt.com/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
poblacion = soup.find_all("table")

def extraer_tabla(tabla):
    datos = []

    for tr in tabla.find_all("tr"):
        fila = []

        for td in tr.find_all(["th", "td"]):
            fila.append(td.get_text(strip=True))

        if fila:
            datos.append(fila)

    return datos

datos = extraer_tabla(poblacion[0])
columnas = datos[0]
filas = datos[1:]
df = pd.DataFrame(filas, columns=columnas)
df = df.set_index("#")
df.to_csv("poblacion.csv", index=False)
print("Scraping exitoso y archivo catalogo_libros.csv creado.")
"""

with open("scraper.py", "w", encoding="utf-8") as f:
    f.write(script_code)
