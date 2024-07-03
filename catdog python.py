import random
from datetime import datetime


def generar_fecha_aleatoria():
    # Generar una fecha aleatoria en el año actual
    year = datetime.now().year
    month = 8
    day = random.randint(1, 28)  # Simplificación: todos los meses tendrán 28 días
    return datetime(year, month, day)

def ingreso_hora(lista_atencion):
        print("\tINGRESO DE DATOS")
        print("Ingrese el tipo de mascota ")
        numeroatencion = random.randrange(1,30)
        valoratencion = random.randrange(25000,50000)
        while True:
            try:
                tmascota = int(input("Ingrese una opcion (Perro: 1/Gato: 2): "))
                if tmascota not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Opción no válida. Por favor, ingrese 1 para Perro o 2 para Gato.")
                
        nmascota = input("Ingrese el nombre de la mascota: ")
        while 15 >= len(nmascota) <= 20:
             print("Debe ser un  nombre de entre 15 y 20 caracteres")
             nmascota = input("Ingrese el nombre de la mascota: ")

        print(f"numero de atencion: {numeroatencion}")
        print(f"Valor de atencion: {valoratencion}")
        numero = {"Tipo de mascota":tmascota,
                        "Nombre de mascota":nmascota,
                        "Numero de atencion":numeroatencion,
                        "Valor de atencion":valoratencion}
        
        lista_atencion.append(numero)   

def buscar_hora(lista_atecion):
        busqueda = int(input("Ingrese el numero de atencion: "))
        
        for numero in lista_atecion:
            if numero['Numero de atencion'] == busqueda:
                print("\tDATOS DE ATENCION")
                print("--------------------------------------")
                print(f"Tipo de mascota: {numero['Tipo de mascota']}\n"
                  f"Nombre de mascota: {numero['Nombre de mascota']}\n"
                  f"Numero de atencion: {numero['Numero de atencion']}\n"
                  f"Valor de atencion: ${numero['Valor de atencion']}\n"
                  "--------------------------------------")

def imprimir_hora(lista_atencion):
    busqueda = int(input("Ingrese el numero de atencion: "))
    
    for numero in lista_atencion:
        if numero['Numero de atencion'] == busqueda:
            fecha_impresion = generar_fecha_aleatoria()
            fecha_formateada = fecha_impresion.strftime("%d-%m-%Y")

            # Aplicar descuento si es un gato y el mes es agosto
            if numero['Tipo de mascota'] == 2 and fecha_impresion.month == 8:
                numero['Valor de atencion'] *= 0.8

            print("\tORDEN DE ATENCIÓN VETERINARIA")
            print(f"Fecha de Impresión: {fecha_formateada}")
            print(f"Tipo de Mascota: {numero['Tipo de mascota']}")
            print(f"Número de Atención: {numero['Numero de atencion']}")
            print(f"Valor de la Atención: ${numero['Valor de atencion']:.2f}")
            print(f"Nombre de la Mascota: {numero['Nombre de mascota']}")
            print("--------------------------------------")
     

def main ():


    lista_atencion = []

    opc = 0
    while opc != 4:
        print("\tMENU PRINCIPAL\n"
            "1.-Pedir numero\n"
            "2.-Buscar antecion\n"
            "3.-Imprimir orden de atencion\n"
            "4.-Salir")
        opc = int(input("Seleccione una opcion:"))
        if opc == 1:
            ingreso_hora(lista_atencion)
            
        if opc == 2:
            buscar_hora(lista_atencion)

        if opc == 3:
            imprimir_hora(lista_atencion)
        if opc == 4:
            print("Programa finalizado")

main()
