import json
import os
from productos.Producto import Producto
from productos.ProductoAlimenticio import ProductoAlimenticio
from productos.ProductoElectronico import ProductoElectronico


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
        try:
            datos = {}
            if os.path.exists(self.archivo) and os.path.getsize(self.archivo) > 0:
                datos = self.leer_datos()
            
                if producto.codigo_producto in datos.keys():
                    print(f"Ya existe un producto con el codigo proporcionado: {producto.codigo_producto}.")
                else:
                    datos[producto.codigo_producto] = producto.to_dict()
                    self.guardar_datos(datos)
                    print(f"Producto guardado exitosamente!")
            else:
                datos[producto.codigo_producto] = producto.to_dict()
                self.guardar_datos(datos)
                print(f"Producto guardado exitosamente!")
        except Exception as error:
            print(f"Error inesperado al guardar el nuevo producto: {error}")
    
    def eliminar_producto(self, codigo_producto):
        try:
            datos = self.leer_datos()
            if str(codigo_producto) in datos.keys():
                del datos[codigo_producto]
                self.guardar_datos(datos)
                print(f"El producto con codigo {codigo_producto} ha sido eliminado.")
            else:
                print(f"No se ha encontrado producto con el codigo proporcionado.")
        except Exception as error:
            print(f"Error inesperado al eliminar el producto: {error}")
    
    def actualizar_producto(self, codigo_producto, campo, valor):
        try:
            datos = self.leer_datos()
            if str(codigo_producto) in datos.keys():
                datos[codigo_producto][campo] = valor
                self.guardar_datos(datos)
                print(f"{campo} actualizado correctamente.")
            else:
                print(f"No existe producto con el codigo proporcionado.")
        except Exception as error:
            print(f"Error al actualizar producto: {error}")