'''
Algoritmo:
1. Inicio.
2. Se pide ingresar el costo del CPU.
3. Se pide ingresar el costo del teclado.
4. Se pide ingresar el costo de la pantalla.
5. Se pide ingresar el costo del ratón.
6. Se suman todos los costos.
7. Se muestra en pantalla el costo de una computadora de escritorio.
8. Fin.
'''
costo_cpu = float(input("Ingrese el costo del CPU\n>"))
costo_teclado = float(input("Ingrese el costo del teclado\n>"))
costo_pantalla = float(input("Ingrese el costo de la pantalla\n>"))
costo_ratón = float(input("Ingrese el costo del ratón\n>"))

costo_computadora = costo_cpu + costo_teclado + costo_pantalla + costo_ratón

print("El costo de la computadora es: $%.2f \n"%(costo_computadora))