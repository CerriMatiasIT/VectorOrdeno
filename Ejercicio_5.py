class Analizador_Matriz():
    def __init__(self, matriz, matriz2):
        self.matriz = matriz
        self.matriz2 = matriz2
    
    def suma_de_matrices(self):
        if not self.matriz or not self.matriz2:
            return None  # o podríamos lanzar una excepción
        
        filas = len(self.matriz)
        columnas = len(self.matriz[0])
        
        if len(self.matriz2) != filas or len(self.matriz2[0]) != columnas:
            return "Error: Las matrices deben tener las mismas dimensiones"
        
        matriz_resultado = []
        
        for i in range(filas):
            fila_resultado = []
            for j in range(columnas):
                suma = self.matriz[i][j] + self.matriz2[i][j]
                fila_resultado.append(suma)
            matriz_resultado.append(fila_resultado)
        
        return matriz_resultado
    
    def mostrar_matriz(self, matriz):
        for fila in matriz:
            print(fila)
        print()

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

analizador = Analizador_Matriz(matriz1, matriz2)
resultado = analizador.suma_de_matrices()

print("Matriz 1:")
analizador.mostrar_matriz(matriz1)

print("Matriz 2:")
analizador.mostrar_matriz(matriz2)

print("Suma:")
analizador.mostrar_matriz(resultado)