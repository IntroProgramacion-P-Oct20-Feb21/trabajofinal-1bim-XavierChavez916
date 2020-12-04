
for i in range (1,10,1):
    print(f"Tabla de multiplicar del numero {i}")
    for contador in range (1,12+1,1):
        operacion = i * contador
        print(f"{i} x {contador} = {operacion}")
    print("\n")
