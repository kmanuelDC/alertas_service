import json


def read_json_file(file_path):
    try:
        # Abre el archivo JSON
        with open(file_path, 'r') as file:
            # Carga el contenido del archivo en un diccionario de Python
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except json.JSONDecodeError:
        print(f"El archivo {file_path} no es un JSON válido.")

def write_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al escribir en el archivo {file_path}: {e}")