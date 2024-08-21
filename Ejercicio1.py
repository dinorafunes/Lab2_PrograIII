class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, enfermedades_anteriores, sexo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.nombre_dueño = dueño
        self.enfermedades_anteriores = enfermedades_anteriores
        self.sexo = sexo
        self.estado = "NO ATENDIDO"
        self.tamano = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def registrar(self):
        self.estado = "ATENDIDO"
        self.mostrar_informacion()

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Dirección del Dueño: {self.enfermedades_anteriores}")
        print(f"Teléfono del Dueño: {self.sexo}")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamano}")

nombre = input("Nombre del perro: ")
raza = input("Raza: ")
edad = int(input("Edad: "))
peso = float(input("Peso (en kg): "))
color = input("Color: ")
dueño = input("Nombre del dueño: ")
enfermedades_anteriores = input("Enfermedades anteriores: ")
sexo = input("Sexo de la mascota: ")
print("________________________________")
perro = Perro (nombre, raza, edad, peso, color, dueño, enfermedades_anteriores, sexo)
perro.registrar()