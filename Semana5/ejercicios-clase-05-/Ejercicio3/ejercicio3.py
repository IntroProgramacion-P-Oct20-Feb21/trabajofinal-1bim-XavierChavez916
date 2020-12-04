'''
Realizar un programa que permita determinar si un estudiante ha pasado 
el ciclo se ingresa el promedio del estudiante
- Un estudiante pasa el ciclo si tiene un promedio mayor o igual a 7.5 
- Si el estudiante aprueba el ciclo, presentar un mensaje como el siguiente, 
Estudiante aprobado con un promedio: ?
- Si el estudiante tiene una nota mayor o igual a 5 y menor o igual a 7.4 
presentar un mensaje con el siguiente texto; Estudiante en suspenso con un promedio: 
- Si el estudiante tiene una nota menor a 5 presentar un mensaje con el 
siguiente texto; Estudiante reprobado con un promedio: ? 
'''
promedio = float(input("Ingrese el promedio del estudiante\n> "))

if (promedio >= 7.5):
    print(f"Estudiante aprobado con un promedio: {promedio:.2f}")
else:
    if (promedio >= 5) and (promedio <= 7.4):
        print(f"Estudiante en suspenso con un promedio: {promedio:.2f}")
    else:
        print(f"Estudiante reprobado con un promedio: {promedio:.2f}")    
    