import random
import time

class Vector:
    def __init__(self):
        self.vector = []
    
    def orden_seleccion(self):
        n = len(self.vector)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.vector[j] < self.vector[min_idx]:
                    min_idx = j
            self.vector[i], self.vector[min_idx] = self.vector[min_idx], self.vector[i]
        return self.vector

    def orden_insercion(self):
        n = len(self.vector)
        for i in range(1, n):
            x = self.vector[i]
            j = i - 1
            while j >= 0 and x < self.vector[j]:
                self.vector[j + 1] = self.vector[j]
                j -= 1
            self.vector[j + 1] = x

    def orden_burbujeo(self):
        n = len(self.vector)
        for i in range(n):
            intercambio = False
            for j in range(0, n - i - 1):
                if self.vector[j] > self.vector[j + 1]:
                    self.vector[j], self.vector[j + 1] = self.vector[j + 1], self.vector[j]
                    intercambio = True
            if not intercambio:
                break
        return self.vector

    def generar_ordenado(self, n):
        self.vector = list(range(n))
    
    def generar_desordenado(self, n):
        self.vector = list(range(n, 0, -1))
    
    def generar_random(self, n):
        self.vector = [random.randint(0, 100) for _ in range(n)]

# ================== PRUEBAS ==================
# ===== VERIFICACIÓN DE QUE ORDENA CORRECTAMENTE =====
print("\n=== COMPROBANDO QUE LOS ALGORITMOS ORDENAN BIEN ===")

v_test = Vector()
v_test.generar_random(5)
print("Vector original:", v_test.vector)
v_test.orden_seleccion()
print("Selección:    ", v_test.vector)

v_test = Vector()
v_test.generar_random(5)
print("Vector original:", v_test.vector)
v_test.orden_insercion()
print("Inserción:    ", v_test.vector)

v_test = Vector()
v_test.generar_random(5)
print("Vector original:", v_test.vector)
v_test.orden_burbujeo()
print("Burbujeo:     ", v_test.vector)

# ===== STRESS TESTS =====
N = 5000

def medir_tiempo(metodo, nombre):
    inicio = time.time()
    metodo()
    fin = time.time()
    print(f"{nombre} tardó {(fin - inicio) * 1000:.5f} ms")

# --- Caso 1: Vector ordenado ---
print(f"\n--- Vector ORDENADO (N={N}) ---")
v = Vector()
v.generar_ordenado(N)
medir_tiempo(v.orden_seleccion, "Selección")

v = Vector()
v.generar_ordenado(N)
medir_tiempo(v.orden_insercion, "Inserción")

v = Vector()
v.generar_ordenado(N)
medir_tiempo(v.orden_burbujeo, "Burbujeo")

# --- Caso 2: Vector desordenado (invertido) ---
print(f"\n--- Vector DESORDENADO (N={N}) ---")
v = Vector()
v.generar_desordenado(N)
medir_tiempo(v.orden_seleccion, "Selección")

v = Vector()
v.generar_desordenado(N)
medir_tiempo(v.orden_insercion, "Inserción")

v = Vector()
v.generar_desordenado(N)
medir_tiempo(v.orden_burbujeo, "Burbujeo")

# --- Caso 3: Vector random ---
print(f"\n--- Vector RANDOM (N={N}) ---")
v = Vector()
v.generar_random(N)
medir_tiempo(v.orden_seleccion, "Selección")

v = Vector()
v.generar_random(N)
medir_tiempo(v.orden_insercion, "Inserción")

v = Vector()
v.generar_random(N)
medir_tiempo(v.orden_burbujeo, "Burbujeo")




