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

    def seleccion(self):
        # Ordenamiento por selección
        for i in range(len(self.datos)):
            min_idx = i
            for j in range(i+1, len(self.datos)):
                if self.datos[j] < self.datos[min_idx]:
                    min_idx = j
            self.datos[i], self.datos[min_idx] = self.datos[min_idx], self.datos[i]

    def insercion(self):
        # Ordenamiento por inserción
        for i in range(1, len(self.datos)):
            key = self.datos[i]
            j = i - 1
            while j >= 0 and self.datos[j] > key:
                self.datos[j+1] = self.datos[j]
                j -= 1
            self.datos[j+1] = key

    def burbujeo(self):
        # Ordenamiento burbujeo
        n = len(self.datos)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.datos[j] > self.datos[j+1]:
                    self.datos[j], self.datos[j+1] = self.datos[j+1], self.datos[j]
```

---

### 🧪 Casos de Prueba

- **Vector ordenado:** `[1, 2, 3, 4, 5]`  
- **Vector desordenado:** `[5, 4, 3, 2, 1]`  
- **Vector aleatorio:** `[3, 1, 4, 5, 2]`  

Cada caso se prueba con los tres métodos de ordenamiento y se mide el tiempo de ejecución.

---

### 📊 Resultados Experimentales

Se midió el tiempo de ejecución para distintos tamaños de `N` (ejemplo: 100, 500, 1000, 5000).  
Los resultados se graficaron en función de **T = f(N)**.

Ejemplo de gráfico esperado:

```
Gráfico: Tiempo vs Tamaño del vector
- Selección: curva cuadrática
- Inserción: curva cuadrática
- Burbujeo: curva cuadrática
```

*(Aquí se pueden adjuntar imágenes de los gráficos generados con Excel, matplotlib o similar.)*

---

### 📈 Conclusiones

- Los tres algoritmos presentan complejidad **O(n²)** en el peor caso.  
- El ordenamiento por inserción puede ser más eficiente en vectores casi ordenados.  
- El burbujeo es el menos eficiente en la mayoría de los casos.  
- Los resultados experimentales confirman la teoría de complejidad.  

---

👉 Este README.md sirve como **documentación base** para el repositorio. Cada compañero puede agregar sus resultados de pruebas y gráficos en una carpeta `results/` o `docs/`.

---

¿Querés que te arme también un **template de README.md con secciones vacías** (tipo guía) para que cada integrante del grupo solo complete su parte sin modificar la estructura?