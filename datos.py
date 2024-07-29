import json

#Función para leer y guardar un archivo json
data = {}
rutaJSON = "data\datos.json"

def cargar_datos(): 
    try:
        with open(rutaJSON, "r", encoding="utf-8") as file:
            data.update(json.load(file))
    except Exception as e:
        print(f"Error al cargar los datos {e}")

def guardar_datos(): 
    try: 
        with open(rutaJSON, "w", encoding="utf-8") as file: 
            json.dump(file, data, indent=4, ensure_ascii=False)
    except Exception as e: 
            print(f"Error al guardar los datos {e}")