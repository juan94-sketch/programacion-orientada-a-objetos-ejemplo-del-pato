from abc import ABC, abstractclassmethod

#1. Clase Abstracta (define la interfaz)
class SonidoAnimal(ABC): # Hereda de ABC

    @abstractclassmethod # Metodo que las clases hijas deben implementar
    def hacer_sonido(self):
        pass

#2. Clases Concretas (implementan la interfaz)
class Perro(SonidoAnimal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(SonidoAnimal):
    def hacer_sonido(self):
        return "Miau!"

# 3. Usando la abstraccion
# No se puede instanciar SonidoAnimal directamente:
#animal_sonido = SonidoAnimal() # Esto daria TypeError

mi_perro = Perro()
mi_gato = Gato()

animales = [mi_perro, mi_gato ]

# Mos abstraeremos de que tipo de animal es cada uno,
# solo sabemos que pueden "hacer_sonido".
for animal in animales:
    print(f"El amnimal dice: {animal.hacer_sonido()} ")

    class Pato:
        def hablar(self):
            return " Cuac!"

        def moverse(self):
            return "caminando como un pato"

    class Persona:
        def hablar(self):
            return "caminando erguido"

    class Perro:
        def hablar(self): # Los perros ladran, no "hablan" en el sentido humano, pero para el ejemplo ...
            return "¡Guau!"

        def moverse(self):
            return "corriendo en cuatro patas"

    def realizar_acciones(objeto_que_se_mueve_y_habla):
        """
        Esta funcion no se preocupa por el tipo de objeto,
        solo espera que tenga los metodos hablar() y moverse().
        """
        print(f"Sonido: {objeto_que_se_mueve_y_habla.hablar()}")
        print(f"Movimiento: {objeto_que_se_mueve_y_habla.moverse()}")
        print("-" * 20)

    #Creamos objetos de diferentes clases 
    pato_lucas = Pato()
    juan = Persona()
    firulais = Perro()

    # Usamos la funcion con diferentes tiposde objetos
    print("Demostracion de Duck Typing:")
    realizar_acciones(pato_lucas)
 
    
