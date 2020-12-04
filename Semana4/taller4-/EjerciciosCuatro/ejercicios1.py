'''
Generar un algoritmo que permite calcular y presentar el área de un triángulo.
Los datos deben ser pedidos al usuario.
Algoritmo:
1. Inicio
2. Se pide ingresar la base
3. Se pide ingresar la altura
4. Se calcula el area del triangulo multiplicando su base por la altura
5. Se realiza la división para 2 
6. Se presenta en pantalla el resultado del área del triangulo.
7. Fin
'''
base = float(input("Ingrese la base del triangulo\n>"))
altura = float(input("Ingrese la altura del triangulo\n>"))

area_triangulo = base * altura / 2

print("El area del trinagulo es: %.2f\n" %(area_triangulo))


