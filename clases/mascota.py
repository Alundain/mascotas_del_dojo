class Mascota:
    # implementa __init__( name , tipo , golosinas ):
    def __init__ (self, name, tipo, golosinas, salud, energia, sonido):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
        self.sonido = sonido

# dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia += 25
        return self

    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    # jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud += 10
        self.energia -= 15
        return self

    # ruido() - imprime el sonido que produce la mascota
    def sonido(self):
        print(self.sonido)
        return self 