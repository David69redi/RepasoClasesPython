class Persona:
    def __init__(self, nombre, salud, arma):
        self.nombre = nombre
        self.salud = salud
        self.arma = arma

    def disparar_a(self, objetivo):
        if self.arma.municion > 0:
            self.arma.disparar()
            objetivo.recibir_bala(self.arma.danio)
        else:
            print(f"{self.nombre} no puede disparar, no tiene munición.")

    def recibir_bala(self, danio):
        self.salud -= danio
        
        if self.salud > 0:
            print(f"{self.nombre} ha recibido {danio} de daño. Salud restante: {self.salud}")

class Arma:
    def __init__(self, nombre, municion, danio):
        self.nombre = nombre
        self.municion = municion
        self.danio = danio

    def disparar(self):
        if self.municion != 0:
            print(f"Munición restante: {self.municion}")
            self.municion -= 1
        else:
            print(f"{self.nombre} no tiene munición")

arma1 = Arma("Olympia", 14, 70)
arma2 = Arma("RayGun", 75, 50)
arma3 = Arma("MP5", 225, 30)
arma4 = Arma("AK47", 405, 70)
arma5 = Arma("Deagle", 10, 20)


persona1 = Persona("David", 100, arma1)
persona2 = Persona("Pepe", 100, arma2)

persona1.disparar_a(persona2)
