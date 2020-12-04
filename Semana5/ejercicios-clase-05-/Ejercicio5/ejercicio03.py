porcentaje1 = 10
porcentaje2 = 15
porcentaje3 = 20

numeroDias = int(input("Ingrese el numero de días que se hospedará\n> "))
precioHabitacion = float(input("Ingrese el valor diario de la habitación\n> "))

if (numeroDias > 5 and numeroDias <= 10):
    subtotal = numeroDias * precioHabitacion
    descuento = (porcentaje1 * subtotal)/100
    valorTotal = subtotal - descuento
else:
    if (numeroDias > 10 and numeroDias <= 15):
        subtotal = numeroDias * precioHabitacion
        descuento = (porcentaje2 * subtotal)/100
        valorTotal = subtotal - descuento
    else:
        if(numeroDias > 15):
            subtotal = numeroDias * precioHabitacion
            descuento = (porcentaje3 * subtotal)/100
            valorTotal = subtotal - descuento
        else:
            subtotal = numeroDias * precioHabitacion
            descuento = 0
            valorTotal = subtotal - descuento

print(f"El valor subtotal es: {subtotal:.2f}\nEl descuento es: {descuento:.2f}\n"
        f"El valor total a pagar es: {valorTotal:.2f}")
