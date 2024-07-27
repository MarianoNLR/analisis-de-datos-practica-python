import json

class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo
        
    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as archivo:
                lectura = json.load(archivo)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se ha encontrado el archivo.")
        except Exception as error: 
            raise Exception(f"Error al leer el archivo: {error}")
        else: 
            return lectura
    
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as archivo:
                json.dump(datos, archivo, indent=4)
        except IOError as error:
            print(f"Error al intentar guardar los datos en el archivo: {error}")
        except Exception as error:
            print(f"Error Inesperado: {error}")