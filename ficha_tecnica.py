import time
import os

print(os.uname())

tInit = time.time()
for i in range(1,100000000):
    suma = 1+1
tFin = time.time()
diff = tFin - tInit
print(f"--------SUMA--------")
print(f"Se demoro {diff} en realizar la actividad")
print(f"--------------------------------")

tInit = time.time()
for i in range(1,100000000):
    resta = 1-1
tFin = time.time()
diff = tFin - tInit
print(f"--------resta--------")
print(f"Se demoro {diff} en realizar la actividad")
print(f"--------------------------------")

tInit = time.time()
for i in range(1,100000000):
    multiplicar = 1*1
tFin = time.time()
diff = tFin - tInit
print(f"--------Mult--------")
print(f"Se demoro {diff} en realizar la actividad")
print(f"--------------------------------")

tInit = time.time()
for i in range(1,100000000):
    division = 1/1
tFin = time.time()
diff = tFin - tInit
print(f"--------Division--------")
print(f"Se demoro {diff} en realizar la actividad")
print(f"--------------------------------")

tInit = time.time()
for i in range(1,100000000):
    comparacion = i > 1
tFin = time.time()
diff = tFin - tInit
print(f"--------Comparacion--------")
print(f"Se demoro {diff} en realizar la actividad")
print(f"--------------------------------")

tInit = time.time()
for i in range(1,100000000):
    asignacion = i
tFin = time.time()
diff = tFin - tInit
print(f"--------Asignacion--------")
print(f"Se demoro {diff} en realizar la actividad")
print(f"--------------------------------")