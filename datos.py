import json

#Función para leer un archivo json
def cargarDatos (archivo): 
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error al cargar los datos {e}")


def guardarDatos (archivo, data): 
    try: 
        with open(archivo, "w", encoding="utf-8") as file: 
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos {e}")