'''
Generar un solución que permita calcular y mostrar el pago mensual de un 
préstamo de 1 año de plazo. Se debe ingresar el monto del préstamo y el interés
mensual a cobrar.
Algoritmo:
1. Inicio 
2. Se pide ingresar el monto del préstamo
3. Se pide ingresar el interés mensual a cobrar
4. Se divide el monto del préstamo para 12 meses y se suma el interés mensual
    a cobrar
5. Se muestra en pantalla el pago mensual de un préstamo.
6. Fin
'''
monto_prestamo = float(input("Ingrese el monto del prestamo\n>"))
interes_mensual_cobrar = float(input("ingrese el interes mensual a cobrar\n>"))

pago_mensual = monto_prestamo / 12 + interes_mensual_cobrar

print("El pago mensual del préstamo es: %.2f\n"%(pago_mensual))