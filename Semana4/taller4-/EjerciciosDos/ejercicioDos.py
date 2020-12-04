
largo  = float(input("Ingrese el largo del terreno\n>"))
ancho = float(input("Ingrese el ancho del terreno\n>"))
costoMetro = float(input("Ingrese el costo del m2 del terreno\n>"))
nombreComprador = input("Ingrese el nombre del comprador\n>")

area = largo * ancho
costoTerreno = area * costoMetro

print("El costo del terreno es : %.2f y el comprador es: %s \n"%
    (costoTerreno,
    nombreComprador))

