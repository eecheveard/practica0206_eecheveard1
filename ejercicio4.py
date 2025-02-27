import requests

def contar_palabras_en_url(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() 
        contenido = respuesta.text
        palabras = contenido.split()
        return len(palabras)
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return None

url = "https://www.marca.com/" 
num_palabras = contar_palabras_en_url(url)

if num_palabras is not None:
    print(f"El archivo contiene {num_palabras} palabras.")
