'''
Generar un algoritmo que permita calcular y mostrar el valor de la planilla 
de teléfono de un casa. Se debe ingresar el costo por minutos, el número de 
minutos consumidos en el mes.
Algoritmo:
1. Inicio.
2. Se pide ingresar el costo por minutos.
3. Se pide ingresar el número de minutos consumidos por el mes.
4. Se calcula multiplicando el costo por el número de minutos.
5. Se presenta en pantalla el valor de la planilla de teléfono de una casa.
5. Fin
'''

costo_por_minuto = float(input("Ingrese el costo por minuto\n>"))
minutos_consumidos_mes = float(input("Ingrese el numero de minutos\
 consumidos por el mes\n>"))

valor_planilla = costo_por_minuto * minutos_consumidos_mes

print("El valor de la planilla de teléfono es: %.2f\n"%(valor_planilla))