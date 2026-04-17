import math
import time
    
def gauss(n):
    if n==1:
        return 1
    else:
        return n+gauss(n-1)
    
def conGauss(n):
    if n<3:
        return -1

    for i in range(2, n+1):
        sumaIzq=gauss(i-1)
        sumaDer=gauss(n)-gauss(i)
        if sumaDer==sumaIzq:
            return i
        return -1
        
def metodo1(n):
    if n<3:
        return -1
    for i in range(2, n+1):
        sumaIzq=0
        for j in range(1, i):
            sumaIzq+=j
        sumaDer=0;
        for k in range(i+1, n+1):
            sumaDer+=k



        if sumaDer==sumaIzq:
            return i
    return -1

def metodo2(n):
    if n<3:
        return -1

    for i in range(1, n+1):
        sumaIzq=i*(i-1)/2
        sumaDer=(n*(n+1)-i*(i+1))/2
        if sumaDer==sumaIzq:
           return i

    return -1

    
def metodo3(n):
    if n<3:
        return -1
    i= math.sqrt((math.pow(n, 2)+n)/2)
    entera=int(i)

    if (i-entera) == 0:
        return int(i)

    return -1

 # main  

        
#        6         8
#        35        49
#       204       288
#      1189      1681
#      6930      9800
#     40391     57121
#    235416    332928
#   1372105   1940449
#   7997214  11309768
#  46611179  65918161
        
#n=288
#n= 9800
n= 9800
#n= 1940449

tIni = time.time()
print(metodo3(n))
tFin = time.time()
diff = tFin-tIni
print("Tiempo de ejecución del metodo 3  " + str(diff))
print("-----------------------------------------")

tIni = time.time()
print(metodo2(n))
tFin = time.time()
diff = tFin-tIni
print("Tiempo de ejecución del metodo2  "+ str(diff))
print("-----------------------------------------")

tIni = time.time()
print(metodo1(n))
tFin = time.time()
diff = tFin-tIni
print("Tiempo de ejecución del metodo 1  "+ str(diff))
print("-----------------------------------------")

#tIni = time.time()
#print(conGauss(n))
#tFin = time.time()
#diff = tFin-tIni
#print("Tiempo de ejecución con Gauss  " + str(diff))
#print("-----------------------------------------")
