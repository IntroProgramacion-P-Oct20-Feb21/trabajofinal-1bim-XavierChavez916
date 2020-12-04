bandera = True
cadena_reporte = ""
sumaEdades = 0
sumaEstaturas = 0
contador = 0
cadena_edad = ""
cadena_reporte = (f"{cadena_reporte}Lista de jugadores\n")

while(bandera):
    nombreJugador = input("Ingrese el nombre del Jugador: \n> ")
    posicionCampo = input("Ingrese la posicion del campo\n> ")
    edad = int(input("Ingresa la edad del jugador\n> "))
    estatura = float(input("Ingrese la estatura del jugador\n> "))

    sumaEdades = sumaEdades + edad
    sumaEstaturas = sumaEstaturas + estatura
    contador = contador + 1

   

    
    cadena_reporte = (f"{cadena_reporte}{contador}.) {nombreJugador} -"
                        f"{posicionCampo}- edad {edad}, estatura {estatura:.2f}\n")

    salir = input("Desea salir del ciclo digite (si)\n> ")
    if(salir == "si"):
        bandera = False


promedioEdad = sumaEdades / contador
promedioEstaturas = sumaEstaturas / contador

cadena_reporte = (f"{cadena_reporte}Promedio de edades: {promedioEdad}\n")
cadena_reporte = (f"{cadena_reporte}Promedio de estaturas: {promedioEstaturas}\n")

print(f"{cadena_reporte}")

