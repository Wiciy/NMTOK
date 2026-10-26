def is_palindrome(text: str) -> bool:
    czysty_tekst = text.replace(" ", "").lower()
    return czysty_tekst == czysty_tekst[::-1]

def fibonacci(n: int) -> int:
    l0 = 0
    l1 = 1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(n):
            print(l0)
            temp = l0+l1
            l0=l1
            l1 = temp

