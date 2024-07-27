class Producto:
    def __init__(self, codigo_producto, nombre, precio, stock, marca, categoria):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.categoria = categoria
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def precio(self):
        return self.precio
    
    @property
    def stock(self):
        return self.stock
    
    @property
    def marca(self):
        return self.marca
    
    @property
    def categoria(self):
        return self.categoria
    
    def to_dict(self):
        return {
            "codigo_producto": self.codigo_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca,
            "categoria": self.categoria
        }
    
    def __str__(self):
        return f"""==== Detalles Producto ====
                Codigo: {self.codigo_producto}
                Nombre: {self.nombre}
                Precio: {self.precio}
                Stock: {self.stock}
                Marca: {self.marca}
                Categoria: {self.categoria}
                """