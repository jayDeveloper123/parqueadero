from datetime import datetime
"""
lugar_1 = "odcupado"
lugar_2 = "odcupado"
lugar_3 = "odcupado"
lugar_4 = "odcupado"
lugar_5 = "odcupado"
lugar_6 = "odcupado"
lugar_7 = "odcupado"

if lugar_1 == "cupado":
    ...
if lugar_1 == "Disponible":
    ...
"""

menu = """
    1) elegir lugar/Parquear bicicleta
    2) Sacar Bicicleta 
    :
"""
parqueadero = ["Disponible", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible", "Ocupado"]
cupon_1 = "descuento1"
cupon_2 = "descuento2"
cupon_3 = "descuento3"
print("::::::::::::::::::Lugares Disponibles:::::::::::::::::::")
for i in range(len(parqueadero)):
    print("Lugar ", i + 1 , ": ", parqueadero[i])

opcion = int(input(menu))
#while opcion ==1 or opcion == 2
if opcion == 1:
    lugar = int(input("Elige un lugar: "))
    if lugar >= 9:
        print("Opcion invalida elige un lugar de 1 al 8")
    if parqueadero[lugar-1] == "Disponible":
        parqueadero[lugar-1] = "Ocupado"
        hora_entrada = datetime.now()
        print("Su lugar elejido es: ", lugar, "Su hr de entrada es: ", hora_entrada)
        for i in range(len(parqueadero)):
            print("Lugar ", i + 1, ": ", parqueadero[i])
        if parqueadero[lugar-1] == "Ocupado":
            print("Lugar ocupado")
    opcion = int(input(menu))
    if opcion == 2:
        lugar_aux = int(input("Ingrese su lugar: "))
        if parqueadero[lugar_aux-1] == "Ocupado":
            print("que pasa")
            descuento = input("Si tiene descuento ingrese la cadena de su cupon de descuento / si no lo tienen presione enter:")
            if descuento == cupon_1:
                hora_salida = datetime.now()
                tiempo_total = hora_salida - hora_entrada
                tiempo_total_seg = tiempo_total.total_seconds()
                precio_total = tiempo_total_seg * 1
                precio_total = precio_total - 1
                print("------------------------------------------------")
                print("Hr de entrada: ", hora_entrada , "Hr de salida: ", hora_salida)
                print("Su tiempo fue de: ", tiempo_total_seg, "minutos")
                print("Precio total es de: ", "$", precio_total )
                print("------------------------------------------------")
            elif descuento == "":
                hora_salida = datetime.now()
                tiempo_total = hora_salida - hora_entrada
                tiempo_total_seg = tiempo_total.total_seconds()
                precio_total = tiempo_total_seg * 1
                print("------------------------------------------------")
                print("Hr de entrada: ", hora_entrada, "Hr de salida: ", hora_salida)
                print("Su tiempo fue de: ", tiempo_total_seg, "minutos")
                print("Precio total es de: ", "$", precio_total)
                print("------------------------------------------------")



