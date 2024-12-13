import math

class FirstExercise:
    """Clase del primer ejercicio"""
    def __init__(self,number,chapter):
        self.number=number
        self.chapter=chapter
        
    def imprimir_numero(self):
        """Funcion que imprime un numero"""
        print(self.number)
prime= FirstExercise(6,"Objetos y clases")
print(prime.chapter)
prime.imprimir_numero()

class Circle:
    def __init__(self,radio):
        self.radio=radio
        pass
    def area(self):
        area=math.pi*(self.radio**2)
        return area
    def perimetro(self):
        perimetros=math.pi*(2*self.radio)
        return perimetros
    def modificarRadio(self,num):
        self.radio=num

redondo= Circle(5)
print(redondo.perimetro())

class Vehicle:
    def __init__(self,nombre,velocidadMax,kilometraje,owner="Nter"):
        self.nombre=nombre
        self.velocidadMax=velocidadMax
        self.kilometraje=kilometraje
        self.owner=owner
        pass
    def mostrarCapacidad(self,capacidad):
        print(f"La capacidad de {self.nombre} es {capacidad}")

class Bus(Vehicle):
    def mostrarCapacidad(self,capacidad=50):
        print(f"La capacidad de {self.nombre} es {capacidad}")
    pass 

coche= Vehicle("Mustang",125,4234324)
autobus= Bus("Utobus",100,234325,"Marcos Muñoz")
print(vars(coche))
print(vars(autobus))
autobus.mostrarCapacidad()

