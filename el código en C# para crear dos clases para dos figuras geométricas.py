import math

# Clase para el círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Clase para el cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Clase principal para probar las figuras
if __name__ == "__main__":
    # Crear un círculo y un cuadrado
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)

    # Mostrar resultados
    print(f"Círculo: Área = {circulo.calcular_area():.2f}, Perímetro = {circulo.calcular_perimetro():.2f}")
    print(f"Cuadrado: Área = {cuadrado.calcular_area()}, Perímetro = {cuadrado.calcular_perimetro()}")
