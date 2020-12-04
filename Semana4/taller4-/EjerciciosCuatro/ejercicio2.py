'''
Generar un algoritmo que permite ingresar los gastos de tres hijos de un 
 padre de familia; calcular y mostrar el total de gastos de los hijos del 
 padre de familia.
Algoritmo: 
1. Inicio
2. Se pide ingresar gasto del primer hijo.
3. Se pide ingresar gasto del segundo hijo.
4. Se pide ingresar gasto del tercer hijo.
5. Se Suman los gastos de los 3 hijos.
6. Se presenta en pantalla el total de los gastos de los 3 hijos
7. Fin
'''
gasto_primer_hijo = float(input("Ingrese el gasto del primer hijo\n>"))
gasto_segundo_hijo = float(input("Ingrese el gasto del segundo hijo\n>"))
gasto_tercer_hijo = float(input("Ingrese el gasto del tercer hijo\n>"))

total_gastos = gasto_primer_hijo + gasto_segundo_hijo + gasto_tercer_hijo

print("El costo total es: $%.2f\n" % (total_gastos))
