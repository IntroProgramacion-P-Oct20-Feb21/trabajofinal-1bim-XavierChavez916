
contador = 0
cadena_final = ""
numerador1 = 1
numerador2 = -1
resultado = 0

for i in range(1,15+1,2):
    valor = 1/i
    contador = contador + 1
    if(contador % 2 == 0):
        valor = valor * -1
        cadena_final = (f"{cadena_final}{numerador2}/{i}\n")
    else:
        valor = valor * 1
        cadena_final = (f"{cadena_final}{numerador1}/{i}\n")
    resultado = resultado + valor

print(f"{cadena_final}El resultado es: {resultado:.3f}")        