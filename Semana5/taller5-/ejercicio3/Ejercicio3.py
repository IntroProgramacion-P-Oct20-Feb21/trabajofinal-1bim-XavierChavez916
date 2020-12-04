porcentaje1 = 20
porcentaje2 = 30
porcentaje3 = 15
porcentaje4 = 8
marca = input("Ingrese la marca del automovil\n> ")
origen = input("Ingrese el origen del automovil\n> ")
costo = float(input("Ingrese el costo del automovil\n> "))

if(origen == "Alemania"):
    impuestos = (porcentaje1 * costo)/100
    costo = costo + impuestos
else:
    if(origen == "Japon"):
        impuestos = (porcentaje2 * costo)/100
        costo = costo + impuestos
    else:
        if(origen == "Italia"):
            impuestos = (porcentaje3 *costo)/100
            costo = costo + impuestos
        else:
            if(origen == "USA"):
                impuestos = (porcentaje4 * costo)/100
                costo = costo + impuestos
            else:
                impuestos = 0
                costo = costo + impuestos

print(f"El impuesto por pagar es: {impuestos:.2f}\nEl precio de venta es:"
        f" {costo:.2f}")