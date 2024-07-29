import os 
from crud import *

# Separador de textos, para mejorar la apariencia en consola
def separador(): 
    print("**********************************************************")

#Función para limpiar consola 
def clear(): 
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
#Tuplas con las opciones del menú principal
menuPrincipal = ("1. JSON", "2. txt", "3. csv", "4. Salir del programa")
menuOpciones = ("1. Crear", "2. Mostrar", "3. Actualizar", "4. Eliminar", "5. Salir")

#Función que recorre las tuplas que tienen las opciones del menú
def recorrerMenu(menu): 
    print("Seleccione una opción del menú: ")
    separador()
    for elemento in menu:
        print(elemento)
    separador()
    opcion = input("Ingrese su opción: ")
    return opcion 

#Menú principal 
def menu_principal(): 
    while True: 
        print("¡Bienvenido al menú principal!")
        opcion = recorrerMenu(menuPrincipal)
        if opcion == "1": 
            menu_secundario("JSON")
        elif opcion == "2": 
            clear()
            print("Bienvenido a la sección 2")
        elif opcion == "3": 
            clear()
            print("Bienvenido a la sección 1")
        elif opcion == "4": 
            clear()
            print("Saliendo del programa")
            break
        else:
            clear()
            print("Opción incorrecta, por favor ingrese un valor correcto")

def menu_secundario(opcion): 
    while True: 
        print(f"¡Bienvenido al menú {opcion}")
        opcion = recorrerMenu(menuOpciones)
        if opcion == "1": 
            crear_json()
        elif opcion == "2": 
            clear()
            print("Bienvenido a la sección 2")
        elif opcion == "3": 
            clear()
            print("Bienvenido a la sección 1")
        elif opcion == "4": 
            clear()
            print("Saliendo del programa")
        elif opcion == "5": 
            clear()
            print("Saliendo del programa")
            break
        else:
            clear()
            print("Opción incorrecta, por favor ingrese un valor correcto")
menu_principal()