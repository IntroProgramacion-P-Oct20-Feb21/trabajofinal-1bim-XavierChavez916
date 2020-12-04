cadena_final = ""
bandera = True

while(bandera):
    nota = float(input("Ingrese las calificaciones\n> "))

    cadena_final = (f"{cadena_final}{nota:.2f}\n")

    salida = int(input("Ingrese (-111) si desea salir del ciclo\n> "))

    if(salida == -111):
        bandera = False

print(f"Listado de notas\n{cadena_final}")
