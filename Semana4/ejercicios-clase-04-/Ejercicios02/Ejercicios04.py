# El input sirve para pedir datos cadena 
nombres = input("Ingrese el nombre del estudiante\n>") 
apellidos = input("Ingrese el apellido del estudiante\n>")
ciudad = input("Ingrese la ciudad donde vive porfavor\n>")
país = input("Ingrese el país donde vive por favor\n>")
nacimiento = input("Ingrese el año de nacimiento del estudiante\n>")

print("Datos del usuario:\n%s\n%s\n%s\n%s\n%s\n" % (nombres,
    apellidos,
    ciudad,
    país,
    nacimiento))