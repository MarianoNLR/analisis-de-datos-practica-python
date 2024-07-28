class Producto:
    def __init__(self, codigo_producto, nombre, precio, stock, marca, categoria):
        self._codigo_producto = codigo_producto
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._marca = marca
        self._categoria = categoria
    
    @property
    def codigo_producto(self):
        return self._codigo_producto
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def stock(self):
        return self._stock
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def categoria(self):
        return self._categoria
    
    def to_dict(self):
        return {
            "codigo_producto": self.codigo_producto,
            "nombre": self._nombre,
            "precio": self._precio,
            "stock": self._stock,
            "marca": self._marca,
            "categoria": self._categoria
        }
    
    def __str__(self):
        return f"""========== Detalles Producto ==========
Codigo: {self._codigo_producto}
Nombre: {self._nombre}
Precio: {self._precio}
Stock: {self._stock}
Marca: {self._marca}
Categoria: {self._categoria}
"""