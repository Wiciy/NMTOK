def is_palindrome(text: str) -> bool:
    odwrocony=""
    for litera in text:
        odwrocony = litera + odwrocony

    if text.lower() == odwrocony.lower():
        return True
    else:
        return False