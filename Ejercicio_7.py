import random

class Juego_Numero_Aleatorio():

    def __init__(self):
        self.numero = random.randint(0,1000)

    def adivinar_numero(self):
        numero_a_adivinar = self.numero
        print("JUEGO DE ADIVINANZA")
        print("Adivina el numero aleatorio del 0 al 1000")
        entrada_usuario = 0
        intentos = 0

        while entrada_usuario!= '*' or entrada_usuario != numero_a_adivinar:
            entrada_usuario = input("Ingresa un numero entre el 0 al 1000 '*' para finalizar: ")
            if entrada_usuario == "*":
                print("Fin del juego")
                print(f"Este era el numero: {numero_a_adivinar}")
                break
            entrada_usuario = int(entrada_usuario)
            intentos +=1
            if entrada_usuario < numero_a_adivinar:
                print("El numero es mas grande.")
            elif entrada_usuario > numero_a_adivinar:
                print("El numero es mas chico.")
            else:
                print("Felicidades!!!")
                print(f"Cantidad de intentos {intentos}")
                break
            

player1 = Juego_Numero_Aleatorio()
player1.adivinar_numero()
