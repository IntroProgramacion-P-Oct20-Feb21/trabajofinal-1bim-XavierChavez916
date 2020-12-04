
numerador = 1
denominador = 1
contador = 1

while(contador <= 5):
    if(contador%2==0):
        print(f"-{numerador}/{denominador}",end="") 
    else:
        print(f"+{numerador}/{denominador}",end="")  

    contador = contador + 1 
    denominador = denominador + 2 

print()    