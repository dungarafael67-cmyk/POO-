class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"

# Uso
p = Persona("dunga monsalvo", 17)
print(p.saludar())
