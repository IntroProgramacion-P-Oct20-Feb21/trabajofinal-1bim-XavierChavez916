'''
Se debe generar un algoritmo que permite calcular y mostrar el valor total a 
pagar mensual de servicios digitales de una persona. Los servicios digitales 
son: netflix, youtube premium, dropbox, spotify. Si la persona es menor a 30 
años se descuenta el 20% del total mensual.
1. Inicio
2. Se pide ingresar el valor de netflix a pagar mensualmente
3. Se pide ingresar el valor de youtube premiun a pagar mensualmente
4. Se pide ingresar el valor de dropbox a pagar mensualmente
5. Se pide ingresar el valor de spotify a pagar mensualmente
6. Se suma los servicios digitales
7. Si la persona es menor a 30 años se descuenta el 20% del total mensual
8. Se muestra en pantalla el valor total a pagar mensual de servicios 
   digitales de una persona
9. Fin
'''
porcentaje = 20
edad = int(input("Ingresar la edad de la persona\n>"))
valor_netflix=float(input("Ingresar el valor de netflix a"
                            " pagar mensualmente\n>"))
valor_youtube=float(input("Ingresar el valor de youtube premiun a"
                            " pagar mensualmente\n>"))
valor_dropbox=float(input("Ingresar el valor de dropbox a"
                            " pagar mensualmente\n>"))
valor_spotify=float(input("Ingresar el valor de spotify a"
                            " pagar mensualmente\n>"))

valor_total = valor_netflix + valor_youtube + valor_dropbox + valor_spotify

if(edad < 30):
    descuento = valor_total * porcentaje / 100
    valor_total = valor_total - descuento

print(f"El valor total a pagar mensual de servicios digitales de una persona"
        f" es: {valor_total:.2f}")




