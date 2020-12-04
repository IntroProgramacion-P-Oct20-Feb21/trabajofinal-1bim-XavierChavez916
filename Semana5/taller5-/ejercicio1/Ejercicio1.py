'''
Solución que permita calcular y mostrar el valor a cancelar de una planilla 
de luz. Se debe ingresar el valor de costo por kilovatio/hora y el número de 
kilovatios consumidos en el mes. Si el usuario tiene edad mayor a 65 años, 
se debe descontrar el 10%.
'''
porcentaje = 10
edad = int(input("Ingrese su edad\n>"))
valor_kilovatio_hora = float(input("Ingrese el costo de kilovatio/hora\n>"))
numero_kilovatios_mes = float(input("Ingresar el número de kilovatios\
 consumidospor el mes\n>"))
valor_total = valor_kilovatio_hora * numero_kilovatios_mes
if(edad>65):
    descuento = valor_total * porcentaje / 100
    valor_total = valor_total - descuento

print("El valor de cancelar de una planilla de luz es: %.2f\n"%(valor_total))

