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

def eliminar_json():
    mostrar_json()
    id = input("Ingrese el ID del usuario que desea eliminar: ")
    llaves = datajson.keys()
    buscar = None
    for llave in llaves:
        if llave == id:
            buscar = llave
            break

    if not buscar:
        print("El usuario no existe, ingrese el ID correctamente")
        return

    datajson.pop(buscar)
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
