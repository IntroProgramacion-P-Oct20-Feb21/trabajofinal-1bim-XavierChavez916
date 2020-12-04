limite_tabla = 12
contador = 1

tabla = int(input("Ingrese el número de tabla a generar\n> "))
cadena = ""
print(f"Tabla de multiplicar{cadena}")

while(contador <= limite_tabla):
    operacion = tabla * contador 
    print(f"{cadena}{tabla}*{contador}={operacion}")
    contador = contador + 1

print(f"{cadena}")
