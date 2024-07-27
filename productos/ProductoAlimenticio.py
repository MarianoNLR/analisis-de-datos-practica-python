from productos.Producto import Producto

class ProductoAlimenticio(Producto):
    def __init__(self, codigo_producto, nombre, precio, stock, marca, categoria, fecha_vencimiento, es_libre_gluten):
        super().__init__(codigo_producto, nombre, precio, stock, marca, categoria)
        self._fecha_vencimiento = fecha_vencimiento
        self._es_libre_gluten = es_libre_gluten
        
    @property
    def fecha_vencimiento(self):
        return self._fecha_vencimiento

    @property
    def es_libre_gluten(self):
        return self._es_libre_gluten
    
    def to_dict(self):
        data = super().to_dict()
        data["fecha_vencimiento"] = self._fecha_vencimiento
        data["es_libre_gluten"] = self._es_libre_gluten
        return data
        
    def __str__(self): 
        return f"""{super().__str__()}Fecha Vencimiento: {self._fecha_vencimiento}
        Libre de gluten: {self._es_libre_gluten}"""