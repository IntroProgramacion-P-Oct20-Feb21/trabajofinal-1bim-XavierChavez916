
tabla = int(input("Ingrese la tabla a generar"))

for contador in range(5,30+1,1):
    operacion = tabla * contador
    print(f"{tabla} x {contador} = {operacion}")