import json

#Función para leer y guardar un archivo json
datajson = {}
rutaJSON = "data\datos.json"

def cargar_datos_json(): 
    try:
        with open(rutaJSON, "r", encoding="utf-8") as file:
            datajson.update(json.load(file))
    except Exception as e:
        print(f"Error al cargar los datos {e}")

def guardar_datos_json(): 
    try: 
        with open(rutaJSON, "w", encoding="utf-8") as file: 
            json.dump(datajson, file, indent=4, ensure_ascii=False)
    except Exception as e: 
            print(f"Error al guardar los datos {e}")

#Función para leer y guardar un archivo json
rutaTXT = "data\datos.txt"

def cargar_datos_txt(): 
    try: 
        with open(rutaTXT, "r") as file:
            contenido = file.read()
        return contenido
    except Exception as e: 
        print(f"Error al cargar los datos {e}")

def guardar_datos_txt(contenido):
    try: 
        with open(rutaTXT, "a") as file:
            file.write(contenido + "\n")
    except Exception as e: 
        print(f"Error al guardar los datos {e}")
