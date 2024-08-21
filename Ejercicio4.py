class DispositivoElectronico:
    def __init__(self, tipo, categoria, modelo, pantalla, resolucion, almacenamiento, procesador, velocidad_procesador, ram, frecuencia_ram, bateria, camara, conectividad, peso, sistema_operativo, precio_compra):
        self.tipo = tipo
        self.categoria = categoria
        self.marca = "PHR"
        self.modelo = modelo
        self.pantalla = pantalla 
        self.resolucion = resolucion 
        self.almacenamiento = almacenamiento  
        self.procesador = procesador
        self.velocidad_procesador = velocidad_procesador 
        self.ram = ram  
        self.frecuencia_ram = frecuencia_ram  
        self.bateria = bateria 
        self.camara = camara 
        self.peso =peso
        self.conectividad = conectividad  
        self.sistema_operativo = sistema_operativo  
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7  
        self.origen = "Importado"

    def mostrar_informacion(self):
        print(f"{self.tipo} {self.categoria} {self.marca} {self.modelo}")
        print(f"Pantalla: {self.pantalla} pulgadas, Resolución: {self.resolucion}")
        print(f"Almacenamiento: {self.almacenamiento} GB, Procesador: {self.procesador} ({self.velocidad_procesador} GHz)")
        print(f"RAM: {self.ram} GB ({self.frecuencia_ram} MHz), Batería: {self.bateria} mAh")
        print(f"Cámara: {self.camara} MP, Conectividad: {self.conectividad}")
        print(f"Peso: {self.peso} gramos, Sistema Operativo: {self.sistema_operativo}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}, Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Origen: {self.origen}\n")

# Ejemplo de uso
dispositivos = [
    DispositivoElectronico("Celular", "Gama Alta", "t ultra", 6.5, "1080x2400", 128, "Samsung 888", 2.84, 8, 3200, 4500, 108, "5G, WiFi 6, Bluetooth 5.0", 200, "Android", 300.0),
    DispositivoElectronico("Tablet", "Gama Media", "Tab Pro", 10.1, "2048x1536", 256, "Apple A12Z", 2.49, 6, 2133, 7000, 12, "WiFi 5, Bluetooth 4.2", 450, "iOS", 500.0),
    DispositivoElectronico("Portátil", "Gama Alta", "Laptop Ultra", 15.6, "3840x2160", 512, "Intel Core i7", 3.6, 16, 3200, 8000, 20, "WiFi 6, Bluetooth 5.1", 1500, "Windows 11", 1000.0)
]

for dispositivo in dispositivos:
    dispositivo.mostrar_informacion()