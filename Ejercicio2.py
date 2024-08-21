class Articulo:
    nombre = ""
    marca = ""
    precio_compra = 0.0
    precio_venta = 0.0
    
   
    def __init__(self, nombre, marca, precio_compra):
        self.nombre = nombre
        self.marca = marca
        self.precio_compra = precio_compra
        self.calcular_precio_venta()

    def calcular_precio_venta(self):
        self.precio_venta = self.precio_compra * 1.30
    
    
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Marca:", self.marca)
        print("Precio de Compra: $", self.precio_compra)
        print("Precio de Venta: $", round(self.precio_venta, 2))
        print("___________________________")


class Cuaderno(Articulo):
    def __init__(self, hojas, precio_compra):
        super().__init__(f"Cuaderno de {hojas} hojas", "HOJITAS", precio_compra)
        self.hojas = hojas


class Lapiz(Articulo):
    def __init__(self, tipo, precio_compra):
        super().__init__(f"Lápiz de {tipo}", "RAYAS", precio_compra)
        self.tipo = tipo


cuaderno1 = Cuaderno(50, 2)
cuaderno2 = Cuaderno(100, 3)
lapiz1 = Lapiz("grafito", 0.10)
lapiz2 = Lapiz("colores", 1)


cuaderno1.mostrar_datos()
cuaderno2.mostrar_datos()
lapiz1.mostrar_datos()
lapiz2.mostrar_datos()