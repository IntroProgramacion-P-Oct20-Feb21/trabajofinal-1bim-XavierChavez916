'''
Realizar una miniespecificación que permita seleccionar el tipo de
operación aritemética (+,-,*) a realizar para dos valores ingresados por teclado
Realizar la operación y presentar el resultado en pantalla
'''

resultado = 0
valor1 = int(input("Ingrese el primer valor de la operación\n> "))
valor2 = int(input("Ingrese el segundo valor de la operación\n> "))
op = int(input("Seleccione la operación que desea realizar\n\
Ingrese 1 para suma\nIngrese 2 para restar\nIngrese 3 para multiplicar\n> ")) 

if(op == 1):
    resultado = valor1 + valor2
    tipo = "suma"
else:
    if(op == 2):
        resultado = valor1 - valor2
        tipo = "resta"
    else:
        if(op == 3):
            resultado = valor1 * valor2 
            tipo = "multiplicación"
        else:
            print("Operacion incorrecta")

print(f"El resultado de la operación {tipo} es: {resultado}")