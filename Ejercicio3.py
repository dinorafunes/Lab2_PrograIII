class Vehiculo:

    marca = ""
    modelo = ""
    año = 0
    color = ""
    motor = ""
    transmision = ""
    combustible = ""
    numero_puertas = 0
    precio_compra = 0.0
    precio_venta = 0.0
    nacionalidad = ""
    placa = ""
    

    ruedas = 4
    capacidad_pasajeros = 5

    def __init__(self, marca, modelo, año, color, motor, transmision, combustible, numero_puertas, precio_compra, nacionalidad, placa):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        self.transmision = transmision
        self.combustible = combustible
        self.numero_puertas = numero_puertas
        self.precio_compra = precio_compra
        self.nacionalidad = nacionalidad
        self.placa = placa
        self.calcular_precio_venta()


    def calcular_precio_venta(self):
        self.precio_venta = self.precio_compra * 1.4
    
    def mostrar_datos(self):
        print("╔═════════════════════════════════════════════╗")
        print("║               DETALLES DEL VEHÍCULO         ║")
        print("╠═════════════════════════════════════════════╣")
        print(f"║ Marca:              {self.marca:<30} ║")
        print(f"║ Modelo:             {self.modelo:<30} ║")
        print(f"║ Año:                {self.año:<30} ║")
        print(f"║ Color:              {self.color:<30} ║")
        print(f"║ Motor:              {self.motor:<30} ║")
        print(f"║ Transmisión:        {self.transmision:<30} ║")
        print(f"║ Combustible:        {self.combustible:<30} ║")
        print(f"║ Número de Puertas:  {self.numero_puertas:<30} ║")
        print(f"║ Precio de Compra: $  {self.precio_compra:<30}  ║")
        print(f"║ Precio de Venta:  $  {round(self.precio_venta, 2):<30} ║")
        print(f"║ Nacionalidad:       {self.nacionalidad:<30} ║")
        print(f"║ Placa:              {self.placa:<30} ║")
        print(f"║ Ruedas:             {self.ruedas:<30} ║")
        print(f"║ Capacidad Pasajeros:{self.capacidad_pasajeros:<30} ║")
        print("╚═════════════════════════════════════════════╝")

def registrar_vehiculo():
    marca = input("Marca del vehículo: ")
    modelo = input("Modelo del vehículo: ")
    año = int(input("Año del vehículo: "))
    color = input("Color del vehículo: ")
    motor = input("Motor del vehículo: ")
    transmision = input("Tipo de transmisión (Manual o Automática): ")
    combustible = input("Tipo de combustible (Gasolina, Diesel, Eléctrico, etc.): ")
    numero_puertas = int(input("Número de puertas: "))
    precio_compra = float(input("Precio de compra del vehículo: "))
    nacionalidad = input("Nacionalidad (Nacional o Importado): ")
    placa = input("Placa del vehículo: ")

    return Vehiculo(marca, modelo, año, color, motor, transmision, combustible, numero_puertas, precio_compra, nacionalidad, placa)

print("Registrar vehículo")
vehiculo1 = registrar_vehiculo()

print("---------------------------------------")
vehiculo1.mostrar_datos()