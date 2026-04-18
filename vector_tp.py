import random
class Vector:
    def __init__(self):
        self.vector = []
    
    def orden_seleccion(self):
        pass

    def orden_insercion(self):
        pass

    def orden_burbujeo(self):
        pass
    
    # Métodos para generar vectores
    def generar_ordenado(self, n):
        self.vector = list(range(n))
    
    def generar_desordenado(self, n):
        self.vector = list(range(n, 0, -1))  # descendente
    
    def generar_random(self, n):
        self.vector = [random.randint(0, 100) for _ in range(n)]