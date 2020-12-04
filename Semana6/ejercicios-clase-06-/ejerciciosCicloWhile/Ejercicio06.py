suma_total = 0
bandera = True
contador = 0

print("Ingrese las notas de los estudiantes de su materia")
while(bandera):
    calificaciones = float(input("Ingrese la calificación\n> "))
    suma_total = suma_total + calificaciones
    contador = contador + 1
    
    salir = int(input("Ingrese el valor de -1 para salir del ciclo\n> "))
    if(salir == -1):
        bandera = False
promedio = suma_total / contador
print(f"El promedio final es: {promedio:.2f}")    
