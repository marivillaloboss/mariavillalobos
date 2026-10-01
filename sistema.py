from util import Mostrar_menu
lista = []
for i in range(3):
    texto = input('Ingrese una opcion: ')
    lista.append(texto)
seleccion = Mostrar_menu(lista)
print("Ustes elegio: ,seleccion")