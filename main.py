import os
import platform
from productos.GestionProductos import GestionProductos
from productos.ProductoAlimenticio import ProductoAlimenticio
from productos.ProductoElectronico import ProductoElectronico

def limpiar_consola():
    #TODO
    pass

def mostrar_menu():
    print(
        """
========== Menú de Gestion de Productos =========
1. Agregar Producto Alimenticio
2. Agregar Producto Electronico
3. Buscar Producto por codigo
4. Actualizar Producto
5. Eliminar Producto
6. Listar todos los Productos
7. Salir
=================================================
        """)
    
def agregar_producto(gestion, opcion_producto):
    try:
        codigo_producto = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        marca = input("Ingrese la marca del producto: ")
        categoria = input("Ingrese una categoria para el producto: ")
        
        if opcion_producto == '1':
            fecha_vencimiento = input("Ingrese la fecha de vencimiento: ")
            es_libre_gluten = input("Es libre de gluten (y/n): ")
            while es_libre_gluten != 'y' and es_libre_gluten != 'n':
                print("Opciones invalida. Digite 'y' (si) o 'n' (no)")
                es_libre_gluten = input("Es libre de gluten: y/n")

            es_libre_gluten = True if es_libre_gluten == 'y' else False
            producto = ProductoAlimenticio(codigo_producto, nombre, precio, stock, marca, categoria, fecha_vencimiento, es_libre_gluten)
        else:
            color = input("Ingrese color para el producto:")
            meses_garantia = input("Ingrese los meses de garantias del producto:")
            producto = ProductoElectronico(codigo_producto, nombre, precio, stock, marca, categoria, color, meses_garantia)
        
        gestion.agregar_producto(producto)
        input("Presione Enter para continuar...")
    except Exception as error:
        print(f"Error: {error}")

def buscar_producto_por_codigo(gestion):
    codigo = input("Ingrese el codigo del producto: ")
    gestion.leer_producto(codigo)
    input("Presione Enter para continuar...")

def eliminar_producto(gestion):
    codigo = input("Ingrese el codigo del producto: ")
    gestion.eliminar_producto(codigo)
    input("Presione Enter para continuar...")

if __name__ == "__main__":
    archivo_productos = 'productos_db.json'
    gestion = GestionProductos(archivo_productos)
    
    while True:
        mostrar_menu()
        print("Seleccione una de las opciones:", end = ' ')
        opcion = input()
        
        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        elif opcion == '3':
            buscar_producto_por_codigo(gestion)
        elif opcion == '4':
            #TODO Actualizar producto
            pass
        elif opcion == '5':
            eliminar_producto(gestion)
            pass
        elif opcion == '6':
            #TODO Listar productos
            pass
        elif opcion == '7':
            break;
        else: 
            print('Opcion inválida.')
        