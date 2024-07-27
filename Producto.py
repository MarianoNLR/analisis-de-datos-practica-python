class Producto:
    def __init__(self, nombre, precio, stock, marca, categoria):
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
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca,
            "categoria": self.categoria
        }
    
    def __str__(self):
        return f"""==== Detalles Producto ====
                Nombre: {self.nombre}
                Precio: {self.precio}
                Stock: {self.stock}
                Marca: {self.marca}
                Categoria: {self.categoria}
                """