contador = 1
tabla = int(input("Ingrese la tabla a generar\n> "))
bandera = True
while(contador<=10):
    operacion = tabla * contador
    print(f"{tabla} x {contador} = {operacion}")
    contador = contador + 1
    