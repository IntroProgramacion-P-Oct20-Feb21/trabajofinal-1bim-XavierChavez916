suma_total = 0
bandera = True

while(bandera):
    calificaciones = float(input("Ingrese la calificacion\n> "))
    suma_total = suma_total + calificaciones

    salir = int(input("Ingrese -1 para salir del ciclo\n> "))
    if(salir == -1):
        bandera = False

print(f"Suma de calificaciones es: {suma_total:.2f}")

