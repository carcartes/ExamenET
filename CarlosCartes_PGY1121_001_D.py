import os

lst = list(range(1,101))

contPlat = 0
contGold = 0
ContSilver = 0

listaRut = []

menu = """
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
"""
menu2= """
1. Platinum $20.000.(Asientos del 1-20)
2. Gold $80.0000 (Asientos del 21 al 50)
3. Silver $50.000 (Asientos del 51 al 50)
"""
while True:
    try:
        opc = int(input(menu))
        if opc == 5:
            nombre = input("Cual es su nombre: ")
            apellido = input("Cual es su apellido: ")
            print(f"Adios {nombre} {apellido}, 10/07/23")
            input("Enter para finalizar")
            break
        elif opc == 1:
            while True:
                try:
                    cantEntradas = int(input("entradas: "))
                    if cantEntradas > 0 and cantEntradas <= 3:
                        print("Si el numero esta marcado con x el asiento no esta disponible")
                        print(lst)    
                        print(menu2)
                        for i in range (cantEntradas):
                            numAsiento = int(input("Ingrese el numero de asiento: "))
                            for i in range (101):
                                if numAsiento == lst[i]:
                                    lst[i] = ('x')
                                    if numAsiento >=1 and numAsiento <= 20:
                                        contPlat += 1
                                    elif numAsiento >=21 and numAsiento <= 50:
                                        contGold += 1
                                    elif numAsiento >=51 and numAsiento <= 100:
                                        ContSilver += 1
                                    elif numAsiento >= 1 and numAsiento <=100 and lst[i] == 'x':
                                        print("No disponible")
                                    else:
                                        print("Intente nuevamente")
                                    rut = int(input("rut: "))
                                    listaRut.append(rut)
                                    break
                        break
                    
                except:
                    print("Error vuelva ingresar la entrada, asiento(s) ocupados")

        elif opc == 2:
            print("Si el numero esta marcado con x el asiento no esta disponible")
            print(lst)
            

        elif opc == 3:
            print("Listado de asistentes")
            listaRut.sort()
            print(listaRut)
            

        elif opc == 4:
            print("Tipo Entrada | Cantidad     | Total")
            print(f"Platinum     | {contPlat}            | {contPlat*120000}")
            print(f"Gold         | {contGold}            | {contGold*80000}") 
            print(f"Silver       | {ContSilver}            | {ContSilver*50000}")
            print(f"TOTAL        | {contPlat+contGold+ContSilver}            | {contPlat*120000+contGold*80000+ContSilver*50000}")
            
    except:
        print("excepcion menu")

    
    
