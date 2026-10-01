def menu(lista):
    for i in range(len(lista)):
        print(i + 1, "-", lista[i])
    opcion = int(input("Elija una opción: "))
    return lista[opcion - 1]
textos = []
for i in range(3):
    texto = input("Ingrese una opcion: ")
    textos.append(texto)
print("MENU")
seleccion = menu(textos)
print("Usted eligio" ,seleccion)