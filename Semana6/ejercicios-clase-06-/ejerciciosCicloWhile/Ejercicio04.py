limite = 5
contador = 1
suma_total = 0

print("Ingrese las notas de los estudiantes de su materia ")

while(contador <= limite):
    calificacion = float(input(f"Ingrese la calificacion {contador}\n> "))
    suma_total  = suma_total + calificacion
    contador = contador + 1 

promedio = suma_total / limite
print(f"El promedio final es: {promedio:.2f}")
