from os import system

asientos = [[0 for x in range(10)] for y in range(10)]
asistentes = {}
precio = [120000 if i < 21 else 80000 if i < 51 else 50000 for i in range(100)]
ganancias = 0

def mostrar_asientos():
    for i in range(10):
        for j in range(10):
            if asientos[i][j] == 0:
                print(i * 10 + j + 1, end='\t')
            else:
                print('x', end='\t')
        print()

def comprar():
    global ganancias
    asiento = int(input("Ingrese el numero del asiento a escoger del 1 al 100: "))
    while asiento < 1 or asiento > 100:
        print("** Asiento invalido **")
        asiento = int(input("Ingrese el numero del asiento a escoger del 1 al 100: "))
    fila = (asiento - 1) // 10
    columna = (asiento - 1) % 10
    if asientos[fila][columna] != 0:
        print("** Asiento no disponible **")
        return
    run = int(input("Ingrese su run sin puntos ni guion: "))
    asientos[fila][columna] = run
    ganancias += precio[asiento - 1]
    print("\ Compra realizada con exito /")

def mostrar_disponibles():
    disponibles = sum([fila.count(0) for fila in asientos])
    print(f"hay {disponibles} asientos disponibles")

def listado_asist():
    lista_asistentes = []
    for fila in asientos:
        for run in fila:
            if run != 0:
                lista_asistentes.append(run)
    lista_asistentes.sort()
    print("Listado de asistentes:")
    for run in lista_asistentes:
        print(run)

def ganancias_total():
    print(f"Ganancias totales: ${ganancias}")

while True:
    system('cls')
   
    print("Entradas concierto de Michael Jam")
    print("1- Comprar entradas")
    print("2- Mostrar ubicaciones disponibles")
    print("3- Ver listado de asistentes")
    print("4- Mostrar ganancias totales")
    print("5- Salir")

    opc = int(input())
    while opc<1 or opc>5:
        print("Ingrese una opcion correcta")
        opc = int(input())
   
   
    if opc == 1:
        mostrar_asientos()
        comprar()
       
       
    elif opc == 2:
        mostrar_asientos()
        mostrar_disponibles()
       
    elif opc == 3:
        listado_asist()
        
    elif opc == 4:
        ganancias_total()
        
    elif opc == 5:
        print("Saliendo del sistema....")
        print("Daniel Azocar")
        print("10/01/2023")
        break

