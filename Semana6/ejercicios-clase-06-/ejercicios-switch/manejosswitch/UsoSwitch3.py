'''
Generar un programa que permita ingresar un nombre de una ciudad;
Los nombres de las ciudades permitidas son las que empiezan con vocal.
Si la ciudad es permitida presentar un mensaje:
Nombre con inicial O de otavalo
Si la ciudad no es permitida presentar un mensaje:
opción incorrecta; ninguna de las anteriores
'''

nombre = input("Ingrese el nombre de una ciudad del Ecuador\n> ")

ini = nombre [0]

if(ini == 'a' or ini == 'A'):
    print(f"Nombre con inicial {ini} de {nombre.lower()}")
else:
    if(ini == 'e' or ini == 'E'):
        print(f"Nombre con inicial {ini} de {nombre.lower()}")
    else:
        if(ini == 'i' or ini == 'I'):   
            print(f"Nombre con inicial {ini} de {nombre.lower()}")
        else:
            if(ini == 'o' or ini == 'O'): 
                print(f"Nombre con inicial {ini} de {nombre.lower()}")
            else:
                if(ini == 'u' or ini == 'U'): 
                    print(f"Nombre con inicial {ini} de {nombre.lower()}")
                else:
                    print("Opción incorrecta; ninguna de las anteriores")    


            
        
        

  


