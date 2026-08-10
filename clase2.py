class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
            return f"hola, soy {self.nombre}"

p = Persona("Dunga", 17)
print(p.saludar())

class Galleta:
    def __init__(self,sabor):
        self.sabor = sabor
        
        g1 = Galleta ("vainilla")
        g2 = Galleta ("chocolate")
        print (g1.sabor)
        print (g2.sabor)
