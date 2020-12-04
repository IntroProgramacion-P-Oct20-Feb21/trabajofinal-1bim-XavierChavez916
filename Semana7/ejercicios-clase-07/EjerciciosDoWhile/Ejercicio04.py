numero = 4
potencia = 3
resultado = 1
contador = 1
bandera = True

while(contador <= potencia):
    resultado = resultado * numero #1*4=4||4*4=16
    contador = contador + 1 #1+1=2||2+1+3||
    if(contador <= potencia):#2<=3||3<=3||
        bandera = False
print(f"{resultado}")        