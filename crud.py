from datos import *
# Crud para JSON
def crear_json(): 
    cargar_datos_json()
    usuario={}

    id = input("Ingresa tu id: ")
    usuario["nombre"] = input("Ingresa tu nombre: ")
    usuario["telefono"] = input("Ingresa tu teléfono: ")

    datajson[id] = usuario
    guardar_datos_json()

def mostrar_json():
    cargar_datos_json()
    for id, informacion in datajson.items():
        print(f"* ID: {id} ")
        for clave, valor in informacion.items():
            print(f"- {clave}: {valor}")

def buscarid(id): 
    llaves = datajson.keys()
    buscar = None
    for llave in llaves:
        if llave == id:
            buscar = llave
            return buscar


def actualizar_json():
    mostrar_json()
    id = input("Ingrese el ID del usuario que desea actualizar: ")
    id_encontrado = buscarid(id)
    if not id_encontrado: 
        print("El usuario no existe")
        return
    while True: 
        campo = input("Seleccione el campo que desea actualizar: ").lower()
        if campo == "nombre":
            datajson[id_encontrado]["nombre"] = input("Ingrese el nuevo nombre: ")
            break
        elif campo == "telefono":
            datajson[id_encontrado]["telefono"] = input("Ingrese el nuevo telefono: ")
            break
        else: 
            print("Campo incorrecto, por favor escriba correctamente el campo")
    print("Dato actualizado")
    guardar_datos_json()

def eliminar_json():
    mostrar_json()
    id = input("Ingrese el ID del usuario que desea eliminar: ")
    id_encontrado = buscarid(id)

    if not id_encontrado:
        print("El usuario no existe")
        return

    datajson.pop(id_encontrado)
    print("Usuario eliminado")
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
