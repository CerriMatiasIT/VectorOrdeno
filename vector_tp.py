import random
class Vector:
    def __init__(self):
        self.vector = []
    
    def orden_seleccion(self):
        pass

    def orden_insercion(self):
        pass

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
