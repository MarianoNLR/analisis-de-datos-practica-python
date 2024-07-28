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
    producto = gestion.leer_producto(codigo)
    input("Presione Enter para continuar...")
    return producto

def eliminar_producto(gestion):
    codigo = input("Ingrese el codigo del producto: ")
    gestion.eliminar_producto(codigo)
    input("Presione Enter para continuar...")

def listar_productos(gestion): 
    productos = gestion.leer_datos()
    
    for producto in productos.values():
        if 'fecha_vencimiento' in producto:
            print(f"{ProductoAlimenticio(**producto)}")
        else:
            print(f"{ProductoElectronico(**producto)}")
        print("==========================================")
    input("Presione Enter para continuar...")

def actualizar_producto(gestion):
    producto = buscar_producto_por_codigo(gestion)
    print("========== Menú de Actualizacion ==========")
    opcion_valida = False
    opciones_campos = {
        '1': "nombre",
        '2': "precio",
        '3': "stock",
        '4': "marca",
        '5': "categoria",
    }
    while True:
        mostrar_menu_actualizar_campos(producto)
        opcion = input("Seleccione el campo que desea actualizar: ")
        
        if opcion == '8':
            break
        
        campo = opciones_campos.get(opcion)
            
        if opcion == '6':
            if 'fecha_vencimiento' in producto:
                campo = "fecha_vencimiento"
            else:
                campo = "color"
        if opcion == '7':
            if 'fecha_vencimiento' in producto:
                campo = "es_libre_gluten"
            else:
                campo = "meses_garantia"

        if campo is None:
            print("Ingrese una opcion válida")
            continue
        
        print(f"Campo a actualizar: {campo}")
        valor = input(f"Nuevo {campo}: ")
        '''
        #     opcion_valida = True
        # if opcion == '1':
        #     campo = "nombre"
        #     opcion_valida = True
        # if opcion == '2':
        #     campo = "precio"
        #     opcion_valida = True
        # if opcion == '3':
        #     campo = "stock"
        #     opcion_valida = True
        # if opcion == '4':
        #     campo = "marca"
        #     opcion_valida = True
        # if opcion == '5':
        #     campo = "categoria"
        #     opcion_valida = True
        # if opcion == '6':
        #     if 'fecha_vencimiento' in producto:
        #         campo = "fecha_vencimiento"
        #     else:
        #         campo = "color"
        # if opcion == '7':
        #     if 'fecha_vencimiento' in producto:
        #         campo = "es_libre_gluten"
        #     else:
        #         campo = "meses_garantia"
        #     opcion_valida = True
        # if opcion == '8':
        #     break
        
        # if not opcion_valida:
        #     print("Ingrese una opcion valida.")
        '''
        gestion.actualizar_producto(producto['codigo_producto'], campo, valor)
        input("Presione Enter para continuar...")

def mostrar_menu_actualizar_campos(producto):
    menu = """
========= Seleccione el campo a actualizar =========
1.Nombre.
2.Precio.
3.Stock.
4.Marca.
5.Categoria.
"""
    if 'fecha_vencimiento' in producto:
        menu += """6.Fecha de Vencimiento.
7.Libre de gluten.
8.Salir."""
    else:
        menu += """6.Color.
7.Meses de garantía.
8.Salir."""
        
    print(menu)

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
            producto_datos = buscar_producto_por_codigo(gestion)
            mensaje_consola = ""
            if 'fecha_vencimiento' in producto_datos:
                producto = ProductoAlimenticio(**producto_datos)
                mensaje_consola += """==== Producto Alimenticio ====\n"""
            else:
                producto = ProductoElectronico(**producto_datos)
                mensaje_consola += """==== Producto Electronico ====\n"""
            mensaje_consola += f"{producto}"
            print(mensaje_consola)
        elif opcion == '4':
            actualizar_producto(gestion)
        elif opcion == '5':
            eliminar_producto(gestion)
            pass
        elif opcion == '6':
            listar_productos(gestion)
            pass
        elif opcion == '7':
            break;
        else: 
            print('Opcion inválida.')
        