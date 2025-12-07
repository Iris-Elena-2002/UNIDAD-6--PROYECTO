import os
import pickle

archivo_texto = "catalogo_museo.txt"
archivo_binario = "catalogo_museo.bin"

coleccion = []

def crear_archivo_texto():
    if not os.path.exists(archivo_texto):
        with open(archivo_texto, "w", encoding="utf-8") as f:
            f.write("Catálogo del Museo\n")
            f.write("===================\n\n")
        print ("Archivo de texto creado exitosamente.")

def guardar_caracteristicas_museo(caracteristicas):
    try:
        with open(archivo_texto, "a", encoding="utf-8") as f:
            f.write(f"Nombre: {caracteristicas['nombre']}\n")
            f.write(f"Artista: {caracteristicas['artista']}\n")
            f.write(f"Año de creacion: {caracteristicas['ano_creacion']}\n")
            f.write(f"Tipo de Museo: {caracteristicas['tipo_museo']}\n")
            f.write("-------------------\n")
        print("Características del museo guardadas exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar las características del museo: {e}")

def leer_coleccion_museo():
    try:
        with open(archivo_texto, "r", encoding="utf-8") as f:
            contenido = f.read()
            print("\nContenido del archivo de texto del museo:\n")
            print(contenido)
    except FileNotFoundError:
        print("El archivo de texto del museo no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo de texto del museo: {e}")

def buscar_exhibicion(titulo_buscar,coleccion):
    try:
        print("\n Buscar una exhibición por título \n")
        titulo_buscar = input("Ingrese el título de la exhibición a buscar: ").lower().strip()
        encontrado = False
        for exhibicion in coleccion:
            if exhibicion["título"].lower().strip() == titulo_buscar:
                print(f"\n Exhibición encontrada: {exhibicion['título']} | {exhibicion['artista']} | {exhibicion['año_creacion']} | {exhibicion['tipo']}\n")
                encontrado = True
        if not encontrado:
            print(f"\n La exhibición '{titulo_buscar}' no se encontró en la colección.\n")
    except Exception as e:
        print("Ocurrió un error al buscar la exhibición. Por favor, intente nuevamente.")

def guardar_binario_museo(coleccion):
    try:
        with open(archivo_binario, "wb") as binario:
            pickle.dump(coleccion, binario)
        print("\n Colección guardada en formato binario.\n") 
    except Exception as e:
        print(f"Ocurrió un error al guardar la colección en formato binario: {e}")

def leer_datos_binario_museo(coleccion):
    try:
        with open(archivo_binario, "rb") as binario:
            coleccion = pickle.load(binario)
            print("\n Colección cargada desde formato binario:\n")
            for exhibicion in coleccion:
                print(f"Título: {exhibicion['título']}, Artista: {exhibicion['artista']}, Año de Creación: {exhibicion['año_creacion']}, Tipo: {exhibicion['tipo']}")
    except FileNotFoundError:
        print("El archivo binario del museo no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo binario del museo: {e}")

def main(opcion):
    while True:
        print("Menú del Museo")
        print("1. Crear archivo de texto del museo")
        print("2. Guardar características del museo")
        print("3. Leer colección del museo desde archivo de texto")
        print("4. Buscar exhibición por título")
        print("5. Guardar colección en formato binario")
        print("6. Leer colección desde formato binario")
        print("7. Salir")

        if opcion == "1":
            crear_archivo_texto()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del museo: ")
            artista = input("Ingrese la ubicación del museo: ")
            ano_creacion = input("Ingrese el año de fundación del museo: ")
            tipo_museo = input("Ingrese el tipo de museo: ")
            caracteristicas = {
                "nombre": nombre,
                "artista": artista,
                "ano_creacion": ano_creacion,
                "tipo_museo": tipo_museo
                }
            guardar_caracteristicas_museo(caracteristicas)
        elif opcion == "3":
            leer_coleccion_museo()
        elif opcion == "4":
            titulo = input("Ingrese el título de la exhibición a buscar: ")
            buscar_exhibicion(titulo, coleccion)
        elif opcion == "5":
            guardar_binario_museo(coleccion)
        elif opcion == "6":
            leer_datos_binario_museo()
        elif opcion == "7":
            print("Saliendo del programa del museo.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
