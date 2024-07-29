from datos import *

def crear_json(): 
    cargar_datos()
    usuario={}

    id = input("Ingresa tu id: ")
    usuario["nombre"] = input("Ingresa tu nombre: ")
    usuario["telefono"] = input("Ingresa tu teléfono: ")

    data[id] = usuario
    guardar_datos()

