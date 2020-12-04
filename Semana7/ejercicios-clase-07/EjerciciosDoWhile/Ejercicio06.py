contador = 1
cadena_final = ""
while(contador <= 5):
    cadena_final = (f"{cadena_final}Tabla de multiplicar del número {contador}\n")

    for i in range(1, 11):
        operacion = i * contador
        cadena_final = (f"{cadena_final}{contador} x {i} = {operacion}\n")
    cadena_final = (f"{cadena_final}\n") 
    contador = contador + 1

print(f"{cadena_final}")
