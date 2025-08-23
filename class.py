class perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    # método para hacer que el perro ladre
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau Guau!"

    # método para obtener la información del perro
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años"


# programa principal
mi_perro = perro("Firulais", "Labrador", 3)

print(mi_perro.mostrar_informacion())
print(mi_perro.ladrar())
