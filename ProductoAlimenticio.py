import Producto

class ProductoAlimenticio(Producto):
    def __init__(self, codigo_producto, nombre, precio, stock, marca, categoria, fecha_vencimiento, es_libre_gluten):
        super().__init__(codigo_producto, nombre, precio, stock, marca, categoria)
        self.fecha_vencimiento = fecha_vencimiento
        self.es_libre_gluten = es_libre_gluten
        
    @property
    def fecha_vencimiento(self):
        return self.fecha_vencimiento

    @property
    def es_libre_gluten(self):
        return self.es_libre_gluten
    
    def to_dict(self):
        data = super().to_dict()
        data["fecha_vencimiento"] = self.fecha_vencimiento
        data["es_libre_gluten"] = self.es_libre_gluten
        
    def __str__(self): 
        f"""{super().__str__()}
                Fecha Vencimiento: {self.fecha_vencimiento}
                Libre de gluten: {self.es_libre_gluten}"""