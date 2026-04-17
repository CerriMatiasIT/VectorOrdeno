class Numero():
    def __init__(self, numero):
        self.numero = numero
    
    def es_primo(self):
        n = self.numero
        if n <= 1:
            return False
        import math
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True
    def suma_de_multiplos(self):
        numero = self.numero
        suma=0
        if(numero <=0):
            return "El numero a ingresar debe ser mayor que 0"

        for i in range(numero):
            if(i%3==0 and i%5==0):
                suma+=i
            elif(i%3==0):
                suma+=i
            elif(i%5==0):
                suma+=i  
        return f"La suma es {suma}"

    
num = Numero(17)
num2 = Numero(10)
print(num.es_primo())
print(num2.es_primo())
print(num.suma_de_multiplos())
print(num2.suma_de_multiplos())