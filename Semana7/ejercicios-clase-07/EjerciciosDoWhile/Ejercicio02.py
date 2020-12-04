bandera = True
cadena_final = ""
suma = 0
contador = 0
while(bandera):  
    nota = float(input("Ingrese las calificaciones\n> "))

    cadena_final = (f"{cadena_final}{nota:.2f}\n")

    salida = input("Ingrese (s) si desea salir del ciclo\n> ")

    suma = suma + nota
    contador = contador + 1
    promedio = suma / contador
    if(salida == "s"):
        bandera = False

print(f"Listado de notas\n{cadena_final}Y el promedio es: {promedio:.2f}")    


