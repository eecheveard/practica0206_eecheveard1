import os

def guardar_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")

def leer_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10 para leer su tabla: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    nombre_archivo = f"tabla-{n}.txt"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            print(archivo.read())
    else:
        print(f"El archivo {nombre_archivo} no existe.")

# Llamar a la función
guardar_tabla_multiplicar()
leer_tabla_multiplicar()