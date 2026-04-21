import random
class Vector:
    def __init__(self):
        self.vector = []
    
    def orden_seleccion(self):
        for i in range(len(self.vector)):
            min_idx = i
            for j in range(i+1, len(self.vector)):
                if self.vector[j] < self.vector[min_idx]:
                    min_idx = j
            self.vector[i], self.vector[min_idx] = self.vector[min_idx], self.vector[i]

    def orden_insercion(self):
        n = len(self.vector)

        for i in range(1, n):
            x = self.vector[i]
            j = i - 1

            while j >= 0 and x < self.vector[j]:
                self.vector[j + 1] = self.vector[j]
                j = j - 1

            self.vector[j + 1] = x

    def orden_burbujeo(self):
        inicio = time.time()  
        n = len(self.vector)

    for i in range(n):
        intercambio = False
            
        for j in range(0, n - i - 1):
            if self.vector[j] > self.vector[j + 1]:
                self.vector[j], self.vector[j + 1] = self.vector[j + 1], self.vector[j]
                intercambio = True
            
        if not intercambio:
            break
        fin = time.time() 
    
    # Imprimir el tiempo de ejecución en milisegundos
    print(f" Se ordeno en : {(fin - inicio) * 1000:.8f} milisegundos, con Algoritmo Burbujeo")
   
        return self.vector
    
    
    # Métodos para generar vectores
    def generar_ordenado(self, n):
        self.vector = list(range(n))
    
    def generar_desordenado(self, n):
        self.vector = list(range(n, 0, -1))  # descendente
    
    def generar_random(self, n):
        self.vector = [random.randint(0, 100) for _ in range(n)]

vector = Vector()
vector.generar_random(100)
print(vector.vector)

vector.generar_random(100)
inicio = time.time()
vector.orden_insercion()
fin = time.time()
print(f" Se ordeno en : {(fin - inicio)*1000} milisegundos, con Algoritmo Seleccion")


v=Vector()

v.generar_ordenado(5000)
print(v.vector)
v.orden_burbujeo()

v.generar_desordenado(5000)
print(v.vector)
v.orden_burbujeo()

v.generar_random(5000)
print(v.vector)
v.orden_burbujeo()