from productos.Producto import Producto
import datetime

class ProductoAlimenticio(Producto):
    def __init__(self, codigo_producto, nombre, precio, stock, marca, categoria, fecha_vencimiento, es_libre_gluten):
        super().__init__(codigo_producto, nombre, precio, stock, marca, categoria)
        self._fecha_vencimiento = self.validar_fecha_vencimiento(fecha_vencimiento)
        self._es_libre_gluten = es_libre_gluten
        
    @property
    def fecha_vencimiento(self):
        return self._fecha_vencimiento

    @property
    def es_libre_gluten(self):
        return self._es_libre_gluten

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, nueva_fecha):
        self._fecha_vencimiento = self.validar_fecha_vencimiento(nueva_fecha)
    
    def validar_fecha_vencimiento(self, fecha):
        try:
            objeto_fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            if objeto_fecha <= datetime.datetime.now().date():
                raise ValueError(f"La fecha de vencimiento debe ser mayor a la fecha actual!")
            return fecha
        except ValueError as error:
            raise ValueError(f"Error al cargar la fecha de vencimiento: La fecha se debe ingresar con el formato DD/MM/YYYY")
        except Exception as error:
            raise Exception(f"Ocurrio un error al ingresar la fecha de vencimiento")
    
    def to_dict(self):
        data = super().to_dict()
        data["fecha_vencimiento"] = self._fecha_vencimiento
        data["es_libre_gluten"] = self._es_libre_gluten
        return data
        
    def __str__(self): 
        return f"""{super().__str__()}Fecha Vencimiento: {self._fecha_vencimiento}
Libre de gluten: {self._es_libre_gluten}"""