class arreglo_de_enteros():
    def __init__(self,arreglo):
        self.arreglo = arreglo
    
    def esta_ordenado(self):
        arreglo = self.arreglo 
        print(f"Arreglo a revisar: {arreglo}")
        arreglo_ordenado = self.arreglo
        arreglo_ordenado.sort()
        print(f"Resultado esperado: {arreglo_ordenado}")
        numero = 0
        for numero in arreglo:
            if (numero == arreglo_ordenado[numero]):
                continue
            else:
                print("La lista no esta ordenada.")
                break

    def suma_de_arreglos_posiciones_pares(self):
        arreglo = self.arreglo
        acumulador = 0
        for i in range(0, len(arreglo)):
            if(i%2==0):
                acumulador+=arreglo[i]
        print(f"Resultado de la suma:{acumulador}")

objeto = arreglo_de_enteros([1,2,3,4,5])
objeto.esta_ordenado()
objeto.suma_de_arreglos_posiciones_pares()
objeto2 = arreglo_de_enteros([1,2,3,6,4])
objeto2.esta_ordenado()
objeto2.suma_de_arreglos_posiciones_pares()
objeto3 = arreglo_de_enteros([1,2,13,4,8,6])
objeto3.suma_de_arreglos_posiciones_pares()