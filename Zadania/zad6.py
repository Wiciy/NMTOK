def laczListy(lista1: list, lista2: list) -> list:
    list3 = []
    for elem in lista1:
        if elem not in lista2:
            list3.append(elem)
    for elem in lista2:
        if elem not in lista1:
            list3.append(elem)

    for i in range(len(list3)):
        list3[i] = list3[i]**3

    return list3

list1 = [1,2,3]
list2 = [1,2,3,4]

print(laczListy(list1,list2))