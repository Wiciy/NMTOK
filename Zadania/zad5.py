def dlugoscListy(lista: list, dlugosc: int) -> bool:
    if(dlugosc == len(lista)):
        return True
    else:
        return False

lista = [1,2,3,4]
print(dlugoscListy(lista, 2))