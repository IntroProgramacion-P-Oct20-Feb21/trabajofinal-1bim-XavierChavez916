limite_inferior = 10
limite_superior = 20
contador = 10
suma = 0

while(contador >= limite_inferior and contador <= limite_superior):
    suma = suma + contador 
    print(f"Contador {contador}")
    contador = contador + 2
print(f"La suma final es: {suma}")
