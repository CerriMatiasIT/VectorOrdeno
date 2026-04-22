# 📘 TP1 – 2da Parte  
## Métodos de Ordenamiento

### 📌 Objetivo
Implementar una clase `Vector` que contenga:  
- Un atributo principal: un arreglo de enteros.  
- Tres métodos de ordenamiento:  
  - Selección  
  - Inserción  
  - Burbujeo  

Además:  
- Generar casos de prueba con vectores en distintos estados:  
  - Ordenado  
  - Completamente desordenado  
  - Aleatorio  
- Realizar pruebas experimentales y graficar la relación **T = f(N)** para verificar la complejidad de los algoritmos.

---

### 🛠️ Implementación

```python
class Vector:
    def __init__(self, datos):
        self.datos = datos

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
```

---

### 🧪 Casos de Prueba

- **Vector ordenado:** `[1, 2, 3, 4, 5]`  
- **Vector desordenado:** `[5, 4, 3, 2, 1]`  
- **Vector aleatorio:** `[3, 1, 4, 5, 2]`  

Cada caso se prueba con los tres métodos de ordenamiento y se mide el tiempo de ejecución.

---

## 📊 Resultados Experimentales

![Gráfico 1 – Relación T=f(N)](./grafico1.png)

*Gráfico 1. Relación entre el tamaño del vector (N) y el tiempo de ejecución (T) para los algoritmos de selección, inserción y burbujeo. Se observa un crecimiento cuadrático, confirmando la complejidad teórica O(N²).*

---

### 📈 Conclusiones

- Los tres algoritmos presentan complejidad **O(n²)** en el peor caso.  
- El ordenamiento por inserción puede ser más eficiente en vectores casi ordenados.  
- El burbujeo es el menos eficiente en la mayoría de los casos.  
- Los resultados experimentales confirman la teoría de complejidad.  

---
