import Producto


class ProductoElectronico(Producto): 
    def __init__(self, nombre, precio, stock, marca, categoria, color, meses_garantia):
        super().__init__(nombre, precio, stock, marca, categoria)
        self.color = color
        self.meses_garantia = meses_garantia
    
    @property
    def color(self):
        return self.color
    
    @property
    def meses_garantia(self): 
        return self.meses_garantia
    
    def to_dict(self):
        data = super().to_dict()
        data["color"] = self.color
        data["meses_garantia"] = self.meses_garantia
        
        return data
    
    def __str__(self):
        return f"""{super().__str__()}
                Color: {self.color}
                Garantia: {self.meses_garantia} (Meses)"""