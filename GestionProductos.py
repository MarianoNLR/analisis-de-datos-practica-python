import json
import ProductoAlimenticio
import ProductoElectronico
import Producto

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
    
    def leer_producto(self, codigo_producto):
        try:
            datos = self.leer_datos()
            mensaje_consola = ""
            if codigo_producto in datos:
                producto_datos = datos[codigo_producto]
                
                if 'fecha_vencimiento' in producto_datos:
                    producto = ProductoAlimenticio(**producto_datos)
                    mensaje_consola += """==== Producto Alimenticio ====\n"""
                else:
                    producto = ProductoElectronico(**producto_datos)
                    mensaje_consola += """==== Producto Electronico ====\n"""
                mensaje_consola += f"{producto}"
                print(mensaje_consola)
            else:
                print(f"No se ha encontrado un producto con el codigo: {codigo_producto}.")
                
        except Exception as error:
            print(f"Error al leer el producto: {error}")
            
    def agregar_producto(self, producto):
        pass
    
    def eliminar_producto(self):
        pass
    
    def actualizar_producto(self, codigo_producto):
        pass