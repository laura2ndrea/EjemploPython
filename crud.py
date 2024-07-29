from datos import *

def crear_json(): 
    cargar_datos_json()
    usuario={}

    id = input("Ingresa tu id: ")
    usuario["nombre"] = input("Ingresa tu nombre: ")
    usuario["telefono"] = input("Ingresa tu teléfono: ")

    datajson[id] = usuario
    guardar_datos_json()

def crear_txt(): 
    contenido = cargar_datos_txt()
    print(contenido)
    nota = input("Escriba una nota que desea guardar: ")
    guardar_datos_txt(nota)
