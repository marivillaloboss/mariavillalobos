asientos = []
for fila in range(12):
    asientos.append([0, 0, 0, 0])
seguir = "si"
while seguir == "si":
    print("\nMAPA DEL COLECTIVO")
    for fila in range(12):
        for columna in range(4):
            if asientos[fila][columna] == 0:
                print("☺", end=" ")
            else:
                print("☻", end=" ")
        print()
    fila = int(input("Ingrese la fila (1 a 12): "))
    columna = int(input("Ingrese la columna (1 a 4): "))
    if asientos[fila - 1][columna - 1] == 0:
        asientos[fila - 1][columna - 1] = 1
        print("Asiento reservado.")
    else:
        print("Ese asiento ya está ocupado.")
    seguir = input("¿Desea realizar otra reserva? (si/no): ")
    ocupados = 0
    libres = 0
    for fila in range(12):
        for columna in range(4):
            if asientos[fila][columna] == 1:
                ocupados += 1
            else:
                libres += 10
            print("\nOCUPACIÓN ACTUAL")
            print("Asientos ocupados:", ocupados)
            print("Asientos libres:", libres)