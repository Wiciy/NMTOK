def czyParzysta(liczba) -> bool:
    if(liczba%2==0):
        return True
    else:
        return False

wynik = czyParzysta(26)

if(wynik):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")