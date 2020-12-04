suma_total = 0
contador = 0
bandera = True

print("Ingrese las notas de los estudiantes de su materia")

while(bandera):
    calificaciones = float(input("Ingrese la calificación\n> "))
    suma_total = suma_total + calificaciones
    contador = contador + 1
    
    salir = input("Ingrese 'si' para salir del ciclo\n> ")
    if(salir == "si"):
        bandera = False

promedio = suma_total / contador
print(f"El promedio final es: {promedio:.2f}")