import requests
import gzip

def descargar_datos(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return gzip.decompress(respuesta.content).decode('utf-8')
    return None

def obtener_pib(datos, pais):
    for linea in datos.split('\n'):
        if linea.startswith(pais):
            print(linea.replace('\t', ' '))
            return
    print("País no encontrado.")

url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
datos = descargar_datos(url)

if datos:
    pais = input("Introduce las iniciales del país (por ejemplo, 'DE' para Alemania): ").strip().upper()
    obtener_pib(datos, pais)