'''
Realizar un programa que permita presentar un mensaje de: 
acceso correcto, si el valor ingresado para la variable ciudad tiene el valor 
de Loja; caso contrario, presentar un mensaje de acceso incorrecto
'''
ciudad = input("Ingrese la ciudad\n> ")
if (ciudad == "Loja"):
    print(f"Acceso correcto")
else:
    print(f"Acceso incorrecto")
