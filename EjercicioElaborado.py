#permite registrar la información básica de un cliente en un salón de belleza,
#usa "EN ESPERA" para indicar que el cliente aún no ha recibido el servicio, y "SERVICIO COMPLETADO" cuando el servicio ha sido finalizado
class ClienteSalon:
    def __init__(self, nombre, edad, servicio, tiempo_servicio, nombre_estilista):
        self.nombre = nombre
        self.edad = edad
        self.servicio = servicio
        self.tiempo_servicio = tiempo_servicio
        self.nombre_estilista = nombre_estilista
        self.estado = "EN ESPERA"
    
    def registrar(self):
        self.estado = "SERVICIO COMPLETADO"
        self.mostrar_informacion()

    def mostrar_informacion(self):
        print(f"Nombre del Cliente: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Servicio Solicitado: {self.servicio}")
        print(f"Tiempo Estimado de Servicio: {self.tiempo_servicio} minutos")
        print(f"Estilista Asignado: {self.nombre_estilista}")
        print(f"Estado: {self.estado}")

nombre = input("Nombre del cliente: ")
edad = int(input("Edad: "))
servicio = input("Servicio solicitado: ")
tiempo_servicio = int(input("Tiempo estimado del servicio: "))
nombre_estilista = input("Nombre del estilista: ")

cliente = ClienteSalon(nombre, edad, servicio, tiempo_servicio, nombre_estilista)
cliente.registrar()
