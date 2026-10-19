def czySumaWieksza(liczba1: int, liczba2: int, liczba3: int) -> bool:
    if(liczba1+liczba2 >= liczba3):
        return True
    else:
        return False

print(czySumaWieksza(5,5,5))