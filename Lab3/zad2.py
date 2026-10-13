#Sposób 1
listaLiczb = [10, 44, 90, 86, 100]
def razy_dwa(lista):
    for i in range(len(lista)):
        lista[i] *= 2
    for liczba in lista:
        print(liczba)

razy_dwa(listaLiczb)

#Sposób 2
liczby = [10, 44, 90, 86, 100]
dwukrotnosc_liczb = [liczba*2 for liczba in liczby]

print(dwukrotnosc_liczb)