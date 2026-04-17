class IntercaladorArreglos():
    def __init__(self, arreglo1, arreglo2):
        self.arreglo1 = arreglo1
        self.arreglo2 = arreglo2
    
    def intercalar(self):
        a1 = self.arreglo1
        a2 = self.arreglo2
        resultado = []
        
        i = 0  # índice para a1
        j = 0  # índice para a2
        
        # Mientras haya elementos en ambos arreglos
        while i < len(a1) and j < len(a2):
            if a1[i] <= a2[j]:
                resultado.append(a1[i])
                i += 1
            else:
                resultado.append(a2[j])
                j += 1
        
        # Agregar los elementos restantes de a1 (si quedaron)
        while i < len(a1):
            resultado.append(a1[i])
            i += 1
        
        # Agregar los elementos restantes de a2 (si quedaron)
        while j < len(a2):
            resultado.append(a2[j])
            j += 1
        
        return resultado
    
    def mostrar_resultado(self):
        resultado = self.intercalar()
        print(f"Arreglo 1: {self.arreglo1}")
        print(f"Arreglo 2: {self.arreglo2}")
        print(f"Intercalado: {resultado}")

# Prueba con el ejemplo
a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]

intercalador = IntercaladorArreglos(a1, a2)
intercalador.mostrar_resultado()
# Resultado esperado: [-10, -5, 0, 0, 0, 1, 5, 7]