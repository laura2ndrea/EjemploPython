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

def crear_csv(): 
    tiempos = cargar_datos_csv()
    for elemento in tiempos: 
        print(elemento)
    registro = []
    tiempo = input("Ingrese el tiempo realizado: ")
    nombre = input("Ingrese su nombre: ")
    registro.append(tiempo)
    registro.append(nombre)
    tiempos.append(registro)
    guardar_datos_csv(tiempos)
