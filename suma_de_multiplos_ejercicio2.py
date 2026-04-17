def suma_de_multiplos(numero):
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

print(suma_de_multiplos(10))
print(suma_de_multiplos(16))
