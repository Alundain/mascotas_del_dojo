class Ninja:
# implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premio = premio
        self.mascota = mascota
        self.comida_mascota = comida_mascota
        
    # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        self.mascota.jugar()
        return self

# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self, food):
        if len(self.comida_mascota) > 0:
            comida_mascota =self.comida_mascota.pop()
            print(f"Alimenta {self.name} {food}!")
            self.mascota.comer()
        else:
            print('alimenta a tu mascota')
        return self

# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar(self):
        self.mascota.sonido()
        return self

