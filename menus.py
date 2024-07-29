import os 

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
menuPrincipal = ("1. Opción 1", "2. Opción 2", "3. Opción 3", "4. Salir del programa")

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
while True: 
    print("¡Bienvenido al menú principal!")
    opcion = recorrerMenu(menuPrincipal)
    if opcion == "1": 
        clear()
        print("Bienvenido a la sección 1")
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